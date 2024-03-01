import sqlite3
db = sqlite3.connect('regform.db')
cursor = db.cursor()

"""import pymysql
db=pymysql.connect(host="localhost",user="root",password="pooja",database="regform")
cursor=db.cursor()"""

import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import Tk, Label
t=tkinter.Tk()
t.title("my gui site")
t.geometry("700x700")
l1=tkinter.Label(t,text="REGISTRATION FORM",fg="black",font=("Arial Bold",35))
l1.pack()
backgroundImage = ImageTk.PhotoImage(Image.open("C:/Users/new/Pictures/circles-highlights-background-form-wallpaper-preview.jpg"))
bgLabel = Label(t, image=backgroundImage)
bgLabel.pack()

def register():
    try:
        firstname = name_field.get()
        lastname = lastname_field.get()
        email = email_id_field.get()
        gender = gender_var.get()
        print(firstname)
    
        query = "INSERT INTO screen2 (firstname,lastname,email, gender) VALUES (%S, %s, %s, %s)"
    
        cursor.execute(query, (firstname,lastname,email, gender))
        db.commit()
        print('User registered successfully')
    except:
        db.rollback()
        print('Error occurred')




firstname_label = Label(t, text="FirstName",font=("Arial bold",15))
firstname_label.place(x=30, y=100)
name_field = Entry(t)
name_field.place(x=150, y=110)
lastname_label = Label(t, text="LastName",font=("Arial bold",15))
lastname_label.place(x=30, y=150)
lastname_field = Entry(t)
lastname_field.place(x=150, y=160)

email_id_label = Label(t, text="Email id",font=("Arial bold",15))
email_id_label.place(x=30, y=200)
email_id_field = Entry(t)
email_id_field.place(x=150, y=210)

gender_label = Label(t, text="Gender: ",font=("Arial bold",15))
gender_label.place(x=30,y=250)
gender_var = StringVar()
male_radio = Radiobutton(t, text="Male", variable=gender_var, value="Male",font=("Arial Bold",11))
male_radio.place(x=150,y=250)
female_radio = Radiobutton(t, text="Female", variable=gender_var, value="Female",font=("Arial Bold",11))
female_radio.place(x=210,y=250)

submit_button = Button(t, text="Submit", bg="light blue", font=("Arial bold",15),command=lambda:print("Form submitted successfully!"))
submit_button.place(x=200, y=330)




t.mainloop()
cursor.close()
db.close()

