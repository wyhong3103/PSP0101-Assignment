def register_user_gui():
    from medical_historry_gui import medical_history_register
    from pathlib import Path
    from tkinter import Tk, Canvas, Entry, Button, PhotoImage
    import sqlite3
    from tkinter import messagebox
    from tkinter import ttk
    from passlib.hash import pbkdf2_sha256
    import tkinter as tk



    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./Assets Folder/reg2assets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def register():
        global useroid, postcode, state, age, name, username, state_int, occupation_int
        usernameGui = entry_1.get()
        passwordGui = entry_2.get()
        fullnameGui = entry_3.get()
        ageGui = entry_4.get()
        postcodeGui = entry_7.get()
        occupationGui = (dropdown.get())
        stateGui = (statedropdown.get())
        IcGui = entry_5.get()
        PhoneGUi = entry_6.get()



        connector = sqlite3.connect("database.db")
        my_cursor = connector.cursor()
        username_v = ""
        password = ""
        name_v = ""
        age_v = ""
        postcode_v = ""
        occupation = ""

        # Username Validation
        username_v = usernameGui
        my_cursor.execute("SELECT * FROM person_data")
        username_validation = my_cursor.fetchall()
        un_validaiton = True
        for un in username_validation:
            if username_v == un[0]:
                un_validaiton = False
        if un_validaiton == False:
            messagebox.showerror("Error", "Username is unavailable!")
            window.destroy()
            register_user_gui()
        username = username_v

        # Password Input
        password_p = passwordGui

        # Name Validaiton
        name_v = fullnameGui
        name_validation = True
        for char in name_v:
            if str(char) in [str(i) for i in range(0, 10)]:
                name_validation = False
        if name_validation == False:
            messagebox.showerror("Name Input Error","INVALID INPUT! YOU CANNOT INPUT NUMBER AS YOUR NAME!")
            window.destroy()
            register_user_gui()
        name = name_v.title()

        # Age Validation
        try:
            age_v = int(ageGui)
            if age_v >= 12 and age_v <= 120:
                age = age_v
            else:
                messagebox.showerror("Invalid input","Invalid Age")
                window.destroy()
                register_user_gui()
        except ValueError:
            messagebox.showerror("Invalid input","Invalid Age")
            window.destroy()
            register_user_gui()

        # Phone Number validation
        try:
            phone_v = (PhoneGUi)
            if len(phone_v) <= 11:
                phone = f"60{phone_v}"
        except ValueError:
            messagebox.showerror("IC Input Error","No symbols(including \"-\") or any letters are allowed!")

        try:
            ic_v = (IcGui)
            if len(ic_v) != 12:
                raise ValueError
            ic = ic_v
        except ValueError:
            messagebox.showerror("Ic Input Error", "Invalid IC Number! No symbols or letters can be included!")
            window.destroy()
            register_user_gui()


        # Occupation Input
        occupation_dict = {
            1: "Health-care Worker",
            2: "Community Services",
            3: "Energy, Food",
            4: "Transportation",
            5: "Students",
            6: "Others or None"
        }
        try:
            if occupationGui == "1#Health-care Worker":
                occupation_int = 1
            elif occupationGui == "2#Community Services":
                occupation_int = 2
            elif occupationGui == "3#Energy, Food":
                occupation_int = 3
            elif occupationGui == "4#Transportation":
                occupation_int = 4
            elif occupationGui == "5#Students" :
                occupation_int = 5
            elif occupationGui == "6#Others or None":
                occupation_int = 6



            occupation_v =  (occupation_int)

            if occupation_v not in range(1, 7):
                raise ValueError
            occupation = occupation_dict[occupation_v].title()

        except ValueError:
            messagebox.showerror("Please select value")
            window.destroy()
            register_user_gui()

        state_list = [
            "Johor",
            "Kuala Lumpur",
            "Kedah",
            "Kelantan",
            "Labuan",
            "Malacca",
            "Negeri Sembilan",
            "Pahang",
            "Penang",
            "Perak",
            "Perlis",
            "Putrajaya",
            "Sabah",
            "Sarawak",
            "Selangor",
            "Terengganu"
        ]

        if stateGui not in state_list:
            messagebox.showerror("State Input Error","Please select a state")
            window.destroy()
            register_user_gui()
        state = stateGui
            

        # Postcode Validation
        try:
            postcode_v = int(postcodeGui)
            if postcode_v >= 1000 and postcode_v <= 100000:
                postcode = postcode_v
            else:
                messagebox.showerror("Postcode Input Error","Invalid Postcode")
                window.destroy()
                register_user_gui()
        except ValueError:
            messagebox.showerror("Postcode Input Error","Invalid Postcode")
            window.destroy()
            register_user_gui()


        #Password encryption
        password = pbkdf2_sha256.hash(password_p)
        my_cursor.execute(
            "INSERT INTO person_data VALUES(:username ,:password, :name ,:age,:phone,:ic,:occupation,:state ,:postcode,:elgibility, :risk ,:priority, :appointmentstatus ,:appointmentdate, :appointmenttime ,:appointmentlocation, :notification)",
            {
                "username": username,
                "password": password,
                "name": name,
                "age": age,
                "phone": phone,
                "ic": ic,
                "occupation": occupation,
                "state": state,
                "postcode": postcode,
                "elgibility": "N",
                "risk": "Low",
                "priority": 1,
                "appointmentstatus": "N",
                "appointmentdate": "N",
                "appointmenttime": "N",
                "appointmentlocation": "N",
                "notification": 0
            })
        messagebox.showinfo("Register", "Please update your medical history to proceed!" )
        my_cursor.execute("SELECT *,oid FROM person_data")
        person_data = my_cursor.fetchall()
        for i in person_data:
            if i[0] == username and i[1] == password:
                useroid = i[-1]
        connector.commit()
        connector.close()
        window.destroy()
        medical_history_register(useroid)



    def backtomainmenu():
        window.destroy()
        from Mainmenu import mainmenu
        mainmenu()

    window = Tk()
    window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='./icon2.png'))
    window.eval('tk::PlaceWindow . center')
    window.title("MySejaterah")
    window.geometry("297x520")
    window.configure(bg="#05BDF7")

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
    canvas.create_text(
        14.0,
        92.0,
        anchor="nw",
        text="Password:",
        fill="#FFFFFF",
        font=("Roboto", 18 * -1)
    )

    canvas.create_text(
        10.0,
        47.0,
        anchor="nw",
        text="Username:",
        fill="#FFFFFF",
        font=("Roboto", 18 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        193.0,
        64.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_1.place(
        x=119.0,
        y=53.0,
        width=148.0,
        height=20.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        193.0,
        103.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        show="*",
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_2.place(
        x=119.0,
        y=92.0,
        width=148.0,
        height=20.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        193.0,
        151.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_3.place(
        x=119.0,
        y=140.0,
        width=148.0,
        height=20.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        193.0,
        194.0,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_4.place(
        x=119.0,
        y=183.0,
        width=148.0,
        height=20.0
    )

    #Ic No.
    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        193.0,
        395.0,
        image=entry_image_5
     )
    entry_5 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_5.place(
        x=119.0,
        y=385.0,
        width=148.0,
        height=20.0
    )

    #Phone number
    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        193.0,
        355.0,
        image=entry_image_6
    )
    entry_6 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_6.place(
        x=119.0,
        y=345.0,
        width=148.0,
        height=20.0
    )

    entry_image_7 = PhotoImage(
        file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(
        193.0,
        316.0,
        image=entry_image_7
    )
    entry_7 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_7.place(
        x=119.0,
        y=305.0,
        width=148.0,
        height=20.0
    )

    canvas.create_text(
        14.0,
        137.0,
        anchor="nw",
        text="Full Name:",
        fill="#FFFFFF",
        font=("Roboto", 17 * -1)
    )

    canvas.create_text(
        41.0,
        177.0,
        anchor="nw",
        text="Age:",
        fill="#FFFFFF",
        font=("Roboto", 18 * -1)
    )

    canvas.create_text(
        10.0,
        226.0,
        anchor="nw",
        text="Ocupation:",
        fill="#FFFFFF",
        font=("Roboto", 18 * -1)
    )

    canvas.create_text(
        30.0,
        269.0,
        anchor="nw",
        text="State:",
        fill="#FFFFFF",
        font=("Roboto", 18 * -1)
    )

    canvas.create_text(
        2.0,
        307.0,
        anchor="nw",
        text="Postal Code:",
        fill="#FFFFFF",
        font=("Roboto", 17 * -1)
    )

    canvas.create_text(
        2.0,
        345.0,
        anchor="nw",
        text="Phone No(+60):",
        fill="#FFFFFF",
        font=("Roboto", 13 * -1)
    )

    canvas.create_text(
        35.0,
        385.0,
        anchor="nw",
        text="IC No:",
        fill="#FFFFFF",
        font=("Roboto", 17 * -1)
    )

    canvas.create_text(
        108.0,
        8.0,
        anchor="nw",
        text="Sign up",
        fill="#FFFFFF",
        font=("Roboto Bold", 24 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=register,
        relief="flat"
    )
    button_1.place(
        x=116.0,
        y=430.0,
        width=128.0,
        height=34.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=backtomainmenu,
        relief="flat"
    )
    button_2.place(
        x=134.0,
        y=470.0,
        width=89.0,
        height=30.0
    )

    ocupation = ["1#Health-care Worker",
                 "2#Community Services",
                 "3#Energy, Food",
                 "4#Transportation",
                 "5#Students",
                 "6#Others or None"]

    dropdown = ttk.Combobox(
        window,
        width=37,
        value=(ocupation)
    )
    dropdown.place(
        x=113.0,
        y=225.5,
        width=160.0

    )

    state = ["Johor",
            "Kuala Lumpur",
            "Kedah",
            "Kelantan",
            "Labuan",
            "Malacca",
            "Negeri Sembilan",
            "Pahang",
            "Penang",
            "Perak",
            "Perlis",
            "Putrajaya",
            "Sabah",
            "Sarawak",
            "Selangor",
            "Terengganu"]

    statedropdown = ttk.Combobox(
        window,
        width=37,
        value=(state)
    )
    statedropdown.place(
        x=113.0,
        y=265.0,
        width=160.0
    )


    window.resizable(False, False)
    import tkinter as tk
    from tkinter import messagebox


    window.protocol("WM_DELETE_WINDOW", backtomainmenu)
    window.mainloop()
if __name__ == '__main__':
    register_user_gui()
