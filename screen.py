'''
Ideas for additional features:

Make it look nicer
Give the images additional attributes 
Make an AI that also sorts the images based on something

stop screen tearing when scrolling

horizontal scrollbar needs to go across the screen but is hard like really hard
'''

from calendar import c
from heapq import merge
import tkinter as tk
from turtle import onclick
from unittest import result
from PIL import Image,ImageTk,ImageFile
from click import command
from sqlalchemy import all_, column, true
import random
from tkinter import ttk
import os
from os import listdir
from functools import partial
import numpy as np
from sympy import comp

ImageFile.LOAD_TRUNCATED_IMAGES = True
HEIGHT = 300
WIDTH = 200
storage_dict = {}
storage_dict2 = {}
img_list = []
img2_list = []
counting = 2
storage_list = []
store_counts = 0
storage_list2 = []
temp_storage2 = []
temp_storage1 = []
all_images_dict = {}
ranking_storage = {}
first = 0 
lives = 1
button_list = []
label_list = []
number_of_buttons = 3
bstore = {}
count4 = 0
end_screen_number = 1000000
count5 = 0
count6 = 0
roundnum = 0
roundn = 0
all_current_values = []
prewinner = 0
comparitor = {}

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

def random_generation_temp():
    for x in temp_storage1:
        if x != end_screen_number:
            all_images_dict[x][3] = np.random.poisson(4,1)

def random_generation_first():
    for x in range(number_of_buttons):
        if x != end_screen_number:
            all_images_dict[x][3] = np.random.poisson(4,1)


def power(n):
    end_check = 0
    winner = {0:0,1:0}
    power = {'attack':0, 'defense':0,"speed":0,"magic":0,4:0, 5:0}
    winner = {'attack':0, 'defense':0,"speed":0,"magic":0,4:0, 5:0}
    global comparitor
    global roundnum
    global count6
    global all_current_values
    global prewinner
    
    img = ImageTk.getimage(all_images_dict[n][0])
    pix_val = list(img.getdata())
    #pix_val_flat = [x for sets in pix_val for x in sets]
    total = {0:0,1:0,2:0,3:0}      
    for x in pix_val:
        for y in range(len(x)):
            total[y] += x[y]    
    power['attack'] = [(total[0]/1000000)]#**np.random.poisson(2,1))//4
    power['defense'] = [(total[1]/1000000)]#**np.random.exponential(4,1)//2
    power["speed"] = [(total[2]/1000000) ] #* p.random.normal(10,1,1)
    if (total[3]/1000000) > 70:
        power['magic'] = 100 + ((total[3]/1000000) - 70)
    else:
        power['magic'] = [0]
    power[4] = [n]
    power[5] = roundnum
    return power

def ai():
    end_check = 0
    winner = {0:0,1:0}
    #power = {'attack':0, 'defense':0,"speed":0,"magic":0,4:0, 5:0}
    winner = {'attack':0, 'defense':0,"speed":0,"magic":0,4:0, 5:0}
    global comparitor
    global roundnum
    global count6
    global all_current_values
    global prewinner

    double_check = 0        
    for n in temp_storage1:
        if n!= end_screen_number:
            if n not in all_current_values:
                pow = power(n)
                
                
                comparitor[count6] = pow
                
                count6 += 1
                all_current_values.append(n)
                double_check = 1

        end_check = 1
    if double_check == 1:
        for x in comparitor:
            if comparitor[x][5] == roundnum:
                if (comparitor[x]['speed'][0] + comparitor[x]['attack'][0] )> winner['defense']:
                    if (winner['attack'] + winner['magic']) < comparitor[x]['defense'][0] + comparitor[x]['speed'][0]:
                        for y in winner.keys():
                            if y != 5:
                                print('the winners defense ' + str(winner['defense']))
                                print('attackers score ' + str(comparitor[x]['speed'][0] + comparitor[x]['attack'][0] ))
                                winner[y] = comparitor[x][y][0]
    else:
        winner[4] = prewinner
        prewinner = 0
    print(comparitor)
    roundnum += 1
    print(winner)    
    prewinner = winner[4]
    if end_check == 1:
        return winner[4]
    if end_check == 0:
        return end_screen_number
    

