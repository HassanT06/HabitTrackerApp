import tkinter as tk;

#create main window
#Excessive code comments to help remind me of concepts

root = tk.Tk() 
root.title("Habit Tracker") #App name
root.geometry("500x400") #Window Dimensions(x,y)
root.configure(bg="coral") #Background colour change [#wNOTE: does not affect text label's background colour]
                            #Hexcodes can also be used

Header = tk.Label(root, text="Welcome to THE Habit Tracker", font=("Roboto",16,"bold"), bg="cyan",fg="black") #Text inside window
Header.pack(pady=10) #Pads the text away from borders

root.mainloop()