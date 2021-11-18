

def view_all_user ():
    from pathlib import Path
    from tkinter import Tk, Canvas, Button, PhotoImage
    import sqlite3
    from passlib.hash import pbkdf2_sha256
    from tkinter import ttk
    import tkinter
    from tkinter import messagebox
    import tkinter as tk

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./Admin Assets Folder/View_all_user_assets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def back():
        window8.destroy()
        from admin_view_user_type_Menu import admin_view_user_type
        admin_view_user_type()

    def idbox(window):
       from IdBox import idbox_gui
       (idbox_gui(window))

    window8 = Tk()
    window8.tk.call('wm', 'iconphoto', window8._w, tk.PhotoImage(file='./icon2.png'))
    window8.eval('tk::PlaceWindow . center')
    window8.geometry("167x340")
    window8.configure(bg="#22AFFF")
    window8.title("MySejaterah")

    connector = sqlite3.connect("database.db")
    my_cursor = connector.cursor()
    my_cursor.execute("SELECT *,oid FROM person_data")


    
    
    canvas = Canvas(
        window8,
        bg="#22AFFF",
        height=371,
        width=420,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    tree = ttk.Treeview(window8)
    tree["show"]="headings"

    windowscroll = ttk.Scrollbar(window8, orient="vertical", command=tree.yview)
    windowscroll.place(x=150, y=0,height=200 + 20)

    tree.configure(yscrollcommand=windowscroll.set)


    # number of collums
    tree["column"] = ("Oid","Name")

    # Assigning size and Width
    tree.column("Oid",width=30, minwidth=30, anchor=tkinter.CENTER)
    tree.column("Name", width=120, minwidth=100, anchor=tkinter.CENTER)
    #tree.column("Age", width=30, minwidth=30, anchor=tkinter.CENTER)
    #tree.column("Occupation", width=150, minwidth=100, anchor=tkinter.CENTER)
    #tree.column("Risk", width=50, minwidth=30, anchor=tkinter.CENTER)
    #tree.column("Appointment Status", width=150, minwidth=30, anchor=tkinter.CENTER)
    #tree.column("Appointment Date", width=150, minwidth=30, anchor=tkinter.CENTER)

    # Assining the Heading
    tree.heading("Oid",text="ID", anchor=tkinter.CENTER)
    tree.heading("Name",text="Name", anchor=tkinter.CENTER)
    #tree.heading("Age", text="Age", anchor=tkinter.CENTER)
    #tree.heading("Occupation",text="Occupation", anchor=tkinter.CENTER)
    #tree.heading("Risk",text="Risk", anchor=tkinter.CENTER)
    #tree.heading("Postcode", text="Postcode", anchor=tkinter.CENTER)
    #tree.heading("Appointment Status", text="Appointment Status", anchor=tkinter.CENTER)
    #tree.heading("Appointment Date",text="Appointment Date", anchor=tkinter.CENTER)

    i = 0
    for ro in my_cursor:
        tree.insert('', i, text="", values=(ro[-1], ro[2], ro[3], ro[6],ro[10],ro[8],ro[12],ro[13]))
        i = i + 1
        tree.pack()

    tree.place(x=0, y=0)












    canvas.place(x=0, y=0)
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=back,
        relief="flat"
    )
    button_1.place(
        x=35.0,
        y=280.0,
        width=91.0,
        height=35.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: idbox(window8),
        relief="flat"
    )
    button_2.place(
        x=25.0,
        y=240.0,
        width=120.0,
        height=34.0
    )

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

 
    window8.protocol("WM_DELETE_WINDOW", back)
    #window.resizable(False, False)
    window8.mainloop()




if __name__ == '__main__':
    view_all_user()

