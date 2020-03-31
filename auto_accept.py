import pyautogui
from python_imagesearch.imagesearch import imagesearch_loop, imagesearch
import time

pyautogui.FAILSAFE = False
TIMELAPSE = 1

acceptButtonImg = './sample.png'
acceptedButtonImg = './sample-accepted.png'
championSelectionImg_flash = './flash-icon.png'
championSelectionImg_emote = './emote-icon.png'
playButtonImg = './play-button.png'

def checkGameAvailableLoop():
    while True:
        pos = imagesearch(acceptButtonImg, 0.8)
        if not pos[0] == -1:
            pyautogui.click(pos[0], pos[1])
            print("Game accepted!")
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
    accepted = imagesearch(acceptedButtonImg)
    play = imagesearch(playButtonImg)

    if accepted[0] == -1 and not play[0] == -1:
        return True
    else:
        return False


def main():
    run = True

    while run is True:
        checkGameAvailableLoop()
        time.sleep(TIMELAPSE)

        while True:
            cancelled = checkGameCancelled()
            if cancelled is True:
                print("Game has been cancelled, waiting...")
                break
            
            csResult = checkChampionSelection()
            if csResult is True:
                print("Champion selection! Good Luck :D")
                time.sleep(TIMELAPSE)
                run = False
                break

            time.sleep(TIMELAPSE)
        

if __name__ == '__main__':
    print("Running...")
    main()