import pyautogui
import time
import keyboard

print("---------Super Simple---------")
print (" ▄▄· ▄▄▄▄▄▄▄▄  ▄▄▌       ▌ ▐·")
print ("▐█ ▌▪•██  ▀▄ █·██•      ▪█·█▌")
print ("██ ▄▄ ▐█.▪▐▀▀▄ ██▪      ▐█▐█•")
print ("▐███▌ ▐█▌·▐█•█▌▐█▌▐▌     ███ ")
print ("·▀▀▀  ▀▀▀ .▀  ▀.▀▀▀     . ▀  ")
print("------------Spammer-----------")
print("Created by Nico")
print("")
print("╔══════════ Mode ══════════╗")
print("║                          ║")
print("║ 1. Spam Ctrl + V         ║")
print("║ 2. Spam Ctrl + V + Enter ║")
print("║ 3. Exit                  ║")
print("║                          ║")
print("╚══════════════════════════╝")
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
    exit
    
    