def view_by_risk():
    from pathlib import Path
    from tkinter import Tk, Canvas, Button, PhotoImage,messagebox
    import sqlite3
    from passlib.hash import pbkdf2_sha256
    from tkinter import ttk
    import tkinter
    import tkinter as tk
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./Admin Assets Folder/View_all_user_assets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def back():
        window.destroy()
        from admin_view_user_type_Menu import admin_view_user_type
        admin_view_user_type()

    def idbox(window):
       from IdBox import idbox_gui
       (idbox_gui(window))

    window = Tk()
    window.eval('tk::PlaceWindow . center')
    window.geometry("385x400")
    window.configure(bg="#22AFFF")
    window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='./icon2.png'))
    window.title("MySejaterah")

    connector = sqlite3.connect("database.db")
    my_cursor = connector.cursor()
    my_cursor.execute("SELECT *,oid FROM person_data ORDER BY risk ASC")


    canvas = Canvas(
        window,
        bg="#22AFFF",
        height=371,
        width=420,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    tree = ttk.Treeview(window)
    tree["show"] = "headings"

    windowscroll = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    windowscroll.place(x=370, y=0, height=200 + 20)

    tree.configure(yscrollcommand=windowscroll.set)

    # number of collums
    tree["column"] = ("Oid", "Name", "Occupation", "Risk")

    # Assigning size and Width
    tree.column("Oid", width=50, minwidth=10, anchor=tkinter.CENTER)
    tree.column("Name", width=120, minwidth=100, anchor=tkinter.CENTER)
    tree.column("Occupation", width=150, minwidth=100, anchor=tkinter.CENTER)
    tree.column("Risk", width=50, minwidth=30, anchor=tkinter.CENTER)

    # Assining the Heading
    tree.heading("Oid", text="ID", anchor=tkinter.CENTER)
    tree.heading("Name", text="Name", anchor=tkinter.CENTER)
    tree.heading("Occupation", text="Occupation", anchor=tkinter.CENTER)
    tree.heading("Risk", text="Risk", anchor=tkinter.CENTER)

    i = 0
    for ro in my_cursor:
        tree.insert('', i, text="", values=(ro[-1], ro[2], ro[6], ro[10]))
        i = i + 1
        tree.pack()

    tree.place(x=0, y=0)

    canvas.place(x=0, y=0)
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=back,
        relief="flat"
    )
    button_1.place(
        x=135.0,
        y=326.0,
        width=91.0,
        height=35.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: idbox(window),
        relief="flat"
    )
    button_2.place(
        x=125.0,
        y=280.0,
        width=120.0,
        height=34.0
    )

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

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            window.quit()
            window.destroy()

    window.protocol("WM_DELETE_WINDOW", back)
    window.resizable(True, True)
    window.mainloop()
    connector.close()


if __name__ == '__main__':
    view_by_risk()

def view_by_postcode():
    from pathlib import Path
    from tkinter import Tk, Canvas, Button, PhotoImage,messagebox
    import sqlite3
    from passlib.hash import pbkdf2_sha256
    from tkinter import ttk
    import tkinter
    import tkinter as tk
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./Admin Assets Folder/View_all_user_assets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def back():
        window.destroy()
        from admin_view_user_type_Menu import admin_view_user_type
        admin_view_user_type()

    def idbox(window):
       from IdBox import idbox_gui
       (idbox_gui(window))


    window = Tk()
    window.eval('tk::PlaceWindow . center')
    window.geometry("380x350")
    window.configure(bg="#22AFFF")
    window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='./icon2.png'))
    window.title("MySejaterah")

    connector = sqlite3.connect("database.db")
    my_cursor = connector.cursor()
    my_cursor.execute("SELECT *,oid FROM person_data ORDER BY postcode DESC")

    canvas = Canvas(
        window,
        bg="#22AFFF",
        height=371,
        width=420,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    tree = ttk.Treeview(window)
    tree["show"] = "headings"

    # number of collums
    tree["column"] = ("Oid", "Name", "Age", "Postcode")

    windowscroll = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    windowscroll.place(x=365, y=0, height=200 + 20)

    tree.configure(yscrollcommand=windowscroll.set)

    # Assigning size and Width
    tree.column("Oid", width=50, minwidth=10, anchor=tkinter.CENTER)
    tree.column("Name", width=120, minwidth=100, anchor=tkinter.CENTER)
    tree.column("Age", width=50, minwidth=30, anchor=tkinter.CENTER)
    tree.column("Postcode", width=150, minwidth=100, anchor=tkinter.CENTER)


    # Assining the Heading
    tree.heading("Oid", text="ID", anchor=tkinter.CENTER)
    tree.heading("Name", text="Name", anchor=tkinter.CENTER)
    tree.heading("Age", text="Age", anchor=tkinter.CENTER)
    tree.heading("Postcode", text="Postcode", anchor=tkinter.CENTER)


    i = 0
    for ro in my_cursor:
        tree.insert('', i, text="", values=(ro[-1], ro[2], ro[3], ro[8]))
        i = i + 1
        tree.pack()
    
    tree.place(x=0, y=0)

    canvas.place(x=0, y=0)
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=back,
        relief="flat"
    )
    button_1.place(
        x=135.0,
        y=280.0,
        width=91.0,
        height=35.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: idbox(window),
        relief="flat"
    )
    button_2.place(
        x=125.0,
        y=240.0,
        width=120.0,
        height=34.0
    )

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
    connector.close()

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            window.quit()
            window.destroy()

    window.protocol("WM_DELETE_WINDOW", back)
    window.resizable(True, True)
    window.mainloop()


