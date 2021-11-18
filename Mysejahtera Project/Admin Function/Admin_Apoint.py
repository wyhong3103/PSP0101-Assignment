
from sqlite3.dbapi2 import connect


def admim_apoint_gui():
    from pathlib import Path
    from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
    import  sqlite3
    from tkinter import ttk
    import datetime
    import tkinter
    from tkinter import messagebox
    import tkinter as tk



    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./Admin Assets Folder/Admin_Apoint_assets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)



    def apoint():

        def filtering_list():
            connector = sqlite3.connect("database.db")
            my_cursor = connector.cursor()
            my_cursor.execute("SELECT * FROM health_data")
            record = my_cursor.fetchall()
            eligible_list = []
            for id in record:
                if (id[0].lower() == "n" and id[1].lower() == "n" and id[2].lower() == "n" and id[4].lower() == "y"):
                    eligible_list.append(id[-1])

            connector.commit()
            connector.close()
            return eligible_list

        connector = sqlite3.connect("database.db")
        my_cursor = connector.cursor()        
        my_cursor.execute("SELECT *,oid FROM vax_center")
        vax_centerlist = my_cursor.fetchall()


        vax_id_gui= (entry_2.get())
        patient_id_gui = entry_1.get()
        date_gui = datedropdown.get()
        months_gui = monthsdropdown.get()
        year_gui = yeardropdown.get()
        hour_gui= hourdropdown.get()
        min_gui = mindropdown.get()


        for center in vax_centerlist:
         vax_centerid_v = str(vax_id_gui)
         centerid_validation = False
        for centerid in vax_centerlist:
            if vax_centerid_v == str(centerid[-1]):
                centerid_validation = True
                vax_centerid = vax_centerid_v
        if centerid_validation == False:
            messagebox.showwarning("Warning","Invalid Vax Center ID!")
            return
        vax_centername = ""
        for center in vax_centerlist:
            if str(center[-1]) == str(vax_centerid):
                vax_centername = center[0]
        my_cursor.execute("SELECT *,oid FROM person_data ORDER BY risk")
        personlist = my_cursor.fetchall()
        filtered_list = filtering_list()
        my_cursor.execute("SELECT * FROM vax_appointment")
        receive_or_not = my_cursor.fetchall()
        received_id_list = []
        for i in receive_or_not:
            received_id_list.append(i[1])
        for person in personlist:
            if ((person[12] == "N") and (str(person[-1]) in filtered_list)) and (
                    str(person[-1]) not in received_id_list):

                    userid_v = (patient_id_gui)
                    userid_validation = False
        for uid in personlist:
            if ((uid[12] == "N") and (str(uid[-1]) in filtered_list)) and (str(uid[-1]) not in received_id_list):
                if str(userid_v) == str(uid[-1]):
                    userid_validation = True
                    userid = userid_v
        if userid_validation == False:
            messagebox.showwarning("Warning","Invalid User ID!")
            return
        username = ""
        if userid_validation == True:
            for person in personlist:
                if str(person[-1]) == userid:
                    username = person[2]
                    phone = person[4]
                    ic = person[5]
            try:  # datetime input validation
                date_i = F"{date_gui}/{months_gui}/{year_gui}"
                date_v = datetime.datetime.strptime(date_i, "%d/%m/%y")
                date = date_v.strftime("%d/%m/%y")
                today = datetime.datetime.now()
                today_date = today.strftime("%d/%m/%y")
                today_object = datetime.datetime.strptime(today_date, "%d/%m/%y")
                today_timestamp = datetime.datetime.timestamp(today_object)
                date_validation = datetime.datetime.timestamp(date_v)
                if date_validation < (today_timestamp + 86400):
                    messagebox.showwarning("Warning","You can only assign an appointment which is at least 1 day later than today!")
                    connector.close()
                    return
                time_vax = F"{hour_gui}:{min_gui}"
                timevalidate = datetime.datetime.strptime(time_vax, "%H:%M")
                hour = timevalidate.strftime("%H")
                if hour in ["18", "19", "20", "21", "22", "23", "24", "00", "01", "02", "03", "04", "05", "06",
                            "07", "08", "09"]:
                    messagebox.showinfo("Date","Make sure Date Is Selected")
                my_cursor.execute("SELECT capacityperhour FROM vax_center WHERE oid =" + vax_centerid)
                capacityperhour = my_cursor.fetchall()
                my_cursor.execute("SELECT date,time FROM vax_appointment WHERE vaxcenterid =" + vax_centerid)
                date_time = my_cursor.fetchall()
                counter = 0
                for dateandtime in date_time:
                    if dateandtime[0] == date and dateandtime[1][0:2] == hour:
                        counter += 1
                if counter < capacityperhour[0][0]:
                    my_cursor.execute(
                        "INSERT INTO vax_appointment VALUES(:username, :userid ,:phone,:ic,:vaxcenter ,:vaxid, :date, :time , :confirmation)",
                        {
                            "username": username,
                            "userid": userid,
                            "phone" : phone,
                            "ic" : ic,
                            "vaxcenter": vax_centername,
                            "vaxid": vax_centerid,
                            "date": date,
                            "time": time_vax,
                            "confirmation": "N"
                        })
                    messagebox.showinfo("Assign Appointment", "Appointment assigned! Awaiting for user's confirmation!")
                    my_cursor.execute("""UPDATE person_data SET notification = :notif WHERE oid = :useroid""",
                                        {"notif": 1, "useroid": userid})
                    connector.commit()
                    connector.close()
                    window.destroy()
                    admim_apoint_gui()
                else:
                    messagebox.showwarning("Warning", "The vaccination capacity for the exact hour is fulled!")
                    connector.close()
                    return
            except (TypeError, ValueError):
                messagebox.showerror("Error","Invalid Input")
                connector.close()
                window.destroy()
                admim_apoint_gui()



    def back():
        window.destroy()
        from AdminMainMenu import adminmainmenu
        adminmainmenu()
        



    def view_usr():
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
        window2.geometry("925x220")
        window2.eval('tk::PlaceWindow . center')
        window2.configure(bg="#22AFFF")
        window2.title("MySejaterah")

        connector = sqlite3.connect("database.db")
        my_cursor = connector.cursor()
        def filtering_list():
            connector = sqlite3.connect("database.db")
            my_cursor = connector.cursor()
            my_cursor.execute("SELECT * FROM health_data")
            record = my_cursor.fetchall()
            eligible_list = []
            for id in record:
                if (id[0].lower() == "n" and id[1].lower() == "n" and id[2].lower() == "n" and id[4].lower() == "y"):
                    eligible_list.append(id[-1])

            connector.commit()
            connector.close()
            return eligible_list

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
        windowscroll.place(x=910, y=0, height=200 + 20)

        tree.configure(yscrollcommand=windowscroll.set)
        # number of collums
        tree["column"] = ("Oid", "Username", "Occupation","State","Postcode","Risk", "Priority","IC","Phone")

        # Assigning size and Width
        tree.column("Oid", width=50, minwidth=10, anchor=tkinter.CENTER)
        tree.column("Username", width=100, minwidth=100, anchor=tkinter.CENTER)
        tree.column("Occupation", width=150, minwidth=100, anchor=tkinter.CENTER)
        tree.column("State", width=100, minwidth=30, anchor=tkinter.CENTER)
        tree.column("Postcode", width=70, minwidth=30, anchor=tkinter.CENTER)
        tree.column("Risk", width=70, minwidth=30, anchor=tkinter.CENTER)
        tree.column("Priority", width=70, minwidth=30, anchor=tkinter.CENTER)
        tree.column("IC", width=150, minwidth=100, anchor=tkinter.CENTER)
        tree.column("Phone", width=150, minwidth=100, anchor=tkinter.CENTER)


        # Assining the Heading
        tree.heading("Oid", text="ID", anchor=tkinter.CENTER)
        tree.heading("Username", text="Username", anchor=tkinter.CENTER)
        tree.heading("Occupation", text="Occupation", anchor=tkinter.CENTER)
        tree.heading("State", text="State", anchor=tkinter.CENTER)
        tree.heading("Postcode", text="Postcode", anchor=tkinter.CENTER)
        tree.heading("Risk", text="Risk", anchor=tkinter.CENTER)
        tree.heading("Priority", text="Priority", anchor=tkinter.CENTER)
        tree.heading("IC", text="Ic no", anchor=tkinter.CENTER)
        tree.heading("Phone", text="Phone", anchor=tkinter.CENTER)


        my_cursor.execute("SELECT *,oid FROM person_data")
        list_of_user = [i for i in my_cursor.fetchall() if str(i[-1]) in filtering_list()]
        my_cursor.execute("SELECT useroid FROM vax_appointment")
        received_user = my_cursor.fetchall()
        connector.commit()
        connector.close()
        received_user_id = [i[0] for i in received_user]
        list_of_user1 = [i for i in list_of_user if str(i[-1]) not in received_user_id]
        i = 0

        for ro in list_of_user1:
            
            tree.insert('', i, text="", values=(ro[-1], ro[2], ro[6], ro[7],ro[8],ro[10],ro[11],ro[5],ro[4]))
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


    def view_vax():
        from pathlib import Path
        from tkinter import Tk, Canvas, Button, PhotoImage
        import sqlite3
        from tkinter import ttk
        import tkinter
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path("./View_all_user_assets")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        window3 = Tk()
        window3.geometry("505x220")
        window3.eval('tk::PlaceWindow . center')
        window3.configure(bg="#22AFFF")
        window3.title("MySejaterah")

        connector = sqlite3.connect("database.db")
        my_cursor = connector.cursor()
        my_cursor.execute("SELECT *,oid FROM vax_center")
        vax_center = my_cursor.fetchall()
        connector.commit()
        connector.close()

        canvas = Canvas(
            window3,
            bg="#22AFFF",
            height=371,
            width=420,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        tree = ttk.Treeview(window3)
        tree["show"] = "headings"
        windowscroll = ttk.Scrollbar(window3, orient="vertical", command=tree.yview)
        windowscroll.place(x=490, y=0, height=200 + 20)

        tree.configure(yscrollcommand=windowscroll.set)
        # number of collums
        tree["column"] = ("Oid", "VaxName", "State", "Postcode" , "Capacity Per Hour")

        # Assigning size and Width
        tree.column("Oid", width=30, minwidth=10, anchor=tkinter.CENTER)
        tree.column("VaxName", width=120, minwidth=100, anchor=tkinter.CENTER)
        tree.column("State", width=150, minwidth=100, anchor=tkinter.CENTER)
        tree.column("Postcode", width=70, minwidth=30, anchor=tkinter.CENTER)
        tree.column("Capacity Per Hour", width=120, minwidth=30, anchor=tkinter.CENTER)

        # Assining the Heading
        tree.heading("Oid", text="Oid", anchor=tkinter.CENTER)
        tree.heading("VaxName", text="Vacination Center", anchor=tkinter.CENTER)
        tree.heading("State", text="State", anchor=tkinter.CENTER)
        tree.heading("Postcode", text="Postcode", anchor=tkinter.CENTER)
        tree.heading("Capacity Per Hour", text="Capacity per Hr", anchor=tkinter.CENTER)

        i = 0
        for ro in vax_center:
            tree.insert('', i, text="", values=(ro[-1], ro[0], ro[1], ro[2] , ro[3]))
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
    window.geometry("297x420")
    window.configure(bg="#05BDF7")
    window.title("MySejaterah")

    canvas = Canvas(
        window,
        bg="#05BDF7",
        height=420,
        width=297,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        198.00000000000003,
        223.99999999999997,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_1.place(
        x=124.00000000000003,
        y=212.99999999999997,
        width=148.0,
        height=20.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        198.00000000000003,
        185.99999999999997,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_2.place(
        x=124.00000000000003,
        y=174.99999999999997,
        width=148.0,
        height=20.0
    )


    canvas.create_text(
        7.000000000000028,
        177.99999999999997,
        anchor="nw",
        text="Vax Center ID:",
        fill="#FFFFFF",
        font=("Roboto", 14 * -1)
    )

    canvas.create_text(
        20.00000000000003,
        212.99999999999997,
        anchor="nw",
        text="Patient ID:",
        fill="#FFFFFF",
        font=("Roboto", 17 * -1)
    )

    canvas.create_text(
        10.00000000000003,
        250.99999999999997,
        anchor="nw",
        text="Date(dd/mm/yy):",
        fill="#FFFFFF",
        font=("Roboto", 16 * -1)
    )

    canvas.create_text(
        10.00000000000003,
        291.0,
        anchor="nw",
        text="Time(HH/MM):",
        fill="#FFFFFF",
        font=("Roboto", 17 * -1)
    )

    canvas.create_text(
        60.00000000000003,
        9.999999999999972,
        anchor="nw",
        text="Assign an Appointment",
        fill="#FFFFFF",
        font=("Roboto Bold", 20 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=apoint,
        relief="flat"
    )
    button_1.place(
        x=88.00000000000003,
        y=327.0,
        width=128.0,
        height=34.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=view_vax,
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
        command=view_usr,
        relief="flat"
    )
    button_3.place(
        x=70.00000000000003,
        y=119.99999999999997,
        width=164.0,
        height=34.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=back,
        relief="flat"
    )
    button_4.place(
        x=107.00000000000003,
        y=377.0,
        width=89.0,
        height=30.0
    )

    Date= ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]

    Months=["1","2","3","4","5","6","7","8","9","10","11","12"]

    Year =["21","22","23","24","25","26"]

    Hour = ["10","11","12","13","14","15","16","17"]

    Min = ["00","10","20","30","40","50",]

    datedropdown = ttk.Combobox(
        window,
        width=10,
        value=(Date)
    )
    datedropdown.place(
        x=150.0,
        y=250.5,
        width=35.0

    )

    monthsdropdown = ttk.Combobox(
        window,
        width=10,
        value=(Months)
    )
    monthsdropdown.place(
        x=200.0,
        y=250.5,
        width=35.0

    )

    yeardropdown = ttk.Combobox(
        window,
        width=10,
        value=(Year)
    )
    yeardropdown.place(
        x=250.0,
        y=250.5,
        width=35.0

    )

    hourdropdown = ttk.Combobox(
        window,
        width=10,
        value=(Hour)
    )
    hourdropdown.place(
        x=150,
        y=291.5,
        width=35.0

    )

    mindropdown = ttk.Combobox(
        window,
        width=10,
        value=(Min)
    )
    mindropdown.place(
        x=200.0,
        y=291.5,
        width=35.0

    )

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            window.quit()
            window.destroy()

    window.protocol("WM_DELETE_WINDOW", back)
    window.resizable(False, False)
    window.mainloop()

if __name__ == '__main__':
    admim_apoint_gui()
