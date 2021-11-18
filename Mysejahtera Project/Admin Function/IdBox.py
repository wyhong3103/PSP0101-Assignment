def idbox_gui(window):
    from pathlib import Path
    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
    from pathlib import Path
    from tkinter import Tk, Canvas, Button, PhotoImage
    import tkinter as tk
    import sqlite3
    from tkinter import ttk
    import tkinter
    from tkinter import messagebox

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./Admin Assets Folder/IdBoxassets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def viewinfo(window2,window):
        useroid = entry_1.get()
        from view_userdetail_admin import  view_userdetails_admin_gui
        view_userdetails_admin_gui(useroid)


    def destroy():
        window2.destroy()









    window2 = tk.Toplevel(window)
    window2.tk.call('wm', 'iconphoto', window2._w, tk.PhotoImage(file='./icon2.png'))
    window2.geometry("297x250")
    window2.configure(bg="#05BDF7")
    window2.title("MySejaterah")

    canvas = Canvas(
        window2,
        bg="#05BDF7",
        height=250,
        width=297,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    canvas.create_image(
        178.0,
        102.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        window2,
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_1.place(
        x=104.0,
        y=91.0,
        width=148.0,
        height=20.0
    )

    canvas.create_text(
        64.0,
        14.0,
        anchor="nw",
        text="View User Info\n",
        fill="#FFFFFF",
        font=("Roboto Bold", 24 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(window2,
                      image=button_image_1,
                      borderwidth=0,
                      highlightthickness=0,
                      command=lambda: viewinfo(window2,window),
                      relief="flat"
                      )
    button_1.place(
        x=85.0,
        y=140.0,
        width=128.0,
        height=34.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(window2,
                      image=button_image_2,
                      borderwidth=0,
                      highlightthickness=0,
                      command=destroy,
                      relief="flat"
                      )
    button_2.place(
        x=98.0,
        y=195.0,
        width=89.0,
        height=31.0
    )

    canvas.create_text(
        20.0,
        91.0,
        anchor="nw",
        text="User ID:",
        fill="#FFFFFF",
        font=("Roboto Bold", 18 * -1)
    )
    window2.resizable(False, False)
    window2.mainloop()
