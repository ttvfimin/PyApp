# Licensed under GNU/GPU. All code written is my own OR written in collaboration with another person. Please read credits.md for more information.

import random as r
import time as t
import os
import hangman as h
import platform as pl
from colored import fg

def login(us, pa):
  if us == "kcliix":
    if pa == "kcliix":
      return True
  else:
    return False

def mm(user):
  h.hangman.clear(pl.system())
  wTD = input("1) Calculator\n2) Hangman\n3) Exit\n>")
  if wTD == "1":
    #calculator().run()
    print("Not implemented")
  elif wTD == "2":
    h.hangman.start()
    print("%s " % (fg(15)))
  elif wTD == "3":
    exit("Thanks for using PyApp!")

if __name__ == "__main__":
  u = input("Username\n> ")
  p = input("Password\n> ")
  if login(u, p):
    while 1:
      mm(u)