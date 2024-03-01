import pyautogui
import time
import threading
from pynput.keyboard import Controller as KeyController, Key, Listener

def zarzuc_wedke():
    x = 651
    y = 894
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.click()
    print("Zarzucam wedkę")

def sprawdz_kolor(x, y, kolor, komunikat):
    pixel_color = pyautogui.pixel(x, y)
    if pixel_color == kolor:
        print(komunikat)
        return True
    return False

def klikaj_spacje():
    keyboard = KeyController()
    while True:
        if sprawdz_kolor(655, 652, (54, 175, 49), "Zarzucam wedkę") or sprawdz_kolor(851, 901, (202, 159, 111), "Złowiłem"):
            break
        with keyboard.pressed(Key.space):
            time.sleep(0.04)  

def klikacz():
    keyboard = KeyController()
    while True:
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        time.sleep(23)

if __name__ == "__main__":
    esc_thread = threading.Thread(target=klikacz)
    esc_thread.daemon = True
    esc_thread.start()

    zarzuc_wedke()
    while True:
        klikaj_spacje()
