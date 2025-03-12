from tkinter import *
from customtkinter import *
from AllFrames import LoginFrame

class WelcomeFrame(CTkFrame):
    """First page (Welcome Page)."""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configure grid to expand
        self.pack(fill="both", expand=True, anchor=CENTER)

        self.label1 = CTkLabel(self, text="Welcome to Meme Generator!", corner_radius=32)
        self.label1.pack(expand=True, anchor=CENTER)
        self.btn1 = CTkButton(self, text="Next", command=lambda: controller.show_frame(LoginFrame))
        self.btn1.pack(pady=10)