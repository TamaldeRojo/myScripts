import pyautogui



def main():
    sWidth, sHeight = pyautogui.size()
    while True:
        currentXmouse, currentYmouse = pyautogui.position()
        print(f"X: {currentXmouse} und Y:{currentYmouse}")
        # if currentYmouse == 0:
        #     # pyautogui.moveTo()
        #     pyautogui.click(600,488)
        #     pyautogui.click(600,800)
        #     pyautogui.scroll(-200)
        #     pyautogui.click(600,508)
        #     pyautogui.scroll(-200)
        #     pyautogui.click(600,730)

    



if __name__ == "__main__":
    main()