pip install pyautogui
import pyautogui, time
time.sleep(5)
f = open("setrain",'r')
for word in f:
pyautogui.typewrite(word)
pyautogui.press("enter")
