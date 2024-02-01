import tkinter as tk
import pyautogui
import time
import random

def start_bot(event=None):
    # Przesuń kursor na pozycję (655, 891) i kliknij go
    pyautogui.moveTo(655, 891, duration=1)
    pyautogui.click()

    # Poczekaj 2 sekundy
    time.sleep(2)

    while True:
        # Klikaj myszką losowo przez czas od 0.03 do 0.07
        czas_klikniecia = random.uniform(0.03, 0.07)
        pyautogui.click()
        time.sleep(czas_klikniecia)

        # Sprawdź kolor na pozycji x=655, y=891
        kolor_piksela_koniec = pyautogui.pixel(655, 891)
        if kolor_piksela_koniec == (229, 207, 183):
            print("wykryto koniec")
            break

# Utwórz główne okno
root = tk.Tk()
root.title("Let's Fish Bot By Forek42")
root.geometry("600x400")
root.configure(bg="blue")

# Dodaj napis na górze
label_title = tk.Label(root, text="Let's Fish Bot By Forek42", font=("Helvetica", 16), bg="blue", fg="white")
label_title.pack(pady=10)

# Dodaj przycisk Start i przypisz klawisz F8
button_start = tk.Button(root, text="Start (F8)", command=start_bot)
button_start.pack(pady=10)
root.bind("<F8>", start_bot)  # Przypisanie klawisza F8 do przycisku Start

# Dodaj przycisk Stop i przypisz klawisz F9
button_stop = tk.Button(root, text="Stop (F9)")
button_stop.pack(pady=10)

# Dodaj napis "SPINNING ONLY"
label_spinning_only = tk.Label(root, text="(SPINNING ONLY)", font=("Helvetica", 12), bg="blue", fg="white")
label_spinning_only.pack(pady=5)

# Uruchom główną pętlę
root.mainloop()
