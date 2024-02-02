from pynput import keyboard, mouse
import time
import random

running = False  # Zmienna śledząca, czy program jest uruchomiony

def on_press(key):
    global running

    if key == keyboard.Key.f8:
        if not running:
            print("Start")
            running = True
            fish()

        else:
            print("Stop")
            running = False

def on_release(key):
    pass

def fish():
    global running

    while running:
        # Przesuń kursor na pozycję (655, 891)
        mouse_controller = mouse.Controller()
        mouse_controller.position = (655, 891)

        # Szybko klikaj myszką losowo przez czas od 0.02 do 0.04
        czas_klikniecia = random.uniform(0.02, 0.04)
        mouse_controller.click(mouse.Button.left, 2)  # 2 oznacza dwukrotne kliknięcie lewym przyciskiem myszy

        # Sprawdź kolor na pozycji x=758, y=704
        kolor_piksela_ryba = mouse_controller.position
        if kolor_piksela_ryba == (758, 704) and pyautogui.pixel(758, 704) == (61, 99, 135):
            print("Ryba złowiona")
            break

        time.sleep(0.1)  # Czas przerwy między kolejnymi iteracjami

# Utwórz obiekt nasłuchujący klawiaturę
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# Trzymaj program uruchomiony
while True:
    pass
