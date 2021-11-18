def adminlogin():
    from pathlib import Path
    from tkinter import Tk, Canvas, Entry, Button, PhotoImage
    from tkinter import messagebox
    import sys
    import tkinter as tk

    #sys.path.append("./")

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./Admin Assets Folder/adminloginassets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def adminlogin():
            admin_name= entry_1.get()
            admin_passwd = entry_2.get()
            username = admin_name
            password = admin_passwd
            admin_list = [("yk","123"),("karthi","123"),("thanir","123"),("cl","123")]
            for i in admin_list:
                if username == i[0] and password == i[1]:
                    messagebox.showinfo("Admin Login", "Login Sucessfully")
                    window.destroy()
                    from AdminMainMenu import adminmainmenu
                    adminmainmenu()
                    return
            messagebox.showerror("Error", "Invalid Credential")


    def backtomainmenu():
        window.destroy()
        from Mainmenu import mainmenu
        mainmenu()

    window = Tk()
    window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='./icon2.png'))
    window.eval('tk::PlaceWindow . center')
    window.geometry("420x297")
    window.configure(bg="#FFFFFF")
    window.title("MySejaterah")

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
        4.0,
        162.0,
        301.0,
        fill="#1AA1DB",
        outline="")

    canvas.create_text(
        5.0,
        112.0,
        anchor="nw",
        text="Great to see you :)",
        fill="#FFFFFF",
        font=("Roboto", 15 * -1)
    )

    canvas.create_text(
        26.0,
        96.0,
        anchor="nw",
        text="Welcome,Admin",
        fill="#FFFFFF",
        font=("Roboto", 15 * -1)
    )

    canvas.create_text(
        210.0,
        39.0,
        anchor="nw",
        text="Log in",
        fill="#000000",
        font=("Roboto", 20 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        290.0,
        108.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0
    )
    entry_1.place(
        x=210.0,
        y=96.0,
        width=160.0,
        height=23.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        290.0,
        166.5,
        image=entry_image_2
    )
    entry_2 = Entry(show="*",
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0
    )
    entry_2.place(
        x=210.0,
        y=154.0,
        width=160.0,
        height=23.0
    )

    canvas.create_text(
        210.0,
        77.0,
        anchor="nw",
        text="Username:",
        fill="#000000",
        font=("Roboto", 12 * -1)
    )

    canvas.create_text(
        212.0,
        133.0,
        anchor="nw",
        text="Password:",
        fill="#000000",
        font=("Roboto", 12 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=adminlogin,
        relief="flat"
    )
    button_1.place(
        x=241.0,
        y=194.0,
        width=86.0,
        height=31.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=backtomainmenu,
        relief="flat"
    )
    button_2.place(
        x=241.0,
        y=246.0,
        width=86.0,
        height=31.0
    )

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            window.quit()
            window.destroy()

    window.protocol("WM_DELETE_WINDOW", backtomainmenu)
    window.resizable(False, False)
    window.mainloop()
if __name__ == '__main__':
    adminlogin()