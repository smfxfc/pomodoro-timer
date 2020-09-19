#! python3

import tkinter as tk
from tkinter import messagebox

def pomodoro_popup(message):
	window = tk.Tk()

	window.title("The pomodoro round timer is up.")
	window.geometry('700x400') # adjust depending on monitor

	def clicked(event=None):
		window.destroy()
	window.bind('<Return>', clicked) # Enable the enter key to close the message box

	btn = tk.Button(window, text=message, command=clicked)
	btn.pack()
	btn.grid(column=0, row=0)
	# this might be redundant, but enabling enter key to close message box via button
	btn.bind('<Return>', clicked) 

	window.mainloop() # this is the line that actually opens the popup box