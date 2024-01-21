import pyautogui
import random
import time

def main():
    try:
        # Przeniesienie kursora na x=655, y=891 i kliknięcie lewego przycisku myszy
        pyautogui.moveTo(655, 891, duration=1)
        pyautogui.click()

        while True:
            # Trzymanie przycisku spacji losowo przez czas od 0.1 do 0.94
            czas_trzymania_spacji = random.uniform(0.1, 0.94)
            pyautogui.keyDown('space')
            time.sleep(czas_trzymania_spacji)
            pyautogui.keyUp('space')

            # Sprawdzenie koloru na pozycji x=758, y=704
            kolor_piksela_spacji = pyautogui.pixel(758, 704)
            if kolor_piksela_spacji == (61, 99, 135):
                break

            # Sprawdzenie koloru na pozycji x=575, y=674
            kolor_piksela_bialy_lewa = pyautogui.pixel(575, 674)
            biale_kolory = [(74, 182, 48), (48, 91, 45), (82, 191, 42, 255), (60, 179, 47, 255)]
            if kolor_piksela_bialy_lewa in biale_kolory:
                print("wykryto_bialy_lewa")

    except KeyboardInterrupt:
        print("\nProgram zakończony.")

if __name__ == "__main__":
    main()
