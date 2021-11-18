def view_userdetails_admin_gui(useroid):
    global response4, x, i, response5, response3, response2, response1, appointmentlocation, appointmenttime, appointmentdate, appointmentstatus, priority, risk, eligibility, postcode, state, occupation, age, name
    from sqlite3.dbapi2 import OperationalError
    from pathlib import Path
    from tkinter import Tk, Canvas, Button, PhotoImage,messagebox
    import sqlite3
    import tkinter as tk


    connector = sqlite3.connect("database.db")
    my_cursor = connector.cursor()
    my_cursor.execute("SELECT oid FROM person_data")
    uservalidation = False
    list2 = my_cursor.fetchall()
    for i in list2:
        if str(useroid) == str(i[0]):
            uservalidation = True
            break
    if uservalidation == False:
        messagebox.showerror("Error!","Invalid User ID!")
        return 0
        

    
    my_cursor.execute("SELECT *,oid FROM person_data WHERE oid =" + str(useroid))
    persondata = my_cursor.fetchall()
    for i in persondata:
        name = i[2]
        age = str(i[3])
        phone = i[4]
        ic = i[5]
        occupation = i[6]
        state = i[7]
        postcode = str(i[8])
        eligibility = i[9]
        risk = str(i[10])
        priority = str(i[11])
        appointmentstatus = i[12]
        appointmentdate = i[13]
        appointmenttime = i[14]
        appointmentlocation = i[15]
    my_cursor.execute("SELECT *,oid FROM health_data WHERE useroid =" + str(useroid))
    healthdata = my_cursor.fetchall()
    for x in healthdata:
        response1 = x[0]
        response2 = x[1]
        response3 = x[2]
        response4 = x[3]
        response5 = x[4]


    connector.commit()
    connector.close()

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./userdetailassets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def usermainmenu(useroid):
        window4.destroy()
        from Usermainmenu import usermainmenu
        usermainmenu(useroid)


    window4 = Tk()
    window4.eval('tk::PlaceWindow . center')
    window4.geometry("420x380")
    window4.title("MySejaterah")
    window4.configure(bg="#22AFFF")

    canvas = Canvas(
        window4,
        bg="#22AFFF",
        height=371,
        width=420,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        17.0,
        39.99999999999997,
        402.0,
        350.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_text(
        47.0,
        48.99999999999997,
        anchor="nw",
        text="Name :"+(name),
        fill="#000000",
        font=("Roboto", 12 * -1)
    )

    canvas.create_text(
        47.0,
        62.99999999999997,
        anchor="nw",
        text=("Age:",age) ,
        fill="#000000",
        font=("Roboto", 12 * -1)
    )
    canvas.create_text(
        47.0,
        76.99999999999997,
        anchor="nw",
        text="Phone:"+ (phone),
        fill="#000000",
        font=("Roboto", 12 * -1)
    )
    canvas.create_text(
        47.0,
        90.99999999999997,
        anchor="nw",
        text="IC:"+ (ic),
        fill="#000000",
        font=("Roboto", 12 * -1)
    )

    canvas.create_text(
        47.0,
        104.99999999999997,
        anchor="nw",
        text="Occupation:"+ (occupation),
        fill="#000000",
        font=("Roboto", 12 * -1)
    )

    canvas.create_text(
        47.0,
        118.99999999999997,
        anchor="nw",
        text=("State :"+(state)),
        fill="#000000",
        font=("Roboto", 12 * -1)
    )

    canvas.create_text(
        47.0,
        132.99999999999997,
        anchor="nw",
        text=("Postcode:"+(postcode)),
        fill="#000000",
        font=("Roboto", 12 * -1)
    )

    canvas.create_text(
        47.0,
        146.99999999999997,
        anchor="nw",
        text="Eligibility :"+(eligibility),
        fill="#000000",
        font=("Roboto", 12 * -1)
    )

    canvas.create_text(
        47.0,
        158.99999999999997,
        anchor="nw",
        text="Risk :"+ (risk),
        fill="#000000",
        font=("Roboto", 12 * -1)
    )

    canvas.create_text(
        47.0,
        172.99999999999997,
        anchor="nw",
        text="Priority :"+ (priority),
        fill="#000000",
        font=("Roboto", 12 * -1)
    )

    canvas.create_text(
        47.0,
        186.99999999999997,
        anchor="nw",
        text="Appointment Status:"+ (appointmentstatus),
        fill="#000000",
        font=("Roboto", 12 * -1)
    )

    canvas.create_text(
        47.0,
        200.99999999999997,
        anchor="nw",
        text="Appointment Date :"+ (appointmentdate),
        fill="#000000",
        font=("Roboto", 12 * -1)
    )

    canvas.create_text(
        47.0,
        214.99999999999997,
        anchor="nw",
        text="Appointment Time:"+ (appointmenttime),
        fill="#000000",
        font=("Roboto", 12 * -1)
    )

    canvas.create_text(
        47.0,
        228.99999999999997,
        anchor="nw",
        text="Appointment Location :"+(appointmentlocation),
        fill="#000000",
        font=("Roboto", 12 * -1)
    )

    canvas.create_text(
        47.0,
        242.99999999999997,
        anchor="nw",
        text="-----USER'S MEDICAL HISTORY-----",
        fill="#000000",
        font=("Roboto", 12 * -1)
    )

    canvas.create_text(
        47.0,
        256.99999999999997,
        anchor="nw",
        text="Have you got any covid-19 symptoms?: "+x[0],
        fill="#000000",
        font=("Roboto", 12 * -1)
    )

    canvas.create_text(
        47.0,
        270.99999999999997,
        anchor="nw",
        text="Have you had any close contact with covid-19 patient?: "+x[1],
        fill="#000000",
        font=("Roboto", 12 * -1)
    )

    canvas.create_text(
        47.0,
        284.0,
        anchor="nw",
        text="Have you had any allergy?: "+x[2],
        fill="#000000",
        font=("Roboto", 12 * -1)
    )

    canvas.create_text(
        47.0,
        298.0,
        anchor="nw",
        text="Do you have any medical problems?: "+x[3],
        fill="#000000",
        font=("Roboto", 12 * -1)
    )

    canvas.create_text(
        47.0,
        312.0,
        anchor="nw",
        text="Do you like to receive covid-19 vaccination?: "+x[4],
        fill="#000000",
        font=("Roboto", 12 * -1)
    )


    canvas.create_text(
        166.0,
        12.999999999999972,
        anchor="nw",
        text="User Details",
        fill="#FFFFFF",
        font=("Roboto Bold", 16 * -1)
    )
    window4.resizable(False, False)
    window4.mainloop()