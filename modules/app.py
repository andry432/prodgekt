import customtkinter
import modules.finding_path as m_path
import PIL

class App(customtkinter.CTk):
    def __init__(self):
        customtkinter.CTk.__init__(self)
        self.APP_WIDTH = 400
        self.APP_HEIGHT = 400

        self.SCREEN_W = self.winfo_screenwidth()  - self.APP_WIDTH
        self.SCREEN_H = self.winfo_screenheight()
        #1
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.SCREEN_W - self.APP_WIDTH}+{0}")
        self.resizable(False, False) 

        self.title("Головний екран додатку")
        self.IMAGE = customtkinter.CTkImage(
            dark_image = PIL.Image.open(m_path.search("img/1.png")), 
            size = (self.APP_WIDTH, self.APP_HEIGHT)
        )

        
        self.IMAGE_LABEL = customtkinter.CTkLabel(master = self, text = "моя первая практичная робота с customtkinter ", image = self.IMAGE)
        self.IMAGE_LABEL.grid(row = 10, column = 10) 


