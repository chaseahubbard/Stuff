'''
Ideas for additional features:
Add lots of additional images see what happens

Make it look nicer
Give the images additional attributes 
Make an AI that also sorts the images based on something

stop screen tearing when scrolling
'''

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

im = Image.open('C:\Summer_Projects\Images\amazing-beach.jpg','r')

pix_val = list(im.getdata())

pix_val_flat = [x for sets in pix_val for x in sets]