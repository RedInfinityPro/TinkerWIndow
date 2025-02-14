# Project

The code creates a simple GUI application using Tkinter, a Python toolkit. It defines functions and classes for creating windows and components. The MenuBox function creates a title frame and buttons frame. The clear_window function clears all widgets. The MenuWindow function creates a menu box with a title. However, an error occurs in the function.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Imports](#Imports)
- [Rating: 6/10](#Rating)

# About

The code demonstrates the creation of a simple GUI application using Tkinter, a standard Python GUI toolkit. It defines several functions and classes to create different windows and components of the GUI. The MenuBox function creates a title frame and a frame for buttons within the application window. The clear_window function clears all widgets from the window. The MenuWindow function clears the window and creates a menu box with a specific title. The BlackmagicManualWindow function clears the window, creates a menu box with a specific title, and creates a frame for a text box.

# Features

The Tkinter GUI application code consists of several features, including Tkinter utilization, function definitions, class definitions, and window management. Tkinter is Python's standard GUI toolkit used for creating the interface. The application features a menu box, clear_window, menu window, and blackmagic manual window. Class definitions may include classes for complex widgets or data handling. Window management functions manage the opening, closing, and refreshing of different windows within the application. This modular approach allows for the display or hiding of components as needed. For further assistance or specific questions about the implementation, feel free to ask.

# Imports

customtkinter, CTk, CTkLabel, CTkButton, CTkFrame, CTkScrollbar, CText

# **Note:**

If any issues:

    Steps to solve error

```
conn = odbc.connect(connection_String)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
pyodbc.InterfaceError: ('IM002', '[IM002] [Microsoft][ODBC Driver Manager] Data source name not found and no default driver specified (0) (SQLDriverConnect)')
line 12, in <module>
```

1. Install latest Version of SQL Server Management Studio
2. Make a default SQL server

   * Note:
     * The Server Name
     * Authentication: Windows Authentication
     * Encryption: Mandatory
     * Trust Server certificate: picked
     * (Might be optional) Connection string: TrustServerCertificate=yes;
3. Install latest [ODBC Data Source Administrator](https://learn.microsoft.com/en-us/sql/odbc/admin/odbc-data-source-administrator?view=sql-server-ver16) and look for the 'Drivers' tab

   * Look for Item 'ODBC Driver # for SQL Server' this would be used in python as your driver.
4. On Python, here is an example code to get started

```
import pyodbc as odbc
def connectSQL():
    DRIVER = 'ODBC Driver __ for SQL Server' # look at number 3 for details
    SERVER_NAME = '___' # look at number 2 for details
    DATABASE_NAME = 'master' # pick your SQL form
    connection_String = f"""
        DRIVER={DRIVER};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trusted_Connection=yes;
        TrustServerCertificate=yes; # Importent ADD THIS
    """
    try:
        conn = odbc.connect(connection_String)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ___;") # find the table name you wish to use, you can make yor own
        rows = cursor.fetchall()
        print(rows)
    except Exception as e:
        print("Error:", e)
connectSQL()
```
