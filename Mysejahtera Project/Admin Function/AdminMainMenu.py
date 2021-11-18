def adminmainmenu():
    from pathlib import Path
    from tkinter import Tk, Canvas, Button, PhotoImage
    import sqlite3
    from tkinter import messagebox
    import tkinter as tk


    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./Admin Assets Folder/AdminMainMenuAssets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def back_to_mainmenu():
        if messagebox.askokcancel("Log Out","Do you want to Log Out"):
            window.destroy()
            from Mainmenu import mainmenu
            mainmenu()

    def view_user_menu():
        window.destroy()
        from admin_view_user_type_Menu import admin_view_user_type
        admin_view_user_type()

    def addvaxcenter():
        window.destroy()
        from CreateVaxCenter import create_vax_center
        create_vax_center()

    def admin_apoint():
        window.destroy()
        from Admin_Apoint import admim_apoint_gui
        admim_apoint_gui()

    def admin_update():
        window.destroy()
        from admin_update_appoint import admin_update_appoint_gui
        admin_update_appoint_gui()


    window = Tk()
    window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='./icon2.png'))
    window.eval('tk::PlaceWindow . center')
    window.geometry("420x297")
    window.title("MySejaterah")
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
        1.0,
        191.0,
        298.0,
        fill="#1AA1DB",
        outline="")

    canvas.create_text(
        34.0,
        90.0,
        anchor="nw",
        text="Admin",
        fill="#FFFFFF",
        font=("Roboto", 20 * -1)
    )

    canvas.create_text(
        34.0,
        44.0,
        anchor="nw",
        text="Welcome",
        fill="#FFFFFF",
        font=("Roboto", 20 * -1)
    )

    canvas.create_text(
        34.0,
        67.0,
        anchor="nw",
        text="Back",
        fill="#FFFFFF",
        font=("Roboto", 20 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=view_user_menu,
        relief="flat"
    )
    button_1.place(
        x=216.0,
        y=33.0,
        width=187.0,
        height=44.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=back_to_mainmenu,
        relief="flat"
    )
    button_2.place(
        x=252.0,
        y=252.0,
        width=113.0,
        height=44.0
    )

    canvas.create_text(
        20.0,
        141.0,
        anchor="nw",
        text="Good to see you,\nbud :)",
        fill="#FFFFFF",
        font=("Roboto", 20 * -1)
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=addvaxcenter,
        relief="flat"
    )
    button_3.place(
        x=216.0,
        y=87.0,
        width=189.8992156982422,
        height=44.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=admin_apoint,
        relief="flat"
    )
    button_4.place(
        x=216.0,
        y=141.0,
        width=187.0,
        height=44.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=admin_update,
        relief="flat"
    )
    button_5.place(
        x=215.0,
        y=195.0,
        width=190.0,
        height=44.0
    )

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            quit()

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.resizable(False, False)
    window.mainloop()

if __name__ == '__main__':
    adminmainmenu()

