from calendar import calendar
from cgitb import text
from datetime import datetime, timedelta
import customtkinter as ctk
import tkinter as tk

def new_year_countdown():
    current_time = datetime.now()
    new_year = datetime(current_time.year + 1, 1, 1, 0, 0, 0)

    current_time = new_year - current_time 
    time_remaining = str(current_time).split('.')[0] # remove seconds from time
    days_remaining = (new_year - current_time).day

    progress_percentage = int((days_remaining / (24 * 60 * 60)) * 100)
    days.configure(text=f"{days_remaining}")
    
    progress.set(value=progress_percentage)
    label.configure(text=f"{time_remaining}") # display the time remaining

    app.after(1000, new_year_countdown) # refresh the process every second

def resize_font(app, event):
    new_font_size = max(int(event.width / 30), 10)
    app.days['font'] = ("Arial", new_font_size)

def create_window():
    new_window = ctk.CTkToplevel()
    new_window.title('Tasks')
    new_window.geometry('300x300')
    ctk.CTkLabel(new_window, text='Set deadlines').pack()
    # calendar(new_window, selectmode='day',
    #                year = 2024,
    #                month=1,
    #                day=22).pack()
    new_window.pack()

app = ctk.CTk() # declare the window, call it what you like, I went with app
app.geometry("350x350") # declare the size
app.title("Year Counter") # declare the title

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(frame, text="", font=("Arial",16)) # declare a label
label.pack() # apply it to the window

days = ctk.CTkLabel(frame, text="", font=("Arial",154), text_color=("light blue")) # declare a label
days.pack()
# days.pack(expand=True, fill=customtkinter.BOTH)

days_used = ctk.CTkLabel(frame, text="Days Used", font=("Arial",14), text_color=("light blue")) # declare a label
days_used.pack() # apply it to the window

progress = ctk.CTkProgressBar(frame, orientation="horizontal", mode="determinate")
progress.pack()

add_task = ctk.CTkButton(frame, text="Add Task", command=create_window)
add_task.pack(expand=True)

new_year_countdown() # call the function to see the countdown

app.mainloop()