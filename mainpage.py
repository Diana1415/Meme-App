"""This is the main page program."""

from tkinter import *
from customtkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk


set_appearance_mode("dark")


class MemeApp:
	"""This class contains general methods of user interface."""

	def __init__(self, window):
		self.window = window  # Creating a window
		self.window.title("Meme Generator")  # Assigning a title
		self.window.geometry('500x400')

		self.meme_text = StringVar()  # variable fot the meme text
		self.image_path = None  # variable for image path
		self.image_label = None  # image label

		self.create_widgets()  # create widgets

	def create_widgets(self):

    	# Размечаем 3 колонки: пустая, центр, пустая (для выравнивания)
		self.window.columnconfigure(0, weight=1)  # Левая колонка
		self.window.columnconfigure(1, weight=1)  # Левая колонка
		self.window.columnconfigure(2, weight=1)  # Центральная колонка (основная)
		self.window.columnconfigure(3, weight=1)  # Правая колонка

    	# Поле ввода текста (занимает две колонки)
		self.entry_box = CTkEntry(self.window, 
                              placeholder_text="Enter meme text",
                              height=30,
                              width=400,
                              font=("Helvetica", 18))
		self.entry_box.grid(row=0, column=1, columnspan=2, pady=10, sticky="nsew")  

    	# Кнопки Submit и Clear (размещены в одной строке)
		btn1 = CTkButton(self.window, text="Submit", command=self.submit)
		btn1.grid(row=1, column=1, pady=5, padx=10, sticky="e")  

		btn2 = CTkButton(self.window, text="Clear", command=self.clear)
		btn2.grid(row=1, column=2, pady=5, padx=10, sticky="w")  

    	# Кнопка Upload (по центру)
		btn3 = CTkButton(self.window, text="Upload", command=self.upload_image)
		btn3.grid(row=2, column=1, columnspan=2, pady=10, sticky="n")

		# Метка для изображения
		self.lableframe = LabelFrame(self.window, background='blue')
		self.lableframe.grid(row=3, column=1, columnspan=2, pady=10, sticky="nsew")
		self.image_label = CTkLabel(self.lableframe, text="No Image")
		self.image_label.grid(row=3, column=1, columnspan=2)  # Пятая строка

		# Button create meme
		btn4 = CTkButton(self.window, text="Create Meme", command=self.create_meme)
		btn4.grid(row=4, column=1, columnspan=2, pady=10, sticky="n")


	def submit(self):
		"""Handles submit action."""
		self.entry_box.configure(state="disabled")
		meme_text = self.entry_box.get()
		return meme_text

	def clear(self):
		"""Clears the entry box."""
		self.entry_box.configure(state="normal")
		self.entry_box.delete(0, END)

	def upload_image(self):
		"""Uploads an image and displays it."""
		self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
		if self.image_path:
			image = Image.open(self.image_path)
			image.thumbnail((400, 400))
			photo = ImageTk.PhotoImage(image)
			self.image_label.configure(image=photo, text = '')
			self.image_label.image = photo  # Keep reference
			print(self.image_path)
		return self.image_path

	def create_meme(self):
		pass


if __name__ == "__main__":
	window = CTk()
	app = MemeApp(window)
	window.mainloop()