import pyautogui
import time
import keyboard
import random
import string

print("---------Super Simple---------")
print(" ▄▄· ▄▄▄▄▄▄▄▄  ▄▄▌       ▌ ▐·")
print("▐█ ▌▪•██  ▀▄ █·██•      ▪█·█▌")
print("██ ▄▄ ▐█.▪▐▀▀▄ ██▪      ▐█▐█•")
print("▐███▌ ▐█▌·▐█•█▌▐█▌▐▌     ███ ")
print("·▀▀▀  ▀▀▀ .▀  ▀.▀▀▀     . ▀  ")
print("------------Spammer-----------")
print("Created by Nico")
print("")
print("╔══════════ Mode ═══════════╗")
print("║                           ║")
print("║ 1. Spam Ctrl + V          ║")
print("║ 2. Spam Ctrl + V + Enter  ║")
print("║ 3. Ctrl + V Bypass        ║")
print("║ 4. Ctrl + V + Enter Bypass║")
print("║ 5. Exit                   ║")
print("║                           ║")
print("╚═══════════════════════════╝")
mode = input("Press number + enter to select mode: ")

if mode == ("1"):
    pulsaciones_por_segundo = int(input("Number of times per second: "))
    intervalo = 1 / pulsaciones_por_segundo
    while True:
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(intervalo)

if mode == ("2"):
    pulsaciones_por_segundo = int(input("Number of times per second: "))
    intervalo = 1 / pulsaciones_por_segundo
    while True:
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(intervalo)

if mode == ("3"):
    def generar_numero_aleatorio_cercano(numero):
        numero_aleatorio = random.uniform(numero - 0.20, numero + 0.20)
        return numero_aleatorio


    try:
        numero_ingresado = float(input("Number of times per second:"))
        numero_aleatorio = generar_numero_aleatorio_cercano(numero_ingresado)
    except:
        print("Error")


    def generar_letras_aleatorias():
        letras_aleatorias = ''.join(random.choice(string.ascii_letters) for _ in range(3))
        return letras_aleatorias


    while True:
        letras_generadas = generar_letras_aleatorias()
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(letras_generadas)
        time.sleep(numero_aleatorio)

if mode == ("4"):
    def generar_numero_aleatorio_cercano(numero):
        numero_aleatorio = random.uniform(numero - 0.20, numero + 0.20)
        return numero_aleatorio


    try:
        numero_ingresado = float(input("Number of times per second:"))
        numero_aleatorio = generar_numero_aleatorio_cercano(numero_ingresado)
    except:
        print("Error")


    def generar_letras_aleatorias():
        letras_aleatorias = ''.join(random.choice(string.ascii_letters) for _ in range(3))
        return letras_aleatorias


    while True:
        letras_generadas = generar_letras_aleatorias()
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(letras_generadas)
        pyautogui.press('enter')
        time.sleep(numero_aleatorio)


if mode == ("5"):
    exit




