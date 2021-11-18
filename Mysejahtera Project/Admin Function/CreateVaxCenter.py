def create_vax_center():
    from pathlib import Path
    from tkinter import Tk, Canvas, Entry,  Button, PhotoImage
    from tkinter import ttk
    import sqlite3
    from tkinter import messagebox
    import tkinter as tk

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./Admin Assets Folder/CreateVaxCenterAssets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def back():
        window.destroy()
        from AdminMainMenu import adminmainmenu
        adminmainmenu()

    def createvax():
        global capacityperhour, postcode, state, state_int
        vac_name_gui= entry_1.get()
        vac_postcode = entry_2.get()
        stateGui =statedropdown.get()
        capacity_gui = entry_4.get()



        while True:
            vaxcentername = (vac_name_gui)
            postcode_v = (vac_postcode)
            if int(postcode_v) >= 1000 and int(postcode_v) <= 100000:
                postcode = postcode_v
            else:
                messagebox.showerror("Error", "Invalid Postcode")
                window.destroy()
                create_vax_center()
                continue
            state_dict = {
                1: "Johor",
                2: "Kuala Lumpur",
                3: "Kedah",
                4: "Kelantan",
                5: "Labuan",
                6: "Malacca",
                7: "Negeri Sembilan",
                8: "Pahang",
                9: "Penang",
                10: "Perak",
                11: "Perlis",
                12: "Putrajaya",
                13: "Sabah",
                14: "Sarawak",
                15: "Selangor",
                16: "Terengganu"


            }
            try:

                if stateGui == "Johor":
                    state_int = 1
                elif stateGui == "Kuala Lumpur":
                    state_int = 2
                elif stateGui == "Kedah":
                    state_int = 3
                elif stateGui == "Kelantan":
                    state_int = 4
                elif stateGui == "Labuan":
                    state_int = 5
                elif stateGui == "Malacca":
                    state_int = 6
                elif stateGui == "Negeri Sembilan":
                    state_int = 7
                elif stateGui == "Pahang":
                    state_int = 8
                elif stateGui == "Penang":
                    state_int = 9
                elif stateGui == "Perak":
                    state_int = 10
                elif stateGui == "Perlis":
                    state_int = 11
                elif stateGui == "Putrajaya":
                    state_int = 12
                elif stateGui == "Sabah":
                    state_int = 13
                elif stateGui == "Sarawak":
                    state_int = 14
                elif stateGui == "Selangor":
                    state_int = 15
                elif stateGui == "Terengganu":
                    state_int = 16




                state_v = (state_int)
                if state_v in state_dict:
                    state = state_dict[state_v]
            except (ValueError, TypeError):
                messagebox.showerror("Select state")

            capacityperhour_v = (capacity_gui)
            if int(capacityperhour_v) <= 2000:
                capacityperhour = capacityperhour_v
            else:
                messagebox.showerror("Error", "Invalid Number Hours")
                window.destroy()
                create_vax_center()
                continue
            break

        connector = sqlite3.connect("database.db")
        my_cursor = connector.cursor()
        my_cursor.execute("INSERT INTO vax_center VALUES(:centername ,:state ,:postcode, :capacityperhour)", {
            "centername": vaxcentername,
            "state": state,
            "postcode": postcode,
            "capacityperhour": capacityperhour
        })
        connector.commit()
        connector.close()
        messagebox.showinfo("Vaccination Center", "Vax Center Added Sucessfully")

    window = Tk()
    window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='./icon2.png'))
    window.eval('tk::PlaceWindow . center')
    window.geometry("297x361")
    window.configure(bg="#05BDF7")
    window.title("MySejaterah")

    canvas = Canvas(
        window,
        bg="#05BDF7",
        height=361,
        width=297,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_text(
        7.000000000000028,
        55.0,
        anchor="nw",
        text="Center Name:",
        fill="#FFFFFF",
        font=("Roboto", 14 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        193.00000000000003,
        64.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_1.place(
        x=119.00000000000003,
        y=53.0,
        width=148.0,
        height=20.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        193.00000000000003,
        111.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_2.place(
        x=119.00000000000003,
        y=100.0,
        width=148.0,
        height=20.0
    )

    #entry_image_3 = PhotoImage(
        #file=relative_to_assets("entry_3.png"))
    #entry_bg_3 = canvas.create_image(
        #193.00000000000003,
        #156.0,
        #image=entry_image_3
    #)
    #entry_3 = Entry(
        #bd=0,
        #bg="#FFFFFF",
        #highlightthickness=0
    #)
    #entry_3.place(
        #x=119.00000000000003,
        #y=145.0,
        #width=148.0,
        #height=20.0
    #)

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        193.00000000000003,
        214.0,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#FFFFFF",
        highlightthickness=0
    )
    entry_4.place(
        x=119.00000000000003,
        y=203.0,
        width=148.0,
        height=20.0
    )

    canvas.create_text(
        33.00000000000003,
        146.0,
        anchor="nw",
        text="State:",
        fill="#FFFFFF",
        font=("Roboto", 18 * -1)
    )

    canvas.create_text(
        8.000000000000028,
        100.0,
        anchor="nw",
        text="Postal Code:",
        fill="#FFFFFF",
        font=("Roboto", 15 * -1)
    )

    canvas.create_text(
        64.00000000000003,
        9.0,
        anchor="nw",
        text="Add Vax Center",
        fill="#FFFFFF",
        font=("Roboto Bold", 24 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=createvax,
        relief="flat"
    )
    button_1.place(
        x=84.00000000000003,
        y=260.0,
        width=128.0,
        height=34.0
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
        x=104.00000000000003,
        y=305.0,
        width=89.0,
        height=31.0
    )

    canvas.create_text(
        19.00000000000003,
        193.0,
        anchor="nw",
        text="Capacity",
        fill="#FFFFFF",
        font=("Roboto", 18 * -1)
    )

    canvas.create_text(
        19.00000000000003,
        210.0,
        anchor="nw",
        text="Per Hour:",
        fill="#FFFFFF",
        font=("Roboto", 18 * -1)
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
        x=119.00000000000003,
        y=145.0,
        width=148.0,
        height=20.0
    )

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            window.quit()
            window.destroy()

    window.protocol("WM_DELETE_WINDOW", back)
    window.resizable(False, False)
    window.mainloop()

if __name__ == '__main__':
    create_vax_center()
