def admin_view_user_type():
    from pathlib import Path
    from tkinter import Tk, Canvas, Button, PhotoImage
    from tkinter import messagebox
    import tkinter as tk


    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./Admin Assets Folder/admin_view_user_assets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def back():
        window.destroy()
        from AdminMainMenu import adminmainmenu
        adminmainmenu()

    window = Tk()

    def viewallinfo():
        window.destroy()
        from View_all_user_info_gui import view_all_user
        view_all_user()

    def view_by_risk():
        window.destroy()
        from View_all_user_info_gui import view_by_risk
        view_by_risk()

    def view_postcode():
        window.destroy()
        from View_all_user_info_gui import view_by_postcode
        view_by_postcode()

    def view_priority():
        window.destroy()
        from View_all_user_info_gui import view_by_priority
        view_by_priority()

    window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='./icon2.png'))
    window.geometry("420x297")
    window.configure(bg="#FFFFFF")
    window.title("MySejaterah")
    window.eval('tk::PlaceWindow . center')

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
        27.0,
        104.0,
        anchor="nw",
        text="Please Choose",
        fill="#FFFFFF",
        font=("Roboto", 20 * -1)
    )

    canvas.create_text(
        27.0,
        127.0,
        anchor="nw",
        text="an Option",
        fill="#FFFFFF",
        font=("Roboto", 20 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=viewallinfo,
        relief="flat"
    )
    button_1.place(
        x=217.0,
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
        command=back,
        relief="flat"
    )
    button_2.place(
        x=252.0,
        y=249.0,
        width=113.0,
        height=44.0
    )

    canvas.create_text(
        20.0,
        141.0,
        anchor="nw",
        text="\n",
        fill="#FFFFFF",
        font=("Roboto", 20 * -1)
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=view_by_risk,
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
        command=view_postcode,
        relief="flat"
    )
    button_4.place(
        x=217.0,
        y=142.0,
        width=187.0,
        height=44.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=view_priority,
        relief="flat"
    )
    button_5.place(
        x=215.0,
        y=195.0,
        width=199.0,
        height=44.0
    )

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            window.quit()
            window.destroy()


    window.protocol("WM_DELETE_WINDOW", back)
    window.resizable(False, False)
    window.mainloop()
if __name__ == '__main__':
    admin_view_user_type()