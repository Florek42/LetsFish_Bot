import pyautogui
import time
import random

def przenies_i_kliknij():
    pyautogui.moveTo(655, 891, duration=1)
    pyautogui.click()

def sprawdz_kolor_i_trzymaj_spacje():
    kolor_piksela = pyautogui.pixel(655, 891)
    dopuszczalne_kolory = [(215, 180, 138), (217, 184, 142)]

    if kolor_piksela in dopuszczalne_kolory:
        czas_trzymania = random.uniform(0.1, 0.94)
        pyautogui.keyDown('space')
        
        # Czekaj, aż pojawi się kolor (61, 99, 135) na x=758, y=704
        while pyautogui.pixel(758, 704) != (61, 99, 135):
            time.sleep(0.1)
        
        pyautogui.keyUp('space')

def trzymaj_i_pusc_spacje():
    while pyautogui.pixel(576, 673) != (255, 255, 255):
        time.sleep(0.1)

    while pyautogui.pixel(749, 693) != (255, 255, 255):
        pyautogui.keyDown('space')
        time.sleep(0.1)

    pyautogui.keyUp('space')

def przenies_i_kliknij_po_kolorze():
    pyautogui.keyUp('space')
    time.sleep(1)
    pyautogui.moveTo(929, 533, duration=1)
    
    kolor_piksela_5 = pyautogui.pixel(929, 533)
    oczekiwany_kolor_5 = (228, 206, 182)

    if kolor_piksela_5 == oczekiwany_kolor_5:
        pyautogui.click()

# Pierwszy etap
przenies_i_kliknij()
sprawdz_kolor_i_trzymaj_spacje()

# Drugi etap
trzymaj_i_pusc_spacje()
trzymaj_i_pusc_spacje()

# Trzeci etap
przenies_i_kliknij_po_kolorze()
