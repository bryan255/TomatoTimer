from tkinter import *

class timer_window(Toplevel):

    def __init__(self, parent, hrs, mins):
        super().__init__()
        self.geometry('250x150')
        self.title('Timer')
        self.resizable(False, False)
        self.configure(background='white')
        self.columnconfigure(0, weight=1)
        self.time = [hrs, mins]

    def run_timer(self):
        self.total_sec = (self.time[0] * 3600) + (self.time[1] * 60)
        while self.total_sec > 0:
            self.total_sec -= 1
            self.hours, self.secs = divmod(self.total_sec, 3600)
            self.mins, self.secs = divmod(self.secs, 60)
            self.timer['text'] = f'{self.hours:02d}h : {self.mins:02d}m : {self.secs:02d}s'
            self.total_sec = (self.hours * 3600) + (self.mins * 60) + self.secs
            self.after(1000, self.run_timer)

    def create_timer_buttons(self):

        self.cvs = Canvas(self,
                        width=100,
                        height=175,
                        background='white'
                        )
        self.cvs.grid(row=0, padx=10, pady=10)

        self.timer = Label(self.cvs,
                           text=f'{self.time[0]:02d}h : {self.time[1]:02d}m : 00s',
                           font=('Arial', 12),
                           background='white')
        self.timer.grid(row=0, columnspan=3)


        self.start_button = Button(self.cvs,
                                   text='Start',
                                   command=self.run_timer)
        self.pause_button = Button(self.cvs,
                                   text='Pause')
        self.reset_button = Button(self.cvs,
                                   text='Reset')
        self.close_button = Button(self.cvs,
                                   text='Close',
                                   command=self.destroy)
        
        self.start_button.grid(row=1, column=0)
        self.pause_button.grid(row=1, column=1)
        self.reset_button.grid(row=1, column=2)
        self.close_button.grid(row=2, column=1)

class main_window(Tk):

    def __init__(self, img_path):
        super().__init__()
        self.geometry('350x350')
        self.resizable(False, False)
        self.configure(bg='white')
        self.columnconfigure(0, weight=1)
        self.img = PhotoImage(master=self, file=img_path).subsample(3, 3)

    def tomato_img(self):
        Label(self,
              image=self.img
              ).grid(row=0, pady=5)

    def title(self):
        Label(self,
              text='All or nothing.\nNo in-between.',
              font=('Arial', 14),
              background='white'
              ).grid(row=1)

    def set_timer(self):
        self.timer_label['text'] = f'{int(self.hours_spbx.get()):02d}h : {int(self.mins_spbx.get()):02d}m : 00s'

    def timer_spinboxes(self):

        # canvas for headers & spinboxes
        self.spbx_canvas = Canvas(self,
                                  width=100,
                                  background='white'
                                  )
        self.spbx_canvas.grid(row=2, pady=10)

        # create the headers
        Label(self.spbx_canvas,
              text='Hours\n(0-4):',
              background='white'
              ).grid(row=0, column=0)
        Label(self.spbx_canvas,
              text='Minutes\n(0 - 55):',
              background='white'
              ).grid(row=0, column=1)
        
        # create spinboxes

        self.hrs = IntVar()
        self.mins = IntVar()

        self.hours_spbx = Spinbox(self.spbx_canvas,
                                    from_=0,
                                    to=4,
                                    justify=CENTER,
                                    width=5,
                                    font=('Arial', 14),
                                    textvariable=self.hrs,
                                    command=self.set_timer
                                    )
        self.mins_spbx = Spinbox(self.spbx_canvas,
                                    from_=0,
                                    to=55,
                                    increment=5,
                                    justify=CENTER,
                                    width=5,
                                    font=('Arial', 14),
                                    textvariable=self.mins,
                                    command=self.set_timer
                                    )
        self.hours_spbx.grid(row=1, column=0)
        self.mins_spbx.grid(row=1, column=1)

    def reset_timer(self):

        self.timer_label['text'] = '00h : 00m : 00s'
        self.hrs.set(0)
        self.mins.set(0)

    def call_timer(self):
        self.timer = timer_window(self, int(self.hours_spbx.get()), int(self.mins_spbx.get()))
        self.timer.grab_set()
        self.timer.create_timer_buttons()

    def timer_and_buttons(self):
        
        # canvas for timer and buttons
        self.canvas_timer_and_buttons = Canvas(self,
                                          width=100,
                                          background='white')
        self.canvas_timer_and_buttons.grid(row=3, pady=10)

        # timer label
        self.timer_label = Label(self.canvas_timer_and_buttons,
                                 text='00h : 00m : 00s',
                                 font=('Arial', 14),
                                 background='white')
        self.timer_label.grid(row=0, columnspan=2)

        # ready, reset, and close buttons
        self.ready_button  = Button(self.canvas_timer_and_buttons,
                                    text='Ready',
                                    command=self.call_timer)
        self.reset_button = Button(self.canvas_timer_and_buttons,
                                   text='Reset',
                                   command=self.reset_timer)
        self.close_button = Button(self.canvas_timer_and_buttons,
                                   text='Close',
                                   command=lambda: self.destroy())
        self.ready_button.grid(row=1, column=0, sticky=EW, pady=5)
        self.reset_button.grid(row=1, column=1, sticky=EW, pady=5)
        self.close_button.grid(row=2, columnspan=2)

    def start(self):
        self.tomato_img()
        self.title()
        self.timer_spinboxes()
        self.timer_and_buttons()
        self.mainloop()

if __name__ == '__main__':

    root = main_window(r'C:\Users\bkors\OneDrive - Smithfield Foods, Inc\Desktop\Pomodoro\tomato.png')
    root.start()