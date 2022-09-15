# Importing the modules
import tkinter as tk
import tkinter.font as font
import datetime
import winsound as ws


# creating a countdown class
class Countdown(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.show_widgets()
        self.seconds_left = 0
        self._timer_on=False

    def show_widgets(self):
        self.label.pack()
        self.entry.pack()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()

    def create_widgets(self):
        self.myFont = font.Font(family='Lato', size=15)
        self.label=tk.Label(self, text="Enter the time in seconds.", font=self.myFont)
        self.entry=tk.Entry(self, justify="center", font=self.myFont)
        self.entry.focus_set()
        self.reset=tk.Button(self, text="Reset Timer", command=self.reset_button, padx=20, pady=15, font=self.myFont)
        self.stop=tk.Button(self, text="Stop Timer", command=self.stop_button, padx=20, pady=15, font=self.myFont)
        self.start=tk.Button(self, text="Start Timer", command=self.start_button, padx=20, pady=15, font=self.myFont)

    def countdown(self):
        self.label["text"]=self.convert_seconds_left_to_time()

        if self.seconds_left:
            self.seconds_left-=1
            self._timer_on=self.after(1000, self.countdown)
        else:
            self._timer_on = False
            ws.PlaySound("Alarm Clock Sound", ws.SND_FILENAME)
    
    def reset_button(self):
        self.seconds_left=0
        self.stop_timer()
        self._timer_on=False
        self.label["text"]="Enter the time in seconds."
        self.start.forget()
        self.stop.forget()
        self.reset.forget()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()

    def stop_button(self):
        self.second_left=int(self.entry.get())
        self.stop_timer()

    def start_button(self):
        self.seconds_left=int(self.entry.get())
        self.stop_timer()
        self.countdown()
        self.start.forget()
        self.stop.forget()
        self.reset.forget()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()

    def stop_timer(self):
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on=False

    def convert_seconds_left_to_time(self):
        return datetime.timedelta(seconds=self.seconds_left)

# Main loop
if __name__=="__main__":
        root=tk.Tk()
        root.resizable(False, False)
        root.geometry("300x300")
        root.title("Alarm timer")

        countdown=Countdown(root)
        countdown.pack()
       
        root.mainloop()
