import sqlite3
connector = sqlite3.connect("database.db")
my_cursor = connector.cursor()

my_cursor.execute("""CREATE TABLE person_data(
    username text,
    password text,
    name text,
    age int,
    phone_number text,
    ic_number text,
    occupation text,
    state text,
    postcode int,
    eligibility text,
    risk text,
    priority int,
    appointmentstatus text,
    appointmentdate text,
    appointmenttime text,
    appointmentlocation text,
    notification int
)""")

my_cursor.execute("""CREATE TABLE health_data(
    response1 text,
    response2 text,
    response3 text,
    response4 text,
    response5 text,
    useroid text
)""")

my_cursor.execute("""CREATE TABLE vax_center(
    vaxcentername text,
    state text,
    postcode text,
    capacityperhour int
)""")

my_cursor.execute("""CREATE TABLE vax_appointment(
    username text,
    useroid text,
    phone_number text,
    ic_number text,
    vaxcenter text,
    vaxcenterid text,
    date text,
    time text,
    confirmation text)
""")



connector.commit()
connector.close()