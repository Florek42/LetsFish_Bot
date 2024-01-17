import time
import random
import pyautogui

def lfb():
    while True:
        # Sprawdź kolor piksela na pozycji (749, 692)
        while pyautogui.pixel(749, 692) == (61, 99, 135):
            # Jeśli kolor na (749, 692) to (61, 99, 135), przestań trzymać spację
            pyautogui.keyUp('space')
            time.sleep(random.uniform(0.3, 0.7))

            # Poczekaj, aż kolor (61, 99, 135) na (749, 692) zmieni się na inny
            while pyautogui.pixel(749, 692) == (61, 99, 135):
                time.sleep(0.1)

            # Zacznij trzymać spację
            pyautogui.keyDown('space')

        # Przesuń kursor myszy do pozycji "zarzuc_wedke"
        pyautogui.moveTo(655, 891, duration=1)

        # Kliknij lewym przyciskiem myszy
        pyautogui.click()

        # Sprawdź kolor piksela na pozycji (655, 891)
        while pyautogui.pixel(655, 891) == (215, 180, 138):
            # Trzymaj spację przez losowy czas od 1.1 do 3.3 sekundy
            pyautogui.keyDown('space')
            time.sleep(random.uniform(1.1, 3.3))

            # Poczekaj, aż kolor (215, 180, 138) na (655, 891) zniknie
            while pyautogui.pixel(655, 891) == (215, 180, 138):
                time.sleep(0.1)

            # Puść spację
            pyautogui.keyUp('space')

if __name__ == "__main__":
    lfb()


# gdy pojawia sie pasek lowienia ten zielono czerwony to za szybko ciagnie bot