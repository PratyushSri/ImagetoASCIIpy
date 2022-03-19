#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
import tkinter as tk
from tkinter import Canvas
from PIL import Image,ImageDraw
import PIL.ImageFont
import os


#requirements pip install numpy, pip install opencv, pip install tkinter, pip install Pillow


# In[2]:


usetkinter = True
Debug= True
while True:
    Filename = input(" Enter Valid Image name: ")
    if os.path.isfile(Filename):
        print("File Found")
        break
    else:
        print("File not found")
        


# In[3]:


#image = Image.open(Filename)
#image


# In[4]:


# extended ascii characters were not working so
#txt = "  .,:;!|#$@░▒▓█"

# created a string with characters that might fit as ascii charcter art
txt = "  _.,*:!|abc#8$@"

txt = txt[::-1]
#didn't want to write backwards so used slicing instead XD


# In[5]:


#only for jupyter notebook
#newm=image.convert('L')
#newm


# In[6]:



#it will return a 2 dimensional array with values ranging 0-255
# Stored in pixels each value represent color as 0 -> black and 255-> white others in middle of gray
pixels = cv2.imread(Filename,cv2.IMREAD_GRAYSCALE)


# using pixels.shape we get row and col lengths, which we can then use to identiy the resolution of image
new_width = pixels.shape[1]
new_height = pixels.shape[0]

# creating a list with list comprehension from asciitext used above
charlist = [x for x in txt]

""" 
#using join function we create a huge string of lenght image's Row x Col
# for every value in the 2d array it can range 0-255 we have 16 characters and now we have to seprate 255/15 = 17 
# to distribute any values to its int as string index. 
# chose 17 as i had 15 characters since a value can be 255 dividing it by 17 we get 15 -> 
# charlist[15] that would raise an out of index error so I added an extra space character to make our ascii string lenght of 16
"""
characters = "".join([charlist[pix//17] for row in pixels for pix in row])


# Here, we use characters[i:i+new_width] to identify slicing from i to the number of col as in width of image
# starting with 0 to total length with increament of total column value, replicating the matrix of pixels.shape but with \n
# this will create the final image.
ascii_image = "\n".join(characters[i:(i+new_width)] for i in range(0,len(characters),new_width))
#ascii_image = map(0,pixels,0,len(charlist)-1)

if Debug:
    print("Pixels value of image : ",pixels)
    print("Dimension of Image: ",pixels.shape)
    print("Ascii text to be used: ",txt)
    print("Total number of ascii characters: ",len(charlist))
    print("Total number of ascii text pasted on Image: ",len(characters))
    print("Length of final String: ",len(ascii_image))


    # creating a text file to display the Art.
with open("Imageas_ASCII.txt","w") as f:
    f.write(ascii_image)


# In[7]:


if usetkinter:
    window  = tk.Tk()

    window.title("TESTING TKINTER")
    w = Canvas(window,width = new_width,height=new_height*2,bg='white')
    w.create_text(0,0,text=ascii_image,anchor="nw",fill="red",font = ('roboto 1 bold'))

    w.pack()


    window.mainloop()



# In[ ]:





# In[ ]:





# In[ ]:




