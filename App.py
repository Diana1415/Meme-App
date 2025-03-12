from customtkinter import *
from frames.AllFrames import *

class App(CTk):
    """Main app handling all switch pages."""

    def __init__(self):
        """This functions initializes app attributes and show_frame method."""
        super().__init__()  # Inheritance of ... Наследование функций супер класса
        self.title("Meme Generator")  # Displayed title of an app
        self.geometry('400x400')

        # Container for page storage
        self.container = CTkFrame(self)  # This container will save link to a parent frame 
        self.container.pack(fill="both", expand=True)  # location maintenance

        self.frames = {}  # Dictionary for storage of all pages

        # Creation and addition of all pages
        for F in (WelcomeFrame, LoginFrame, CreateAccountFrame, MainPageFrame, GenerateMemeFrame, CreateMemeFrame, ForgotPassFrame):
            frame = F(self.container, self)  # Initialization of other frames
            self.frames[F] = frame 
            frame.pack(fill="both", expand=True)

        self.show_frame(WelcomeFrame)  # Show Welcome page

    def show_frame(self, page_class):
        """Switch method between pages.
        Input: frame (page) class
        Output: "opened" frame."""

        # First remove all other frames
        for frame in self.frames.values():
            frame.pack_forget()

        # Show the selected frame
        frame = self.frames[page_class]
        frame.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()