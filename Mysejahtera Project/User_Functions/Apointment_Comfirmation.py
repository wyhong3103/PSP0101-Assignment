def apointment_status_gui(useroid):
    from pathlib import Path
    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
    import sqlite3
    from tkinter import messagebox
    import tkinter as tk
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./Assets Folder/Appointment_Confirm_Assets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    connector = sqlite3.connect("database.db")
    my_cursor = connector.cursor()
    my_cursor.execute("SELECT * FROM vax_appointment")
    vaxdetails = my_cursor.fetchall()
    status = False
    location = ""
    date = ""
    time = ""
    for i in vaxdetails:
        if str(i[1]) == str(useroid):
            location = i[4]
            date = i[6]
            time = i[7]
            status = True



    def back(useroid):
        window.destroy()
        connector.close()
        from Usermainmenu import usermainmenu
        usermainmenu(useroid)


    def yes():
        connector = sqlite3.connect("database.db")
        my_cursor = connector.cursor()

        my_cursor.execute("""UPDATE vax_appointment SET 
                  confirmation = :cfrmation

                  WHERE useroid = :useroid
                  """,
                          {
                              "cfrmation":"Y",
                              "useroid": useroid
                          })
        my_cursor.execute("""UPDATE person_data SET
                  appointmentstatus = :apmentstatus,
                  appointmentdate = :apmentdate,
                  appointmenttime = :apmenttime,
                  appointmentlocation = :apmentloc
                  WHERE oid = :oid
                  """,
                          {
                              "apmentstatus": "Y",
                              "apmentdate": date,
                              "apmenttime": time,
                              "apmentloc": location,
                              "oid": useroid
                          })
        my_cursor.execute("""UPDATE person_data SET notification = :notif WHERE oid = :useroid""",
                          {"notif": 0, "useroid": useroid})
        connector.commit()
        connector.close()
        messagebox.showinfo("Confirmed", "Appointment has been confirmed!", )
        window.destroy()
        from Usermainmenu import usermainmenu
        usermainmenu(useroid)





    def no():
        connector = sqlite3.connect("database.db")
        my_cursor = connector.cursor()
        my_cursor.execute("SELECT * FROM vax_appointment")

        my_cursor.execute("DELETE from vax_appointment WHERE useroid =" + str(useroid))
        my_cursor.execute("""UPDATE person_data SET
                    appointmentstatus = :apmentstatus,
                    appointmentdate = :apmentdate,
                    appointmenttime = :apmenttime,
                    appointmentlocation = :apmentloc
                    WHERE oid = :oid
                    """,
                          {
                              "apmentstatus": "N",
                              "apmentdate": "N",
                              "apmenttime": "N",
                              "apmentloc": "N",
                              "oid": useroid
                          })

        my_cursor.execute("""UPDATE person_data SET notification = :notif WHERE oid = :useroid""",
                          {"notif": 0, "useroid": useroid})
        connector.commit()
        connector.close()
        messagebox.showinfo("Cancelled", "Appointment has been cancelled!", )
        window.destroy()
        from Usermainmenu import usermainmenu
        usermainmenu(useroid)
        







    window = Tk()
    window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='./icon2.png'))
    window.title("MySejaterah")
    window.geometry("500x342")
    window.configure(bg="#05BDF7")


    canvas = Canvas(
        window,
        bg="#05BDF7",
        height=345,
        width=1000,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_text(
        150.0,
        13.0,
        anchor="nw",
        text="You have received an \napointment",
        fill="#FFFFFF",
        font=("Roboto Bold", 22 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=yes,
        relief="flat"
    )
    button_1.place(
        x=100.0,
        y=250.0,
        width=127.0,
        height=34.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=no,
        relief="flat"
    )
    button_2.place(
        x=322.0,
        y=250.0,
        width=127.0,
        height=34.0
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
        x=230.0,
        y=298.0,
        width=89.0,
        height=31.0
    )

    canvas.create_text(
        54.0,
        91.0,
        anchor="nw",
        text=("Date:",date),
        fill="#FFFFFF",
        font=("Roboto", 24 * -1)
    )

    canvas.create_text(
        54.0,
        119.0,
        anchor="nw",
        text=("Time:",time),
        fill="#FFFFFF",
        font=("Roboto", 24 * -1)
    )

    canvas.create_text(
        54.0,
        147.0,
        anchor="nw",
        text=(f"Place:{location}"),
        fill="#FFFFFF",
        font=("Roboto", 24 * -1)
    )

    canvas.create_text(
        160.0,
        201.0,
        anchor="nw",
        text="Are You Able to Attend",
        fill="#FFFFFF",
        font=("Roboto", 18 * -1)
    )
    window.resizable(False, False)
    import tkinter as tk
    from tkinter import messagebox


    window.protocol("WM_DELETE_WINDOW", lambda: back(useroid))
    window.mainloop()

if __name__ == '__main__':
    apointment_status_gui()


