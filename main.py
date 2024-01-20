from cgitb import text
from datetime import datetime, timedelta
from turtle import color, position
import customtkinter
from PIL import Image

def new_year_countdown():
    current_time = datetime.now()
    new_year = datetime(current_time.year + 1, 1, 1, 0, 0, 0)

    current_time = new_year - current_time 
    time_remaining = str(current_time).split('.')[0] # remove seconds from time
    days_remaining = (new_year - current_time).day

    total_days = int(current_time.total_seconds()) # calculate days and time left
    progress_percentage = int((days_remaining / (24 * 60 * 60)) * 100)
    days.configure(text=f"{days_remaining}")
    
    progress.set(value=progress_percentage)
    label.configure(text=f"{time_remaining}") # display the time remaining

    app.after(1000, new_year_countdown) # refresh the process every second

app = customtkinter.CTk() # declare the window, call it what you like, I went with app
app.geometry("350x350") # declare the size
app.title("Year Counter") # declare the title

frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(frame, text="", font=("Arial",16)) # declare a label
label.pack(padx=5, pady=5) # apply it to the window

progress = customtkinter.CTkProgressBar(frame, orientation="horizontal", mode="determinate")
progress.pack()

days = customtkinter.CTkLabel(frame, text="", font=("Arial",154), text_color=("light blue")) # declare a label
days.pack(padx=5, pady=0) # apply it to the window

days_used = customtkinter.CTkLabel(frame, text="Days Used", font=("Arial",14), text_color=("light blue")) # declare a label
days_used.pack(padx=5, pady=5) # apply it to the window

# frame.gif_image = customtkinter.CTkImage(dark_image=Image.open("clock.gif"))

# call the function to see the countdown
new_year_countdown()

app.mainloop()