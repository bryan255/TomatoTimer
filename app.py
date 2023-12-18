from tkinter import *

root = Tk()
root.title('Tomato Timer')
root.geometry('350x350')
root.configure(bg='white')

root.columnconfigure(0, weight=1)

img = PhotoImage(master=root, file=r'C:\Users\bkors\OneDrive\Desktop\Python\Pomodoro\tomato.png')
img1 = img.subsample(3, 3)

Label(root, image=img1).grid(row=0, pady=5)

title_canvas = Canvas(root, height=70, width=350, background='white')
title_canvas.grid(row=1)

title = Label(title_canvas, text='Believe nothing, question everything.', font=('Arial', 14), bg='white')
title.pack(fill=BOTH)

time_select_canvas = Canvas(root, width=100, background='white')
time_select_canvas.grid(row=2, pady=10)

hour_label = Label(time_select_canvas, text='Hours (0-4):', background='white')
min_label = Label(time_select_canvas, text='Minutes (0-59):', background='white')
sec_label = Label(time_select_canvas, text='Seconds (0-59):', background='white')

hour_sp = Spinbox(time_select_canvas, from_=0, to=4, justify=CENTER, width=10)
min_sp = Spinbox(time_select_canvas, from_=0, to=59, justify=CENTER, width=10)
sec_sp = Spinbox(time_select_canvas, from_=0, to=59, justify=CENTER, width=10)

hour_label.grid(row=0, column=0)
min_label.grid(row=1, column=0)
sec_label.grid(row=2, column=0)

hour_sp.grid(row=0, column=1)
min_sp.grid(row=1, column=1)
sec_sp.grid(row=2, column=1)

root.mainloop()