import tkinter as H


HEIGHT = 420
WIDTH = 560

main_window = H.Tk()
main_window.title("Hidato")

canvas = H.Canvas(main_window, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = H.Frame(main_window, bg='blue', bd=5)
frame.place(relx=0.5, rely=0.03, relwidth=0.75, relheight=0.1, anchor='n')

label = H.Label(frame, font= 20, text="Enter Game size", bg='yellow', fg='red')
label.place(relx = 0.02, relwidth=0.33, relheight=1)

entry = H.Spinbox(frame, from_ = 2, to = 10, font= 90) 
entry.place(relx = 0.4, relwidth=0.1, relheight=1)

entry = H.Spinbox(frame,from_ = 2, to = 10, font= 90)
entry.place(relx = 0.55, relwidth=0.1, relheight=1)

button = H.Button(frame, text="Click to Begin", bg = 'yellow', fg = 'red', font=20)
button.place(relx=0.7, relwidth=0.28, relheight=1)

middle_frame = H.Canvas(main_window, bg='blue', bd=5)
middle_frame.place(relx=0.5, rely=0.16, relwidth=0.75, relheight=0.69, anchor='n')
cell = [([0]*6) for i in range(6)]               # create array for 81 individual cells
        for i in range(6):
            for j in range(6):
                # create and activate the 81 cells (9 rows of 9 cells).
                # The cells are Entry widgets which allow text input.
                cell[i][j] = Entry(middle_frame, width = 1, fg='black')
                cell[i][j].grid(row=i,column=j,)

buttom_frame = H.Frame(main_window, bg='blue', bd=5)
buttom_frame.place(relx=0.5, rely=0.88, relwidth=0.75, relheight=0.1, anchor='n')

button = H.Button(buttom_frame, text="Reset", bg = 'yellow', fg = 'red', font=20)
button.place(relx=0.35, relwidth=0.3, relheight=1)

main_window.mainloop()
