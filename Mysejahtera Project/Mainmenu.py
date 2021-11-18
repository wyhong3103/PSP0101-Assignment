# ********************************************************* 
# Program: Mainmenu.py 
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN 
# Class: TL6V
# Trimester: 2110
# Year: 2021/22 Trimester 1 
# Member_1: 1211101392 | wong Yen Hong| 1211101392@student.mmu.edu.my | 017-299 5322
# Member_2: 1211101534 | Tan Chi Lim | 1211101534@student.mmu.edu.my | 012-256 9650
# Member_3: 1211101615 | Thanirmalai Nagappan | 1211101615@student.mmu.edu.my | 019-479 8675
# Member_4: 1211101399 | Karthigeayah A/L Maniam | 1211101399@student.mmu.edu.my | 011-5951 8636
# *********************************************************
# Task Distribution
# Member_1: Admin's Side Work
# Member_2: Admin's Side Work
# Member_3: User's Side Work
# Member_4: User's Side Work
# *********************************************************

def mainmenu():
    from pathlib import Path
    from tkinter import Tk, Canvas,Button, PhotoImage
    import sys
    import tkinter as tk
    sys.path.append("./User_Functions")
    sys.path.append("./Admin Function")
    

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def adminlogin():
        window.destroy()
        from Adminlogin import adminlogin
        adminlogin()


    def userregister():
        window.destroy()
        from Register_User import register_user_gui
        register_user_gui()

    def userlogin(userlogin=None):
        window.destroy()
        from Userlogin import userlogin
        userlogin()


    window = Tk()
    window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='./icon2.png'))
    window.eval('tk::PlaceWindow . center')
    window.title("MySejaterah")
    window.geometry("420x297")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=297,
        width=420,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        0.0,
        221.0,
        297.0,
        fill="#1AA1DB",
        outline="")

    canvas.create_text(
        28.0,
        91.0,
        anchor="nw",
        text="Hey!! There",
        fill="#FFFFFF",
        font=("Roboto", 16 * -1)
    )

    canvas.create_text(
        28.0,
        110.0,
        anchor="nw",
        text="Welcome to",
        fill="#FFFFFF",
        font=("Roboto", 16 * -1)
    )

    canvas.create_text(
        28.0,
        125.0,
        anchor="nw",
        text="MySejatera",
        fill="#FFFFFF",
        font=("Roboto", 16 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=userlogin,
        relief="flat"
    )
    button_1.place(
        x=268.0,
        y=65.0,
        width=107.0,
        height=36.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=userregister,
        relief="flat"
    )
    button_2.place(
        x=268.0,
        y=106.0,
        width=107.0,
        height=36.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=adminlogin,
        relief="flat"
    )
    button_3.place(
        x=268.0,
        y=235.0,
        width=107.0,
        height=36.0
    )

    canvas.create_text(
        246.0,
        44.0,
        anchor="nw",
        text="Please Choose an option:",
        fill="#000000",
        font=("Roboto", 14 * -1)
    )

    canvas.create_text(
        266.0,
        214.0,
        anchor="nw",
        text="Are you an Admin:",
        fill="#000000",
        font=("Roboto", 14 * -1)
    )
    window.resizable(False, False)
    import tkinter as tk
    from tkinter import messagebox

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            quit()

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()
if __name__ == '__main__':
    mainmenu()