def f_ai():
    winner = {0:0,1:0}
    for x in range(number_of_buttons):
        
        if all_images_dict[x][3] > winner[0]:
            winner[0] = all_images_dict[x][3]
            winner[1] = x
    #print(winner[1])
    return winner[1]


'''
Now I need to create some ideas for what should be in these battle spaces
Not sure what principles I should add
Also should make so there is text that appears that says what happened maybe at the bottom of the screen
Also should make it have inputable variables
What else not sure 
probably should just try to put in a couple random distributions and get it working so that it automatically chooses a
and option before I think much more about what to implement 
'''
def Updates_Images(c): 
    global storage_dict2
    global img_list
    global counting
    global storage_dict
    global store_counts
    global temp_storage1
    global ranking_storage
    global all_images_dict
    global first
    global bstore
    global count4
    global lives    
    
    
    for x in range(number_of_buttons):
        try:
            temp_storage1.append(c[x])
            label_change = label_list[x]
            label_change.config(image = all_images_dict[c[x]][0])
        except:
            label_change = label_list[x]
            label_change.config(image = Final_Screen)
            temp_storage1.append(end_screen_number) 


def Resets_the_Images():
    for x in storage_dict.values():
        bstore[count4] = x
        count4 += 1
        
    storage_dict = {k: v for k, v in storage_dict.items() if v != end_screen_number}
        
    bstore.update(storage_dict)
    count3 = 0
    for x in storage_dict.values():
        ranking_storage[count3] = x
        all_images_dict[x][1] = lives
        all_images_dict[x][2] += 1

        count3 += 1
    storage_dict = {}
    storage_dict2 = {}    
    store_counts = 0
    c = []
    for x in all_images_dict.keys():
        if all_images_dict[x][1] > 0:
            c.append(x)
            
    random.shuffle(c)
    if len(c) > 0:
        Updates_Images(c)


def Image_lives_Counter(buttons_pressed_number):
    for x in range(number_of_buttons):
        try:
            if temp_storage1[x] != end_screen_number:
                if x == buttons_pressed_number:
                    
                    all_images_dict[temp_storage1[buttons_pressed_number]][1] = 0
                else:
                    all_images_dict[temp_storage1[x]][1] -= 1
            else:
                pass
        except:
            print('the problem comes from this number ' + str(x))
           # print(temp_storage1)

def Still_Alive_Images():
    c = []
    for x in all_images_dict.keys():
        if all_images_dict[x][1] > 0:
            c.append(x)
    return c

