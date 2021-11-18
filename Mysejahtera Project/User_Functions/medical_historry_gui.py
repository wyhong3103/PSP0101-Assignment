
def medical_history_register(useroid):
    from pathlib import Path
    from tkinter import Tk, Canvas,Button, PhotoImage
    from tkinter import ttk
    import  sqlite3
    from tkinter import messagebox
    import tkinter as tk

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./Assets Folder/medicalhistoryassets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def medical_historry_gui(useroid):
        global Q1Ans, Q2Ans, ans5, ans4, ans3, ans2, ans1, ans5, ans4, ans3, ans2, ans1, Q5Ans, Q4Ans, Q3Ans
        Q1Gui= Q1.get()
        Q2Gui= Q2.get()
        Q3Gui= Q3.get()
        Q4Gui= Q4.get()
        Q5Gui= Q5.get()

        if Q1Gui == "Yes":
            Q1Ans = "y"
        elif Q1Gui == "No":
            Q1Ans = "n"
        elif Q1Gui == "" :
            messagebox.showinfo("Please Complete the Question","Please Complete all the Question")
            return



        if Q2Gui == "Yes":
            Q2Ans = "y"
        elif Q2Gui == "No":
            Q2Ans = "n"
        elif Q2Gui == "" :
            messagebox.showinfo("Please Complete the Question","Please Complete all the Question")
            return

        if Q3Gui == "Yes":
            Q3Ans = "y"
        elif Q3Gui == "No":
            Q3Ans = "n"
        elif Q3Gui == "" :
            messagebox.showinfo("Please Complete the Question","Please Complete all the Question")
            return


        if Q4Gui in ("Cardiovascular Diseases","Heart Disease" ,"Diabetes","Cancer","Respiratory Disease",
           "Lung Disease", "Chronic Respiratory Disease", "Chronic Lung Disease",
          "Chronic Kidney Disease", "Asthma"," Obesity", "Hyper-Tension ,Cancer"):
            Q4Ans = Q4.get()

        elif Q4Gui == "Others":
            Q4Ans = "y"

        elif Q4Gui == "None":
            Q4Ans = "n"
        elif Q4Gui == "" :
            messagebox.showinfo("Please Complete the Question","Please Complete all the Question")
            return
        if Q5Gui == "Yes":
            Q5Ans = "y"
        elif Q5Gui == "No":
            Q5Ans = "n"
        elif Q5Gui == "" :
            messagebox.showinfo("Please Complete the Question","Please Complete all the Question")
            return


        connector = sqlite3.connect("database.db")
        my_cursor = connector.cursor()
        my_cursor.execute("SELECT * FROM health_data")
        record = my_cursor.fetchall()
        for i in record:
            if str(useroid) == str(i[-1]):
                my_cursor.execute("""UPDATE health_data SET 
                            response1 = :res1,
                            response2 = :res2,
                            response3 = :res3,
                            response4 = :res4,
                            response5 = :res5
                            WHERE useroid = :oid""",
                                  {
                                      "res1": Q1Ans,
                                      "res2": Q2Ans,
                                      "res3": Q3Ans,
                                      "res4": Q4Ans,
                                      "res5": Q5Ans,
                                      "oid": useroid
                                  })
                connector.commit()
                connector.close()
                from risk_priority_assigning import eligibility_risk_priority_assigning
                eligibility_risk_priority_assigning(useroid)
                messagebox.showinfo("UPDATED!", "Update Sucessfull")
                window.destroy()
                from Usermainmenu import usermainmenu
                usermainmenu(useroid)
                return

        my_cursor.execute(
            "INSERT INTO health_data VALUES(:response1 ,:response2 ,:response3 ,:response4 ,:response5, :useroid)", {
                "response1": Q1Ans,
                "response2": Q2Ans,
                "response3": Q3Ans,
                "response4": Q4Ans,
                "response5": Q5Ans,
                "useroid": useroid
            })
        connector.commit()
        connector.close()
        messagebox.showinfo("Register", "Register Successfully!")
        from risk_priority_assigning import  eligibility_risk_priority_assigning, auto_assignment
        eligibility_risk_priority_assigning(useroid)
        auto_assignment(useroid)
        window.destroy()
        from Userlogin import userlogin
        userlogin()





    window = Tk()
    window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='./icon2.png'))
    window.eval('tk::PlaceWindow . center')
    window.title("MySejaterah")
    window.geometry("297x420")
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
        33.00000000000003,
        9.999999999999972,
        anchor="nw",
        text="UPDATE MEDICAL HISTORY",
        fill="#FFFFFF",
        font=("Roboto Bold", 18 * -1)
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
        x=84.0,
        y=363.0,
        width=128.0,
        height=34.0
    )

    canvas.create_text(
        20.00000000000003,
        44.99999999999997,
        anchor="nw",
        text="Have you got any covid-19 symptoms?",
        fill="#FFFFFF",
        font=("Roboto Bold", 14 * -1)
    )

    canvas.create_text(
        25.00000000000003,
        100.99999999999997,
        anchor="nw",
        text="Have you had any close contact with \ncovid-19 patient?",
        fill="#FFFFFF",
        font=("Roboto Bold", 14 * -1)
    )

    canvas.create_text(
        25.00000000000003,
        165.99999999999997,
        anchor="nw",
        text="Have you had any allergy?",
        fill="#FFFFFF",
        font=("Roboto Bold", 14 * -1)
    )

    canvas.create_text(
        25.00000000000003,
        222.99999999999997,
        anchor="nw",
        text="Do you have any medical problems?",
        fill="#FFFFFF",
        font=("Roboto Bold", 14 * -1)
    )

    canvas.create_text(
        12.00,
        295.0,
        anchor="nw",
        text="Do you like to receive covid-19 vaccination",
        fill="#FFFFFF",
        font=("Roboto Bold", 13 * -1)
    )

    Q1 = ["Yes","No"]

    Q1 = ttk.Combobox(
        window,
        width=37,
        value=(Q1)
    )
    Q1.place(
        x=20.0,
        y=70.0,
        width=260.0
    )

    Q2 = ["Yes", "No"]

    Q2 = ttk.Combobox(
        window,
        width=37,
        value=(Q2)
    )
    Q2.place(
        x=20.0,
        y=140.0,
        width=260.0
    )
    Q3 = ["Yes", "No"]

    Q3 = ttk.Combobox(
        window,
        width=37,
        value=(Q3)
    )
    Q3.place(
        x=20.0,
        y=190.0,
        width=260.0
    )
    Q4 = ["None","Cardiovascular Diseases","Heart Disease" ,"Diabetes","Cancer","Respiratory Disease",
           "Lung Disease", "Chronic Respiratory Disease", "Chronic Lung Disease",
          "Chronic Kidney Disease", "Asthma"," Obesity", "Hyper-Tension ,Cancer","Others"]

    Q4 = ttk.Combobox(
        window,
        width=37,
        value=(Q4)
    )
    Q4.place(
        x=20.0,
        y=250.0,
        width=260.0
    )
    Q5 = ["Yes", "No"]

    Q5 = ttk.Combobox(
        window,
        width=37,
        value=(Q5)
    )
    Q5.place(
        x=20.0,
        y=320,
        width=260.0
    )



    window.resizable(False, False)
    import tkinter as tk
    from tkinter import messagebox

    def on_closing():
        messagebox.showinfo("Quit", "Please Complete The Question to Exit")

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()




