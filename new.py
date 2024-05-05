# import re
#
# a = """
# <!DOCTYPE html>
# <html lang="en">
# {% load static %}
# <head>
#     <meta charset="UTF-8">
#     <title>Static Test</title>
#     <link rel="stylesheet" href="{% static 'css/demo.css' %}">
#     <script src="{% static 'js/demo.js' %}"> </script>
# </head>
# <body>
# {% load static %}
# <img src="{% static 'img/img.jpg' %}" alt="Akram" width="400" height="600"><br>
# <h3>Hello welcome to the files</h3>
# <form>
#     <input type="button" onclick="test()" value="Click">
# </form>
# </body>
# </html>
#
#
#
# """
# c = "Hello"
# b = "Hello Everyone in my vlog. Hello to the class."
#
# result = re.finditer('[^<>!%{}"/\n=(),]',a)
# lst = ""
# for i in result:
#     j = i.group()
#     lst += j
# print(lst)
# mresult = re.finditer("\w+\s+",lst)
#
# jst = ""
# for j in mresult:
#     m = j.group()
#     jst += m
# print(jst)
#
# nresult = re.finditer("[^0-9]",jst)
#
# kst = ""
# for k in nresult:
#     o = k.group()
#     kst += o
# print(kst)
#
# # oresult = re.finditer("+html+",kst)
#
# # hst = ""
# # for h in oresult:
# #     h1 = h.group()
# #     hst += h1
# # print(hst)

import ImageTk
import qrcode
from tkinter import *
from PIL import Image
import random
from tkinter import colorchooser
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry("1270x720")
root.title("Qr Code Generator")
global my_color,a
my_color = "black"
canvas = Canvas(root, width=1360,height=750)
canvas.pack()
canvas.configure(background="blue")




my_notebook = ttk.Notebook(root)
my_notebook.place(relx=0.5,rely=0.5,anchor=CENTER)

my_frame1 = Frame(my_notebook,width=900,height=575,bg="lightgrey")
my_frame2 = Frame(my_notebook,width=900,height=575,bg="lightgrey")



my_frame1.pack()
my_frame2.pack()

my_notebook.add(my_frame1,text="Color")
my_notebook.add(my_frame2,text="Submit")



def color():
    global my_color
    my_color = colorchooser.askcolor()[1]



def user1():
    global my_color, a
    if text.get() == "":
        messagebox.showerror("Error","Enter the information to generate QR code")
    else:

        my_notebook.tab(1, state="normal")

        user_input = text.get()

        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
        qr.add_data(user_input)
        qr.make(fit=True)
        img = qr.make_image(fill_color=my_color, back_color="white")
        a = str(random.randint(1000, 99999))
        img.save(a+".png")

        img1 = ImageTk.PhotoImage(Image.open(a+".png"))
        my_imagelabel = Label(my_frame2 ,image=img1)
        my_imagelabel.place(relx=0.5 ,rely=0.5 ,anchor=CENTER)
        my_notebook.select(1)
        text.delete(0, END)
        my_frame1.hide()

my_notebook.tab(1,state="disabled")
head_label = Label(root,text="QR Code Generator",font=("Book Antiqua",25,"bold"),bg="blue",fg="white")
head_label.place(x=2,y=2,width=1360)
lable1 = Label(my_frame1, text="Enter the link to create the QR code",font=("Book Antiqua",20,"bold"),bg="lightgrey")
lable1.place(x=180,y=100)
text = Entry(my_frame1, font=("Book Antiqua",15,"bold"),width=40)
text.place(x=200,y=180)

lable2 = Label(my_frame1, text="Select the color of QR Code",font=("Book Antiqua",15),bg="lightgrey")
lable2.place(x=180,y=260)

button2 = Button(my_frame1, text="Color",font=("Times new roomen",12,),command=color,width=8)
button2.place(x=510,y=260)

button1 = Button(my_frame1, text="Submit",font=("Times new roomen",15,),command=user1,width=12)
button1.place(x=300,y=350)




root.mainloop()