def on_click(args,buttons_pressed_number):
    if args == 1 or args == 2 : 
        global storage_dict2
        global img_list
        global counting
        global storage_dict
        global store_counts
        global temp_storage1
        global ranking_storage
        global all_images_dict
        global first
        global bstore
        global count4
        global lives
        global count5
        global all_current_values

        if len(storage_dict) != 0 or len(storage_dict2) != 0 :
            if args == 1:
                Image_lives_Counter(buttons_pressed_number)
            if args == 2:
                random_generation_temp()
                a = ai()
                Image_lives_Counter(a)
            c = []
            for x in all_images_dict.keys():
                if all_images_dict[x][1] > 0:
                    c.append(x)
                    
            random.shuffle(c)
            if args == 1:
                storage_dict[store_counts] = temp_storage1[buttons_pressed_number]
            
            if args == 2:
                ab = ai()
                storage_dict[store_counts] = ab
            store_counts += 1
            
            temp_storage1 = []
        
            if len(c) > 0:
                Updates_Images(c)
                
            else:
                
                for x in storage_dict.values():
                    bstore[count4] = x
                    count4 += 1
                    
                storage_dict = {k: v for k, v in storage_dict.items() if v != end_screen_number}
                    
                
                
                
                print('this is the value in bstore for the else statement')
                #print(bstore)
                count3 = 0
                for x in storage_dict.values():
                    ranking_storage[count3] = x
                    all_images_dict[x][1] = lives
                    all_images_dict[x][2] += 1
                    all_current_values = []
                    count3 += 1
                storage_dict = {}
                storage_dict2 = {}    
                store_counts = 0
                c = []
                for x in all_images_dict.keys():
                    if all_images_dict[x][1] > 0:
                        c.append(x)
                        
                random.shuffle(c)
                if len(c) > 0:
                    Updates_Images(c)
                print('this is the temporary storage value for the else statment in the if statment')
                #print(temp_storage1)
                
        elif first != 0:
            if args == 1:
                Image_lives_Counter(buttons_pressed_number)
            if args == 2:
                
                random_generation_temp()
                a = ai()
                Image_lives_Counter(a)

            c = []
            for x in all_images_dict.keys():
                if all_images_dict[x][1] > 0:
                    c.append(x)
            random.shuffle(c)      
            if args == 1:
                storage_dict[store_counts] = temp_storage1[buttons_pressed_number]
            if args == 2:
                ab = ai()
                storage_dict[store_counts] = ab

            store_counts += 1
            temp_storage1 = []

            if len(c) > 0:
                Updates_Images(c)
                
            else:
                label_change = label_list[buttons_pressed_number]
                label_change.config(image = Final_Screen)
                temp_storage1.append(end_screen_number)

        else:
            if args == 1:
                storage_dict[store_counts] = buttons_pressed_number
            elif args == 2:
                random_generation_first()
                ab = f_ai()
                storage_dict[store_counts] = ab
            store_counts += 1
            temp_storage1 = []
            if args == 1:
                for x in range(number_of_buttons):
                    if x == buttons_pressed_number:
                        all_images_dict[buttons_pressed_number][1] = 0
                    else:
                        all_images_dict[x][1] -= 1
            elif args == 2:
                for x in range(number_of_buttons):
                    ab = f_ai()
                    if x == ab:
                        all_images_dict[ab][1] = 0
                    else:
                        all_images_dict[x][1] -= 1
            c = []
            for x in all_images_dict.keys():
                if all_images_dict[x][1] > 0:
                    c.append(x)
                    
            random.shuffle(c)
            if len(c) > 0:
                Updates_Images(c)
            first = 1 

    if args == 3:
        r_storage = Merge(storage_dict,storage_dict2)
        Storage_Window(root,r_storage,args)

    if args == 4:
        #bstore = {k: v for k, v in bstore.items() if v != end_screen_number}
        Storage_Window(root,bstore,args)

    if args == 5:
        bstore = {k: v for k, v in bstore.items() if v != end_screen_number}
        result = {}
        for key,value in bstore.items():
            if value not in result.values():
                result[key] = value
        Storage_Window(root,result,args)
        
class Storage_Window:

    def __init__(self, master,Dictionary,args):
        self.total_rows = len(Dictionary)
        self.newWindow = tk.Toplevel(master)

        self.canvas=tk.Canvas(self.newWindow)
        self.scrollbar=ttk.Scrollbar(self.newWindow, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        self.scrollbar2 = ttk.Scrollbar(self.newWindow, orient= 'horizontal', command= self.canvas.xview)
        self.scrollable_frame.bind(
        "<Configure>",
        lambda e: self.canvas.configure(
        scrollregion=self.canvas.bbox("all")
        )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind_all('<MouseWheel>', self.onmousewheel)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")


        self.canvas.configure(xscrollcommand= self.scrollbar2.set)
        #self.canvas.pack(side="top", fill="both", expand=True)
        self.scrollbar2.pack(side="bottom", fill="x")        


        xcol = 0
        ycol = 0
        yl = []
        storagex = {0:0,1:0,2:0}
        for y in Dictionary.keys():
            yl.append(y)
        yl.sort()
        if args == 3 or args == 4:
            for x in yl:
                
                self.nlabel = tk.Label(self.scrollable_frame,image = all_images_dict[Dictionary[x]][0])
                self.nlabel.grid(row = ycol, column= xcol, sticky= 'nsew')
            
                tk.Grid.rowconfigure(self.scrollable_frame,ycol, weight = 1)
                tk.Grid.columnconfigure(self.scrollable_frame,xcol, weight = 1)
                
                if xcol < 2:
                    xcol += 1
                elif xcol == 2:
                    ycol += 1
                    xcol = 0

        if args == 5:
            storagex = {}
            number_of_tiers = 4
            for x in range(11):
                storagex[x] = 0
            yl = []
            z = 0
            for y in all_images_dict.keys():
                yl.append(y)
            for x in yl:
                self.nlabel = tk.Label(self.scrollable_frame, image = all_images_dict[x][0])
                
                for z in range(number_of_tiers):
                    if all_images_dict[x][2] == 0 + z:
                        storagex[z] = storagex[z] + 1
                        xcol = storagex[z] - 1
                        ycol = number_of_tiers - z
                        break
                    elif all_images_dict[x][2] >= number_of_tiers:
                        small = number_of_tiers 
                        storagex[small] = storagex[small] + 1
                        xcol = storagex[small] - 1
                        
                        ycol = 0
                        break
                
                self.nlabel.grid(row = xcol, column= ycol, sticky= 'nsew')
                tk.Grid.rowconfigure(self.scrollable_frame,xcol, weight = 1)
                tk.Grid.columnconfigure(self.scrollable_frame,ycol, weight = 1)

    def onmousewheel(self,event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)),'units')

root = tk.Tk()
root.title("Drafting Game")
root.iconbitmap('c:/Summer_Projects/Images/mage girl 5.jpg')


row_number = 0
column_number = 0

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)

End_image = 'C:\Summer_Projects\End Image\End Screen.jpg'
img2 = Image.open(End_image)
img_2 = img2.resize((610,310))
img_2f = ImageTk.PhotoImage(img_2)
Final_Screen = img_2f

image_nums = []
photo_list = []
photo_folder = 'C:/vn'
for images in os.listdir(photo_folder):
    if(images.endswith('.jpg') or images.endswith('.png')):
        photo_list.append(images)
count3 = 0

for x in photo_list:
    img = (Image.open(photo_folder + '/' + str(x)))
    img_r = img.resize((476,550))
    img_f = ImageTk.PhotoImage(img_r)
    image_nums.append(img_f) 
    all_images_dict[count3] = [img_f,lives,0,0]
    count3 += 1


xrow = 0
yrow = 0
for x in range(number_of_buttons):
    button_option = tk.Button(root, text = 'Option ' + str(x),  command = partial(on_click,1,x))
    label_change = tk.Label(root, image = image_nums[x])
    label_change.grid(row = yrow, column = xrow, sticky = 'nsew')
    button_option.grid(row = yrow+1, column =xrow, sticky = 'nsew')
    if xrow < number_of_buttons -1: 
        xrow += 1
    else:
        xrow = 0
        yrow += 1
    button_list.append(button_option)
    label_list.append(label_change)

button_quit = tk.Button(root, text= "Quit", command= root.quit, bg = 'grey')
button_quit.grid(row = yrow + 2, column = 2 , sticky = 'nsew')

button_choices = tk.Button(root,text = 'Choices', command = lambda:on_click(3,3))
button_choices.grid(row = yrow + 2, column = 0, sticky = 'nsew')

all_button_choices = tk.Button(root,text = 'All Choices', command = lambda:on_click(4,4))
all_button_choices.grid(row = yrow + 2, column = 1, sticky = 'nsew')

ranked_button = tk.Button(root, text = 'Ranked Choices', command= lambda:on_click(5,5))
ranked_button.grid(row = yrow + 3, column = 1, sticky = 'nsew')

ai_button = tk.Button(root, text = 'AI', command= lambda:on_click(2,2))
ai_button.grid(row = yrow + 3, column = 0, sticky = 'nsew')

all_list = [button_list + label_list]
all_list.append(button_quit)
all_list.append(button_choices)
all_list.append(all_button_choices)
all_list.append(ranked_button)
all_list.append(ai_button)

for button in all_list:
    tk.Grid.rowconfigure(root,row_number, weight = 1)
    row_number += 1
    
for button in all_list:
    tk.Grid.columnconfigure(root,column_number, weight = 1)
    column_number += 1

root.geometry('650x650')
root.mainloop()

'''
Need to add a horizontal scrollbar for the top row also need to add image scalling for all the buttons
in the all_list
'''