"""This is the login page program."""

from tkinter import *
from customtkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk


set_appearance_mode("dark")


class LoginApp:
	"""This class contains general methods of user interface."""

	def __init__(self, window):
		self.window = window  # Creating a window
		self.window.title("Meme Generator")  # Assigning a title
		self.window.geometry('500x400')

		self.username = StringVar()  # variable fot the username
		self.password = StringVar()  # variable fot the password
		

		self.create_widgets()  # create widgets

	def create_widgets(self):

    	# Размечаем 3 колонки: пустая, центр, пустая (для выравнивания)
		self.window.columnconfigure(0, weight=1)  # Левая колонка
		self.window.columnconfigure(1, weight=1)  # Левая колонка
		self.window.columnconfigure(2, weight=1)  # Центральная колонка (основная)
		self.window.columnconfigure(3, weight=1)  # Правая колонка

    	# Поле ввода текста (занимает две колонки)
		self.entry_box_username = CTkEntry(self.window, 
                              placeholder_text="Enter Username",
                              height=30,
                              width=400,
                              font=("Helvetica", 18))
		self.entry_box_username.grid(row=0, column=1, columnspan=2, pady=10, sticky="nsew")
		# Поле ввода текста (занимает две колонки)
		self.entry_box_password = CTkEntry(self.window, 
                              placeholder_text="Enter Password",
                              height=30,
                              width=400,
                              font=("Helvetica", 18))
		self.entry_box_password.grid(row=1, column=1, columnspan=2, pady=10, sticky="nsew") 

    	# Кнопки Submit и Clear (размещены в одной строке)
		btn1 = CTkButton(self.window, text="Create Account")
		btn1.grid(row=2, column=1, pady=5, padx=10, sticky="e")  

		btn2 = CTkButton(self.window, text="Log In", command=self.submit)
		btn2.grid(row=2, column=2, pady=5, padx=10, sticky="w")  

	def submit(self):
		"""Handles submit action."""
		self.entry_box_username.configure(state="disabled")
		self.entry_box_password.configure(state="disabled")
		username = self.entry_box_username.get()
		password = self.entry_box_password.get()
		return username, password


if __name__ == "__main__":
	window = CTk()
	app = LoginApp(window)
	window.mainloop()