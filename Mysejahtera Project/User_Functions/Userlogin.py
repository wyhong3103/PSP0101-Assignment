def userlogin():
    import sqlite3
    from pathlib import Path
    from tkinter import messagebox
    from passlib.hash import pbkdf2_sha256
    from tkinter import Tk, Canvas, Entry, Button, PhotoImage
    import tkinter as tk

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./Assets Folder/userloginassets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window = Tk()
    window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='./icon2.png'))
    window.eval('tk::PlaceWindow . center')
    window.title("MySejaterah")
    window.geometry("420x297")
    window.configure(bg="#FFFFFF")

    def backtomainmenu():
        window.destroy()
        from Mainmenu import mainmenu
        mainmenu()

#password verificaton
    def logingui():
        UsernameGui = entry_1.get()
        PasswordGui = entry_2.get()
        connector = sqlite3.connect("database.db")
        my_cursor = connector.cursor()
        username = UsernameGui
        password = PasswordGui
        my_cursor.execute("SELECT *,oid FROM person_data")
        logindetails = my_cursor.fetchall()
        userloginbool = False
        for i in logindetails:
            validation = pbkdf2_sha256.verify(password,i[1])
            if i[0] == username and validation:
                userloginbool = True
                useroid = i[-1]
                

        if userloginbool:
            messagebox.showinfo("Login", "Login Sucessfully!")
            window.destroy()
            from Usermainmenu import usermainmenu
            usermainmenu(useroid)
            connector.commit()
            connector.close()
        else:
            messagebox.showerror("Login", "Invalid Credential!")
            connector.close()
        return 0


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
        152.0,
        297.0,
        fill="#1AA1DB",
        outline="")

    canvas.create_text(
        18.0,
        130.0,
        anchor="nw",
        text="enter your details",
        fill="#FFFFFF",
        font=("Roboto", 15 * -1)
    )

    canvas.create_text(
        18.0,
        112.0,
        anchor="nw",
        text="Welcome,Please",
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
    entry_2 = Entry(
        show="*",
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
        command=logingui,
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
        command= backtomainmenu,
        relief="flat"
    )
    button_2.place(
        x=241.0,
        y=246.0,
        width=86.0,
        height=31.0
    )
    window.resizable(False, False)
    import tkinter as tk
    from tkinter import messagebox



    window.protocol("WM_DELETE_WINDOW", backtomainmenu)
    window.mainloop()


if __name__ == '__main__':
    userlogin()
