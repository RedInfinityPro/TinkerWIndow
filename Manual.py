from customtkinter import *
import pyodbc as odbc
def connectSQL():
    DRIVER = 'ODBC Driver 18 for SQL Server'
    SERVER_NAME = 'DANIEL'
    DATABASE_NAME = 'master'
    connection_String = f"""
        DRIVER={DRIVER};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trusted_Connection=yes;
        TrustServerCertificate=yes;
    """
    try:
        conn = odbc.connect(connection_String)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Employees;")
        rows = cursor.fetchall()
        print(rows)
    except Exception as e:
        print("Error:", e)
connectSQL()

title_font = ("Helvetica", 20, "bold")
small_font = ("Helvetica", 10)
small_font_color = ["#2B2B2B", "#E5E5E5"]
basic_font = ("Helvetica", 11)

class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Chart")
        self.geometry("600x600")
        self.configure(fg_color="#1B1B1B")

if __name__ == "__main__":
    app = App()
    app.mainloop()