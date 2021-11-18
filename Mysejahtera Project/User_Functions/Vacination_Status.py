def vaccine_status(useroid):
    from pathlib import Path
    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
    import sqlite3
    from Usermainmenu import usermainmenu
    from tkinter import messagebox
    import tkinter as tk
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./Assets Folder/Appointment_Confirm_Assets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    connector = sqlite3.connect("database.db")
    my_cursor = connector.cursor()
    my_cursor.execute(
        "SELECT appointmentstatus ,appointmentdate,appointmenttime,appointmentlocation FROM person_data WHERE oid =" + str(
            useroid))
    vax_status = my_cursor.fetchall()
    for i in vax_status:
        date = i[1]
        time = i[2]
        location = i[3]
    connector.commit()
    connector.close()

    def back(useroid):
        window.destroy()
        connector.close()
        from Usermainmenu import usermainmenu
        usermainmenu(useroid)


    window = Tk()

    window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='./icon2.png'))
    window.geometry("400x300")
    window.configure(bg="#05BDF7")
    window.title("MySejaterah")

    canvas = Canvas(
        window,
        bg="#05BDF7",
        height=342,
        width=351,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_text(
        53.0,
        13.0,
        anchor="nw",
        text="Appointment Status:",
        fill="#FFFFFF",
        font=("Roboto Bold", 22 * -1)
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: back(useroid),
        relief="flat"
    )
    button_3.place(
        x=136.0,
        y=250.0,
        width=89.0,
        height=31.0
    )

    canvas.create_text(
        45.0,
        91.0,
        anchor="nw",
        text="Date:" + date,
        fill="#FFFFFF",
        font=("Roboto", 24 * -1)
    )

    canvas.create_text(
        45.0,
        119.0,
        anchor="nw",
        text="Time:" + time,
        fill="#FFFFFF",
        font=("Roboto", 24 * -1)
    )

    canvas.create_text(
        45.0,
        147.0,
        anchor="nw",
        text="Location:" + location,
        fill="#FFFFFF",
        font=("Roboto", 20 * -1)
    )


    window.resizable(False, False)
    import tkinter as tk
    from tkinter import messagebox


    window.protocol("WM_DELETE_WINDOW", lambda: back(useroid))
    window.mainloop()


if __name__ == '__main__':
    apointment_status_gui()