def admin_update_appoint_gui():
    from pathlib import Path
    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
    import sqlite3
    from tkinter import messagebox
    import tkinter as tk


    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./Admin Assets Folder/Admin_Delete_assets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)




    def delete():

        user_id = entry_1.get()



        connector = sqlite3.connect("database.db")
        my_cursor = connector.cursor()
        my_cursor.execute("SELECT *,oid FROM vax_appointment ORDER BY useroid")
        record = my_cursor.fetchall()
        for i in record:
            choice = 1
        if choice == 1:
            connector = sqlite3.connect("database.db")
            my_cursor = connector.cursor()
            user = (user_id)
            my_cursor.execute("SELECT * FROM vax_appointment")
            vax_appointment_v = my_cursor.fetchall()
            if user in [i[1] for i in vax_appointment_v]:
                for i in vax_appointment_v:
                    if str(user) == i[1] and i[-1] == "N":
                        my_cursor.execute("DELETE from vax_appointment WHERE useroid =" + str(user))
                        my_cursor.execute("""UPDATE person_data SET notification = :notif WHERE oid = :useroid""",
                                          {"notif": 0, "useroid": user})
                        messagebox.showinfo("Appointment Update", "Appointment Deleted")
                        connector.commit()
                        connector.close()
                    elif str(user) == i[1] and i[-1] == "Y":
                        my_cursor.execute("DELETE from vax_appointment WHERE useroid =" + str(user))
                        messagebox.showinfo("Appointment Update", "Appointment Deleted")
                        my_cursor.execute(
                            """UPDATE person_data SET appointmentstatus = :apmentstatus, appointmentdate = :apmentdate, appointmenttime = :apmenttime, appointmentlocation = :apmentloc,notification = :notif WHERE oid = :useroid""",
                            {"apmentstatus": "N", "apmentdate": "N", "apmenttime": "N", "apmentloc": "N", "notif": 2,
                             "useroid": user})
                        connector.commit()
                        connector.close()
                        window.destroy()
                        admin_update_appoint_gui()
            else:
                messagebox.showerror("Error", "User ID is not found in appointment list!")
                window.destroy()
                admin_update_appoint_gui()







    def back():
        window.destroy()
        from AdminMainMenu import adminmainmenu
        adminmainmenu()



    def userlist():
        from pathlib import Path
        from tkinter import Tk, Canvas, Button, PhotoImage
        import sqlite3
        from tkinter import ttk
        import tkinter
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("./View_all_user_assets")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        window2 = Tk()
        window2.geometry("620x220")
        window2.eval('tk::PlaceWindow . center')
        window2.configure(bg="#22AFFF")
        window2.title("MySejaterah")

        connector = sqlite3.connect("database.db")
        my_cursor = connector.cursor()
        my_cursor.execute("SELECT * FROM vax_appointment")
        appointment_list = [list(i) for i in my_cursor.fetchall()]
        for i in range(len(appointment_list)):
            appointment_list[i][1] = int(appointment_list[i][1])
        appointment_list.sort(key = lambda x : x[1])

        canvas = Canvas(
            window2,
            bg="#22AFFF",
            height=371,
            width=420,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        tree = ttk.Treeview(window2)
        tree["show"] = "headings"
        windowscroll = ttk.Scrollbar(window2, orient="vertical", command=tree.yview)
        windowscroll.place(x=605, y=0, height=200 + 20)

        tree.configure(yscrollcommand=windowscroll.set)
        # number of collums
        tree["column"] = ("Oid", "Username", "Phone","IC","VaxCenter", "Date","Time")

        # Assigning size and Width
        tree.column("Oid", width=50, minwidth=10, anchor=tkinter.CENTER)
        tree.column("Username", width=120, minwidth=100, anchor=tkinter.CENTER)
        tree.column("Phone", width=120, minwidth=30, anchor=tkinter.CENTER)
        tree.column("IC", width=120, minwidth=30, anchor=tkinter.CENTER)
        tree.column("VaxCenter", width=80, minwidth=50, anchor=tkinter.CENTER)
        tree.column("Date", width=65, minwidth=30, anchor=tkinter.CENTER)
        tree.column("Time", width=50, minwidth=30, anchor=tkinter.CENTER)
        

        # Assining the Heading
        tree.heading("Oid", text="ID", anchor=tkinter.CENTER)
        tree.heading("Username", text="Username", anchor=tkinter.CENTER)
        tree.heading("Phone", text="Phone", anchor=tkinter.CENTER)
        tree.heading("IC", text="IC", anchor=tkinter.CENTER)
        tree.heading("VaxCenter", text="VaxCenter", anchor=tkinter.CENTER)
        tree.heading("Date", text="Date", anchor=tkinter.CENTER)
        tree.heading("Time", text="Time", anchor=tkinter.CENTER)

        i = 0
        for ro in appointment_list:
            tree.insert('', i, text="", values=(ro[1], ro[0],ro[2],ro[3], ro[4], ro[6],ro[7]))
            i = i + 1
            tree.pack()

        tree.place(x=0, y=0)

        canvas.place(x=0, y=0)

        canvas.create_text(
            166.0,
            12.999999999999972,
            anchor="nw",
            text="User Details",
            fill="#FFFFFF",
            font=("Roboto Bold", 16 * -1)
        )

        canvas.create_rectangle(
            9.0,
            41.99999999999997,
            412.0,
            314.0,
            fill="#22AFFF",
            outline="")
        window.resizable(True, True)
        window.mainloop()



    window = Tk()
    window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='./icon2.png'))
    window.geometry("297x270")
    window.configure(bg="#05BDF7")
    window.title("MySejaterah")

    canvas = Canvas(
        window,
        bg="#05BDF7",
        height=270,
        width=297,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        192.00000000000003,
        133.99999999999997,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_1.place(
        x=118.00000000000003,
        y=122.99999999999997,
        width=148.0,
        height=20.0
    )

    canvas.create_text(
        19.00000000000003,
        122.99999999999997,
        anchor="nw",
        text="Patient ID:",
        fill="#FFFFFF",
        font=("Roboto", 16 * -1)
    )

    canvas.create_text(
        20.00000000000003,
        17.99999999999997,
        anchor="nw",
        text="Delete An User's Appoinment",
        fill="#FFFFFF",
        font=("Roboto Bold", 20 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=delete,
        relief="flat"
    )
    button_1.place(
        x=88.00000000000003,
        y=177.99999999999997,
        width=128.0,
        height=34.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=userlist,
        relief="flat"
    )
    button_2.place(
        x=70.00000000000003,
        y=64.99999999999997,
        width=164.0,
        height=34.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=back,
        relief="flat"
    )
    button_3.place(
        x=103.00000000000003,
        y=228.99999999999997,
        width=89.0,
        height=30.0
    )


    window.protocol("WM_DELETE_WINDOW", back)
    window.resizable(False, False)
    window.mainloop()


