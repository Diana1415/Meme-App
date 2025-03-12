from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont

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


class LoginFrame(CTkFrame):
    """Log In Page."""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configure grid to expand
        self.pack(fill="both", expand=True)

        # Title
        self.title1 = CTkLabel(self, text="Log In", font=("Arial", 24, "bold"))
        self.title1.pack(pady=10)

        # Username Entry
        self.username_entry = CTkEntry(self, placeholder_text="Username")
        self.username_entry.pack(pady=5)

        # Password Entry
        self.password_entry = CTkEntry(self, show="*", placeholder_text="Password")
        self.password_entry.pack(pady=5)

        # Submit Button
        CTkButton(self, text="Log In", command=self.login).pack(pady=10)

        # Back Button
        CTkButton(self, text="Back", command=lambda: controller.show_frame(WelcomeFrame)).pack(pady=5)
        
        # Create Account Button
        CTkButton(self, text="Create account", command=lambda: controller.show_frame(CreateAccountFrame)).pack(pady=5)

        # Forgot password Button
        CTkButton(self, text="Forgot password?", command=lambda: controller.show_frame(ForgotPassFrame)).pack(pady=5)

    def login(self):
        """Login Check."""
        username = self.username_entry.get()
        password = self.password_entry.get()
        print("Login successful!")
        self.controller.show_frame(MainPageFrame)


class ForgotPassFrame(CTkFrame):
    """Forgot my password page."""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configure grid to expand
        self.pack(fill="both", expand=True)

        # Title
        CTkLabel(self, text="Forgot Password?", font=("Arial", 24, "bold")).pack(pady=10)

        # Username Entry
        self.username_entry = CTkEntry(self, placeholder_text="Type Email")
        self.username_entry.pack(pady=5)

        # Submit Button
        CTkButton(self, text="Password Update", command=self.reset_password).pack(pady=10)

        # Back Button
        CTkButton(self, text="Back", command=lambda: controller.show_frame(LoginFrame)).pack(pady=5)

    def reset_password():
        pass
    

class CreateAccountFrame(CTkFrame):
    """Create Account Page."""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configure grid to expand
        self.pack(fill="both", expand=True)

        # Title
        CTkLabel(self, text="Create Account", font=("Arial", 24, "bold")).pack(pady=10)

        # Username Entry
        self.username_entry = CTkEntry(self, placeholder_text="Username")
        self.username_entry.pack(pady=5)

        # Password Entry
        self.password_entry = CTkEntry(self, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=5)

        # Password confirmation
        self.password_confentry = CTkEntry(self, placeholder_text="Confirm Password", show="*")
        self.password_confentry.pack(pady=5)

        # Submit Button
        CTkButton(self, text="Create account", command=self.create_account).pack(pady=10)

        # Back Button
        CTkButton(self, text="Back", command=lambda: controller.show_frame(LoginFrame)).pack(pady=5)
    
    def create_account(self):
        pass


class MainPageFrame(CTkFrame):
    """This is the page with a choice."""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configure grid to expand
        self.pack(fill="both", expand=True)

        # Generate meme Button
        CTkButton(self, text="Generate Meme", command=lambda: controller.show_frame(GenerateMemeFrame)).pack(pady=10)

        # Create meme Button
        CTkButton(self, text="Create Meme", command=lambda: controller.show_frame(CreateMemeFrame)).pack(pady=5)


class GenerateMemeFrame(CTkFrame):
    """"""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configure grid to expand
        self.pack(fill="both", expand=True)
        
        #Back Button
        CTkButton(self, text="Back", command=lambda: controller.show_frame(MainPageFrame)).pack(pady=5)


class CreateMemeFrame(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.pack(fill="both", expand=True)

        self.image_path = None
        self.img = None
        self.tk_img = None

        # Текст и его начальные координаты
        self.text_var = StringVar()
        self.text_x, self.text_y = 250, 350
        self.text_id = None  # ID текста на canvas
        self.drag_data = {"x": 0, "y": 0}

        # Поле ввода текста
        self.text_entry = CTkEntry(self, textvariable=self.text_var, width=300, placeholder_text="Enter text...", text_color='black')
        self.text_entry.pack(pady=10)

        # Кнопка загрузки изображения
        self.load_button = CTkButton(self, text="Upload Image", command=self.load_image)
        self.load_button.pack(pady=10)

        # Canvas для отображения изображения
        self.canvas = Canvas(self, width=500, height=400, bg="white")
        self.canvas.pack()

        # Кнопка создания мема
        self.create_button = CTkButton(self, text="Create Meme", command=self.generate_meme)
        self.create_button.pack(pady=10)

        # Кнопка сохранения
        self.save_button = CTkButton(self, text="Save Meme", command=self.save_meme, state=DISABLED)
        self.save_button.pack(pady=10)

        # Привязываем обработчики мыши для перемещения текста
        self.canvas.bind("<ButtonPress-1>", self.on_text_press)
        self.canvas.bind("<B1-Motion>", self.on_text_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_text_release)

    def load_image(self):
        """Загружает и отображает изображение."""
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if not file_path:
            return  

        self.img = Image.open(file_path).resize((500, 400), Image.Resampling.LANCZOS)
        self.tk_img = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(0, 0, anchor=NW, image=self.tk_img)

    def generate_meme(self):
        """Добавляет текст на изображение."""
        if not self.img:
            return

        text = self.text_var.get()
        if not text:
            return

        # Если текст уже есть на canvas — удаляем его
        if self.text_id:
            self.canvas.delete(self.text_id)

        # Отображаем текст как объект canvas
        self.text_id = self.canvas.create_text(
            self.text_x, self.text_y, text=text, font=("Lobster", 20), fill="white")

        self.save_button.configure(state=NORMAL)  

    def save_meme(self):
        """Сохраняет изображение с текстом."""
        if not self.img:
            return

        img_with_text = self.img.copy()
        draw = ImageDraw.Draw(img_with_text)

        try:
            font = ImageFont.truetype("arial.ttf", 30)
        except IOError:
            font = ImageFont.load_default()

        text = self.text_var.get()
        draw.text((self.text_x, self.text_y), text, font=font, fill="white")

        save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
        if save_path:
            img_with_text.save(save_path)

    def on_text_press(self, event):
        """Фиксирует начальные координаты текста при клике."""
        if self.text_id and self.canvas.find_withtag("current"):
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y

    def on_text_drag(self, event):
        """Перемещает текст при движении мыши."""
        dx = event.x - self.drag_data["x"]
        dy = event.y - self.drag_data["y"]
        self.canvas.move(self.text_id, dx, dy)
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def on_text_release(self, event):
        """Сохраняет новые координаты текста."""
        if self.text_id:
            self.text_x, self.text_y = self.canvas.coords(self.text_id)
