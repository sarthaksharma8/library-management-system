#Importing Modules
from http.client import TEMPORARY_REDIRECT
from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *

#Mysql Connectivity
pass1 = ""
database1="library"
con = pymysql.connect(host="localhost",user="root",password=pass1,database=database1)
cur = con.cursor()

#Creating Tables
try:
    cur.execute("CREATE TABLE books (bid VARCHAR(60), title VARCHAR(60), author VARCHAR(60), status VARCHAR(60))")
    con.commit()
except Exception as e:
    pass
try:
    cur.execute("CREATE TABLE books_issued (bid VARCHAR(60),  issuedto VARCHAR(60))")
    con.commit()
except:
    pass

#Display Adjustments
root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")

#Display  background Adjustments
same=True
n=1.0
background_image =Image.open("libraryimportant.jpeg")
[imageSizeWidth, imageSizeHeight] = background_image.size
newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

#Frame Background Adjusting
Canvas1 = Canvas(root)
Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

#Frame Colour Adjusting
headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

#Frame Title Adjusting
headingLabel = Label(headingFrame1, text="Welcome to \n Madhav's Library System", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)   

#Option 1: Add Book Button
btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

#Option 2: Delete Book Button
btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

#Option 3: View Book List Button
btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

#Option 4:Issue Book Button
btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueBook)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

#Option 5: Return Book Button
btn5 = Button(root,text="Return Book",bg='black', fg='white', command = returnBook)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop()
