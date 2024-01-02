import datetime
import sqlite_mod
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
        self.timer_running = False
        self.db = sqlite_mod.local_db()

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.run_timer()

    def run_timer(self):
        if self.timer_running and self.total_sec > 0:
            self.total_sec -= 1
            self.hours, self.secs = divmod(self.total_sec, 3600)
            self.mins, self.secs = divmod(self.secs, 60)
            self.timer['text'] = f'{self.hours:02d}h : {self.mins:02d}m : {self.secs:02d}s'
            self.timer_id = self.after(1000, self.run_timer)
        else:
            self.timer['text'] = '00h : 00m : 00s'
            self.timer_running = False
            self.write_pd()
            self.bell()

    def pause_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.after_cancel(self.timer_id)

    def reset_timer(self):
        if self.timer_running:
            self.pause_timer()
        self.create_timer_buttons()

    def write_pd(self):
        record = [datetime.date.today(), (self.time[0] * 60) + self.time[1]]
        self.db.write_record(record)
        print('record written')
        self.db.close_db()

    def create_timer_buttons(self):
        self.cvs = Canvas(self,
                        width=100,
                        height=175,
                        background='white'
                        )
        self.cvs.grid(row=0, padx=10, pady=10)

        self.total_sec = (self.time[0] * 3600) + (self.time[1] * 60)

        self.timer = Label(self.cvs,
                           text=f'{self.time[0]:02d}h : {self.time[1]:02d}m : 00s',
                           font=('Arial', 12),
                           background='white')
        self.timer.grid(row=0, columnspan=3)

        self.start_button = Button(self.cvs,
                                   text='Start',
                                   command=self.start_timer)
        self.pause_button = Button(self.cvs,
                                   text='Pause',
                                   command=self.pause_timer)
        self.reset_button = Button(self.cvs,
                                   text='Reset',
                                   command=self.reset_timer)
        self.close_button = Button(self.cvs,
                                   text='Close',
                                   command=self.destroy)
        
        self.start_button.grid(row=1, column=0)
        self.pause_button.grid(row=1, column=1)
        self.reset_button.grid(row=1, column=2)
        self.close_button.grid(row=2, column=1)