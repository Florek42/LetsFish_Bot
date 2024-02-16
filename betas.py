import pyautogui
import time
from pynput.keyboard import Controller as KeyController, Key

def zarzuc_wedke():
    x = 651
    y = 894
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.click()
    print("Zarzucam wedkę")

def sprawdz_kolor(x, y, kolor):
    return pyautogui.pixelMatchesColor(x, y, kolor)

def klikaj_spacje():
    keyboard = KeyController()
    while True:
        if sprawdz_kolor(655, 652, (54, 175, 49)) or sprawdz_kolor(851, 901, (194, 146, 91)):
            break
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        time.sleep(0.1)  # Dodajemy opóźnienie 0.1 sekundy

if __name__ == "__main__":
    zarzuc_wedke()
    klikaj_spacje()
