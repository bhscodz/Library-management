import tkinter as tk
import mysql.connector as conn

root= tk.Tk()

book_action='return a book'

return_2=False

canvas1 = tk.Canvas(root, width=600, height=400, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Isuue a book')
label1.config(font=('helvetica', 20,'bold'))
canvas1.create_window(300, 25, window=label1)

label2 = tk.Label(root, text='Enter the details:')
label2.config(font=('helvetica', 15))
canvas1.create_window(300, 65, window=label2)

label0 = tk.Label(root, text='enter book code')
label0.config(font=('helvetica', 10))
canvas1.create_window(100, 120, window=label0)

label4 = tk.Label(root, text='enter the name of isuer:')
label4.config(font=('helvetica', 10))
canvas1.create_window(100, 280, window=label4)

label5 = tk.Label(root, text='enter the address of isuer:')
label5.config(font=('helvetica', 10))
canvas1.create_window(300, 120, window=label5)

label6 = tk.Label(root, text='enter the phone_no of isuer:')
label6.config(font=('helvetica', 10))
canvas1.create_window(300, 280, window=label6)

label7 = tk.Label(root, text='enter the date of issue:')
label7.config(font=('helvetica', 10))
canvas1.create_window(500, 120, window=label7)

label8 = tk.Label(root, text='enter the duration:')
label8.config(font=('helvetica', 10))
canvas1.create_window(500, 280, window=label8)

entry1 = tk.Entry(root) 
canvas1.create_window(100, 140, window=entry1)

entry2 = tk.Entry(root) 
canvas1.create_window(100, 300, window=entry2)

entry3 = tk.Entry(root) 
canvas1.create_window(300, 140, window=entry3)

entry4 = tk.Entry(root) 
canvas1.create_window(300, 300, window=entry4)

entry5 = tk.Entry(root) 
canvas1.create_window(500, 140, window=entry5)

entry6 = tk.Entry(root) 
canvas1.create_window(500, 300, window=entry6)


def get_square_root():
    x1 = entry1.get()
    # condition to check availability of book
    if True:
        message = str(x1)+' is available'
    label3 = tk.Label(root, text=message, font=('helvetica', 10, 'bold'))
    canvas1.create_window(100, 210, window=label3)
def return1():
    global return_2
    global canvas2
    
    if not return_2:
        
        canvas2 = tk.Canvas(root, width=600, height=200, relief='raised')
        canvas2.pack()
        
        return_2=True
        
        label11 = tk.Label(root, text='Return a book')
        label11.config(font=('helvetica', 20,'bold'))
        canvas2.create_window(300, 10, window=label11)

        label12 = tk.Label(root, text='enter book code')
        label12.config(font=('helvetica', 10,'bold'))
        canvas2.create_window(300, 50, window=label12)

        entry11 = tk.Entry(root) 
        canvas2.create_window(300, 80, window=entry11)

        button4 = tk.Button(text='search', command=search, bg='green', fg='black', font=('helvetica', 9, 'bold'))
        canvas2.create_window(400, 80, window=button4)

        button5 = tk.Button(text='return', command=return_book, bg='green', fg='black', font=('helvetica', 9, 'bold'))
        canvas2.create_window(275, 180, window=button5)

        button3 = tk.Button(text='done', command=goback, bg='green', fg='black', font=('helvetica', 9, 'bold'))
        canvas2.create_window(325, 180, window=button3)
    else:
        pass

def goback():
    global return_2
    return_2=False
    canvas2.destroy()
    
def search():
    label13 = tk.Label(root, text='Return a book')
    label13.config(font=('helvetica', 10,'bold'))
    canvas2.create_window(100, 110, window=label13)

    label14 = tk.Label(root, text='enter book code')
    label14.config(font=('helvetica', 10,'bold'))
    canvas2.create_window(100, 150, window=label14)

    label15 = tk.Label(root, text='Return a book')
    label15.config(font=('helvetica', 10,'bold'))
    canvas2.create_window(300, 110, window=label15)

    label16 = tk.Label(root, text='enter book code')
    label16.config(font=('helvetica', 10,'bold'))
    canvas2.create_window(300, 150, window=label16)

    label17 = tk.Label(root, text='Return a book')
    label17.config(font=('helvetica', 10,'bold'))
    canvas2.create_window(500, 110, window=label17)

    label18 = tk.Label(root, text='enter book code')
    label18.config(font=('helvetica', 10,'bold'))
    canvas2.create_window(500, 150, window=label18)
    pass
    

def return_book():
    pass


button1 = tk.Button(text='get the book status', command=get_square_root, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(100, 180, window=button1)

button2 = tk.Button(text=book_action, command=return1, bg='green', fg='black', font=('helvetica', 9, 'bold'))
canvas1.create_window(100, 25, window=button2)

root.mainloop()