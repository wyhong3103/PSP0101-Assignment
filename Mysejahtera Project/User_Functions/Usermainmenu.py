def usermainmenu(useroid):
    global i
    from pathlib import Path
    from tkinter import Tk, Canvas,  Button, PhotoImage
    import sqlite3
    from tkinter import messagebox
    import tkinter as tk
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./Assets Folder/UserMainMenuassets")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    connector = sqlite3.connect("database.db")
    my_cursor = connector.cursor()
    my_cursor.execute("SELECT *,oid FROM person_data WHERE oid =" + str(useroid))
    persondata = my_cursor.fetchall()
    for i in persondata:
        name = i[2]
        notification = i[16]



    def apointment_status(useroid):
        if notification == 0:
            messagebox.showinfo("Appointment Status", "You Have Not Receive Any New Appointment!")
        elif notification == 1:
            window.destroy()
            from Apointment_Comfirmation import apointment_status_gui
            apointment_status_gui(useroid)



    def vax_status(useroid):
        connector.close()
        connector.close()
        window.destroy()
        from Vacination_Status import vaccine_status
        vaccine_status(useroid)

    def backtomainmenu():
        if messagebox.askokcancel("Log Out", "Do you want to log out?"):
            window.destroy()
            from Mainmenu import mainmenu
            mainmenu()

    def userdetail():
        window.destroy()
        from userdetailGui import user_details_gui
        user_details_gui(useroid)

    def medical_historry_gui(useroid):
        from medical_historry_gui import medical_history_register
        window.destroy()
        medical_history_register(useroid)



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
        191.0,
        297.0,
        fill="#1AA1DB",
        outline="")


    canvas.create_text(
        34.0,
        90.0,
        anchor="nw",
        text=(i[2]),
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
        command=lambda:medical_historry_gui(useroid),
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
        command=lambda: vax_status(useroid),
        relief="flat"
    )
    button_2.place(
        x=216.0,
        y=189.0,
        width=187.0,
        height=44.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: apointment_status(useroid),
        relief="flat"
    )
    button_3.place(
        x=216.0,
        y=137.0,
        width=187.0,
        height=44.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=backtomainmenu,
        relief="flat"
    )
    button_4.place(
        x=252.0,
        y=242.0,
        width=113.0,
        height=44.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=userdetail,
        relief="flat"
    )
    button_5.place(
        x=216.0,
        y=85.0,
        width=187.0,
        height=44.0
    )



    if notification == 1:
        messagebox.showinfo("Notification", "You have receive an appointment! Please respond to it!")
    elif notification == 2:
        messagebox.showwarning("Notification", "Your appointment has been cancelled! Please wait for a new appointment!")
        my_cursor.execute("""UPDATE person_data SET notification = :notif WHERE oid = :useroid""",{"notif" : 0 , "useroid" : useroid})
    connector.commit()
    connector.close()


    window.resizable(False, False)
    import tkinter as tk
    from tkinter import messagebox

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to Quit?"):
            quit()

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()

    if __name__ == '__main__':
        usermainmenu()

