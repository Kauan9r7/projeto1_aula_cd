import pyautogui
import time
import pandas

tabela_produtos = pandas.read_csv("produtos.csv")

print(tabela_produtos)
pyautogui.sleep(5)
print(pyautogui.position())