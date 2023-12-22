from tkinter import *
from timer_screen import timer_window

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