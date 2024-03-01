import tkinter
from tkinter import *
from PIL import Image, ImageTk
import pymysql
db=pymysql.connect(host='localhost',user='root',password="pooja",database="regform")
cursor=db.cursor()

t = Tk()
t.title("my gui site")
t.geometry("700x700")

l1 = Label(t, text="REGISTRATION FORM", fg="black", font=("Arial Bold", 35))
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

        query_insert = "INSERT INTO screen2 (firstname, lastname, email, gender) VALUES (%s, %s, %s, %s)"
        cursor.execute(query_insert, (firstname, lastname, email, gender))
        db.commit()
        print('User registered successfully')

        # Print the data in the table after insertion
        query_select = "SELECT * FROM screen2"
        cursor.execute(query_select)
        result = cursor.fetchall()
        print("Data in screen2 table:", result)

    except Exception as e:
        db.rollback()
        print(f'Error occurred: {e}')


firstname_label = Label(t, text="FirstName", font=("Arial bold", 15))
firstname_label.place(x=30, y=100)
name_field = Entry(t)
name_field.place(x=150, y=110)

lastname_label = Label(t, text="LastName", font=("Arial bold", 15))
lastname_label.place(x=30, y=150)
lastname_field = Entry(t)
lastname_field.place(x=150, y=160)

email_id_label = Label(t, text="Email id", font=("Arial bold", 15))
email_id_label.place(x=30, y=200)
email_id_field = Entry(t)
email_id_field.place(x=150, y=210)

gender_label = Label(t, text="Gender: ", font=("Arial bold", 15))
gender_label.place(x=30, y=250)
gender_var = StringVar()
male_radio = Radiobutton(t, text="Male", variable=gender_var, value="Male", font=("Arial Bold", 11))
male_radio.place(x=150, y=250)
female_radio = Radiobutton(t, text="Female", variable=gender_var, value="Female", font=("Arial Bold", 11))
female_radio.place(x=210, y=250)

submit_button = Button(t, text="Submit", bg="light blue", font=("Arial bold", 15), command=register)
submit_button.place(x=200, y=330)

t.mainloop()
cursor.close()
db.close()
