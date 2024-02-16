from pynput.mouse import Controller, Button
from pynput.keyboard import Controller as KeyController, Key
import time
import random

def main():
    # Przeniesienie kursora na pozycję (655, 891) i kliknięcie lewego przycisku myszy
    mouse = Controller()
    mouse.position = (655, 891)
    mouse.click(Button.left, 1)

    # Poczekaj 3 sekundy
    time.sleep(3)

    # Klikaj spację w losowych odstępach czasowych od 0.15 do 0.25, dopóki nie pojawi się kolor (70, 49, 34) na ekranie w miejscu (927, 534)
    while not check_pixel_color(927, 534, (70, 49, 34)):
        czas_klikniecia = random.uniform(0.15, 0.25)
        press_and_release_key(Key.space)
        time.sleep(czas_klikniecia)

    # Przestań klikanie spacji
    release_key(Key.space)

    # Przenieś kursor na pozycję (927, 534) i kliknij lewym przyciskiem myszy raz
    mouse.position = (927, 534)
    mouse.click(Button.left, 1)

    print("Zakończyłem zadanie")

def press_and_release_key(key):
    keyboard = KeyController()
    keyboard.press(key)
    keyboard.release(key)

def release_key(key):
    keyboard = KeyController()
    keyboard.release(key)

def check_pixel_color(x, y, expected_color):
    mouse = Controller()
    actual_color = mouse.position = (x, y)
    return actual_color == expected_color

if __name__ == "__main__":
    main()
