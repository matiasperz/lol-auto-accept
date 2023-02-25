import psutil
import pyautogui
from python_imagesearch.imagesearch import imagesearch_loop, imagesearch
import sys, time

pyautogui.FAILSAFE = False
TIMELAPSE = 2
TIMELAPSE1 = 2
TIMELAPSE2 = 0.5

acceptButtonImg = './img/sample.png'
acceptedButtonImg = './img/sample-accepted.png'
championSelectionImg_flash = './img/flash-icon.png'
championSelectionImg_emote = './img/runes-icon.png'
lobbyImg = './img/lobby.png'

waitingPlayers=False
champSelection=False

def checkProcess(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def checkGameAvailableLoop():
    global TIMELAPSE, TIMELAPSE1, TIMELAPSE2, waitingPlayers
    while True:
        pos = imagesearch(acceptButtonImg, 0.8)
        if not pos[0] == -1:
            pyautogui.click(pos[0]+10, pos[1]+10)
            print("Partida aceptada!")
            TIMELAPSE=TIMELAPSE2
            break
        
        time.sleep(TIMELAPSE)
    

def checkChampionSelection():
    flash = imagesearch(championSelectionImg_flash)
    emote = imagesearch(championSelectionImg_emote)

    if not emote[0] == -1 or not flash[0] == -1:
        return True
    else:
        return False

def checkGameCancelled():
    global TIMELAPSE, TIMELAPSE1, TIMELAPSE2, waitingPlayers
    accepted = imagesearch(acceptedButtonImg)
    lobby = imagesearch(lobbyImg)

    if not accepted[0] == -1 and not lobby[0] == -1:
        if not waitingPlayers:
            print("Esperando al resto de jugadores...")
            waitingPlayers=True
        return False
    if accepted[0] == -1 and not lobby[0] == -1:
        waitingPlayers=False
        TIMELAPSE=TIMELAPSE1
        return True
    else:
        return False

def checkLeagueClient():
    if not checkProcess("LeagueClient.exe"):
        print("Cliente cerrado. Saliendo.")
        time.sleep(5)
        sys.exit()

def main():
    global TIMELAPSE, TIMELAPSE1, TIMELAPSE2, waitingPlayers, champSelection
    run = True

    print("Detectando Cliente de League of Legends... ")
    while True:
        if checkProcess("LeagueClient.exe"):
            print("Cliente de League of Legends detectado.")
            break
        time.sleep(3)

    while True:
        checkLeagueClient()
        checkGameAvailableLoop()
        time.sleep(TIMELAPSE)

        while True:
            checkLeagueClient()
            if checkProcess("League of Legends.exe"):
                print("Partida en curso... ")
                while True:
                    if not checkProcess("League of Legends.exe"):
                        print("Partida finalizada.")
                        break
                    time.sleep(3)
                break

            if checkGameCancelled():
                print("La partida ha sido cancelada, esperando...")
                champSelection=False
                waitingPlayers=False
                TIMELAPSE=TIMELAPSE1
                break
            
            if checkChampionSelection():
                if not champSelection:
                    print("Selección de campeón detectada")
                    champSelection=True
                    waitingPlayers=False
                    TIMELAPSE=TIMELAPSE1
                time.sleep(TIMELAPSE)

            time.sleep(TIMELAPSE)
        

if __name__ == '__main__':
    print("Iniciado.")
    main()
