import time
import pyautogui

def wypisz_kolor_piksela():
    while True:
        # Pobierz aktualną pozycję kursora
        x, y = pyautogui.position()

        # Pobierz kolor piksela na danej pozycji
        kolor = pyautogui.pixel(x, y)

        print(f'Kolor piksela na pozycji x={x}, y={y}: {kolor}')

        # Czekaj 2 sekundy
        time.sleep(0.5)

if __name__ == "__main__":
    wypisz_kolor_piksela()
