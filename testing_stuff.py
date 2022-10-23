
from calendar import c
from heapq import merge
import tkinter as tk
from turtle import onclick
from unittest import result
from PIL import Image,ImageTk
from click import command
from sqlalchemy import all_, column, true
import random
from tkinter import ttk
import os
from os import listdir
from functools import partial
import numpy as np

im = Image.open('C:/Summer_Projects/Images/amazing-beach.jpg','r')

pix_val = list(im.getdata())

pix_val_flat = [x for sets in pix_val for x in sets]

total = 0
for x in pix_val_flat:
    if x >100:
        total += 1

print(total)
print(sum(pix_val_flat))