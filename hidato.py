from tkinter import *
from os import system
#from PIL import Image

HEIGHT = 450
WIDTH = 600
n=0

def resetter(spinbox1, spinbox2):
    n= spinbox1
    m= spinbox2
    if (n<=2|n>=10|n=='*'|m<=2|m>=10|m=='*'):
        photo = PhotoImage(file="hidato.gif")
        label = Label(middle_frame, image=photo, bg = 'red')
        label.place(relwidth=1, relheight=1)
    else:
        cell = [([0]*m) for i in range(n)]               # create array for m*n individual cells
        for i in range(n):
            for j in range(m):
                cell[i][j] = Entry(middle_frame, bd = 1, fg='black', bg ='pink', font = 40 , justify ='center')
                cell[i][j].place(relx=i/n, rely=j/m, relwidth=1/n, relheight=1/m)


main_window = Tk()
main_window.title("Hidato")

canvas = Canvas(main_window, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = Frame(main_window, bg='blue', bd=5)
frame.place(relx=0.5, rely=0.03, relwidth=0.75, relheight=0.1, anchor='n')

label = Label(frame, font= 20, text="Enter Game size", bg='yellow', fg='red')
label.place(relx = 0.02, relwidth=0.33, relheight=1)

spinbox1 = Entry(frame,  bd = 1, fg='black', bg ='pink', font = 40 , justify ='center') 
spinbox1.place(relx = 0.4, relwidth=0.1, relheight=1)


spinbox2 = Entry(frame, bd = 1, fg='black', bg ='pink', font = 40 , justify ='center')
spinbox2.place(relx = 0.55, relwidth=0.1, relheight=1)


button = Button(frame, text="Click to Begin", bg = 'yellow', fg = 'red', font=20, command = lambda:resetter(int(spinbox1.get()),int(spinbox2.get())))
button.place(relx=0.7, relwidth=0.28, relheight=1)

middle_frame = Frame(main_window, bg='blue', bd=5)
middle_frame.place(relx=0.5, rely=0.16, relwidth=0.75, relheight=0.69, anchor='n')
photo = PhotoImage(file="hidato.gif")
label = Label(middle_frame, image=photo, bg = 'red')
label.place(relwidth=1, relheight=1)


buttom_frame = Frame(main_window, bg='blue', bd=5)
buttom_frame.place(relx=0.5, rely=0.88, relwidth=0.75, relheight=0.1, anchor='n')

button = Button(buttom_frame, text="Reset", bg = 'yellow', fg = 'red', font=20)
button.place(relx=0.1, relwidth=0.3, relheight=1)

button = Button(buttom_frame, text="Possible Solution", bg = 'yellow', fg = 'red', font=20)
button.place(relx=0.5, relwidth=0.4, relheight=1)


main_window.mainloop()



