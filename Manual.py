from customtkinter import *

title_font = ("Helvetica", 20, "bold")
small_font = ("Helvetica", 10)
small_font_color = ["#2B2B2B", "#E5E5E5"]
basic_font = ("Helvetica", 11)

class TopDisplay(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.appTitle = CTkLabel(self, text="Welcome",font=title_font).pack(side="top", fill=X, padx=10, pady=10)
        self.search = CTkEntry(self, placeholder_text="Search...", font=basic_font).pack(fill=X, padx=10, pady=10)
        
        self.buttonFrame = CTkFrame(self, height=50, width=100, border_width=1)
        self.buttonFrame.pack(side="bottom", fill=X, padx=10, pady=10)

        self.animalBTN = CTkButton(self.buttonFrame, text="Animals", font=small_font)
        self.animalBTN.pack(side="left", padx=10, pady=10)

        self.addBTN = CTkButton(self.buttonFrame, text="Add", font=small_font)
        self.addBTN.pack(side="left", padx=10, pady=10)

        self.plantBTN = CTkButton(self.buttonFrame, text="Plants", font=small_font)
        self.plantBTN.pack(side="left", padx=10, pady=10)

class BodyDisplay(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.list = ["Domain","Kingdom","Phylum","Class","Order","Family","Genus","Species"]
        self.addList = ["Eukarya", "Animalia"]
        for x, item in enumerate(self.list):
            self.side_buttonFrame = CTkFrame(self, border_width=1)
            self.side_buttonFrame.pack(side="left", fill=Y, padx=10, pady=10)
            self.side_Title = CTkLabel(self.side_buttonFrame, text=item.capitalize(),font=title_font).pack(side="top", fill=X, padx=10, pady=10)

            for i, animal in enumerate(self.addList):
                self.animal_button = CTkButton(self.side_buttonFrame, text=animal).pack(side="top", fill=X, padx=10, pady=10)

class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Chart")
        self.geometry("600x600")
        self.configure(fg_color="#1B1B1B")
        self.topDisplay = TopDisplay(self, border_width=2).pack(side="top", fill=X, padx=10, pady=10)
        self.bodyDisplay = BodyDisplay(self, border_width=2).pack(side="top", fill=BOTH, padx=10, pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()