if __name__ == '__main__':
    view_by_postcode()


def view_by_priority():
    from pathlib import Path
    from tkinter import Tk, Canvas, Button, PhotoImage,messagebox
    import sqlite3
    from passlib.hash import pbkdf2_sha256
    from tkinter import ttk
    import tkinter
    import tkinter as tk
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./Admin Assets Folder/View_all_user_assets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def back():
        window.destroy()
        from admin_view_user_type_Menu import admin_view_user_type
        admin_view_user_type()

    def idbox(window):
       from IdBox import idbox_gui
       (idbox_gui(window))


    window = Tk()
    window.geometry("405x400")
    window.eval('tk::PlaceWindow . center')
    window.configure(bg="#22AFFF")
    window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='./icon2.png'))
    window.title("MySejaterah")

    connector = sqlite3.connect("database.db")
    my_cursor = connector.cursor()
    my_cursor.execute("SELECT *,oid FROM person_data ORDER BY priority DESC")

    canvas = Canvas(
        window,
        bg="#22AFFF",
        height=371,
        width=420,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    tree = ttk.Treeview(window)
    tree["show"] = "headings"
    windowscroll = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    windowscroll.place(x=390, y=0, height=200 + 20)

    tree.configure(yscrollcommand=windowscroll.set)
    # number of collums
    tree["column"] = ("Oid", "Username", "Occupation", "Priority")

    # Assigning size and Width
    tree.column("Oid", width=50, minwidth=10, anchor=tkinter.CENTER)
    tree.column("Username", width=120, minwidth=100, anchor=tkinter.CENTER)
    tree.column("Occupation", width=150, minwidth=100, anchor=tkinter.CENTER)
    tree.column("Priority", width=70, minwidth=30, anchor=tkinter.CENTER)

    # Assining the Heading
    tree.heading("Oid", text="ID", anchor=tkinter.CENTER)
    tree.heading("Username", text="Username", anchor=tkinter.CENTER)
    tree.heading("Occupation", text="Occupation", anchor=tkinter.CENTER)
    tree.heading("Priority", text="Priority", anchor=tkinter.CENTER)

    i = 0
    for ro in my_cursor:
        tree.insert('', i, text="", values=(ro[-1], ro[2], ro[6], ro[11]))
        i = i + 1
        tree.pack()

    tree.place(x=0, y=0)

    canvas.place(x=0, y=0)
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=back,
        relief="flat"
    )
    button_1.place(
        x=150.0,
        y=326.0,
        width=91.0,
        height=35.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: idbox(window),
        relief="flat"
    )
    button_2.place(
        x=150.0,
        y=280.0,
        width=120.0,
        height=34.0
    )

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
    connector.close()
    

    window.protocol("WM_DELETE_WINDOW", back)
    window.resizable(True, True)
    window.mainloop()


if __name__ == '__main__':
    view_by_priority()
