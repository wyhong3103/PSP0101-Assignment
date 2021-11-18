import sqlite3
import datetime

def eligibility_risk_priority_assigning(useroid):
    connector = sqlite3.connect("database.db")
    my_cursor = connector.cursor()
    my_cursor.execute("SELECT * FROM health_data WHERE useroid =" + str(useroid))
    health_data = my_cursor.fetchall()
    high_risk_disease = ["cardiovascular diseases", "heart disease", "diabetes", "cancer", "respiratory disease",
                         "lung disease", "chronic respiratory disease", "chronic lung disease",
                         "chronic kidney disease", "asthma", "obesity", "hyper-tension and cancer"]
    for i in health_data:
        if (str(i[3]).strip()).lower() in high_risk_disease:
            my_cursor.execute("""UPDATE person_data SET risk = :risk WHERE oid = :useroid""",
                              {"risk": "High", "useroid": useroid})
        else:
            my_cursor.execute("""UPDATE person_data SET risk = :risk WHERE oid = :useroid""",
                              {"risk": "Low", "useroid": useroid})
        if (i[0] == "y" or i[1] == "y" or i[2] == "y" or i[4] == "n"):
            my_cursor.execute("""UPDATE person_data SET
                eligibility = :eligibility

                WHERE oid = :oid""",
                              {
                                  "eligibility": "N",
                                  "oid": useroid
                              }
                              )
        else:
            my_cursor.execute("""UPDATE person_data SET
                eligibility = :eligibility

                WHERE oid = :oid""",
                              {
                                  "eligibility": "Y",
                                  "oid": useroid
                              }
                              )

    my_cursor.execute("SELECT * FROM person_data WHERE oid=" + str(useroid))
    details = my_cursor.fetchall()
    priority_dict = {
        "Health-Care Worker": 5,
        "Community Services": 4,
        "Energy, Food": 3,
        "Transportation": 2,
        "Students": 1,
        "Others or None": 1
    }
    for i in details:
        if i[3] >= 60 or i[6] == "Health-Care Worker":
            my_cursor.execute("""UPDATE person_data SET risk = :risk,priority = :prio WHERE oid = :useroid""",
                              {"risk": "High", "prio": 5, "useroid": useroid})
            break
        for keys in priority_dict:
            if i[6] == keys:
                my_cursor.execute("""UPDATE person_data SET priority = :prio WHERE oid = :useroid""",
                                  {"prio": priority_dict[keys], "useroid": useroid})
                break
            else:
                my_cursor.execute("""UPDATE person_data SET priority = :prio WHERE oid = :useroid""",
                                  {"prio": 1, "useroid": useroid})

    connector.commit()
    connector.close()

def auto_assignment(useroid):
    connector = sqlite3.connect("database.db")
    my_cursor = connector.cursor()
    my_cursor.execute("SELECT * FROM person_data WHERE oid=" + str(useroid))
    person_data = my_cursor.fetchall()
    for i in person_data:
        username = i[2]
        phone = i[4]
        ic = i[5]
        state = i[7]
        postcode = int(i[8])
        eligibility = i[9]
    if eligibility == "Y":
        my_cursor.execute(f"SELECT *,oid FROM vax_center")
        vax_center = my_cursor.fetchall()   
        if len(vax_center) == 0:
            return
        else:    
            postcode_diff = 0
            for i in vax_center:
                if i[1] == state:
                    if postcode_diff == 0:
                        postcode_diff = abs(postcode - int(i[2]))
                        vax_name = i[0]
                        vax_capacityperhour = i[3]
                        vax_centerid = i[-1]
                    elif postcode_diff != 0:
                        x = abs(postcode - int(i[2]))
                        if x < postcode_diff :
                            postcode_diff = x
                            vax_name = i[0]
                            vax_capacityperhour = i[3]
                            vax_centerid = i[-1]
                            if postcode_diff == 0:
                                break
                else:
                    if postcode_diff == 0:
                        postcode_diff = abs(postcode - int(i[2]))
                        vax_name = i[0]
                        vax_capacityperhour = i[3]
                        vax_centerid = i[-1]
                    elif postcode_diff != 0:
                        x = abs(postcode - int(i[2]))
                        if x < postcode_diff :
                            postcode_diff = x
                            vax_name = i[0]
                            vax_capacityperhour = i[3]
                            vax_centerid = i[-1]
                            if postcode_diff == 0:
                                break

            day_of_vaccine_obj = datetime.datetime.today() +datetime.timedelta(days = 1)
            day_of_vaccine = day_of_vaccine_obj.strftime("%d/%m/%y")
            time_to_vax_obj = datetime.time(hour = 10, minute = 0)
            time_to_vax = time_to_vax_obj.strftime("%H:%M")
            while True:
                my_cursor.execute(f"SELECT time FROM vax_appointment WHERE vaxcenterid = (?) AND date = (?)",(str(vax_centerid),day_of_vaccine))
                time_tup = my_cursor.fetchall()
                counter = 0
                for time in time_tup:
                    if time[0][0:2] == time_to_vax[0:2]:
                        counter += 1
                if counter < vax_capacityperhour:
                    if time_to_vax[0:2] in ["18","19","20","21","22","23","24","00","01","02","03","04","05","06","07","08","09"]:
                        day_of_vaccine_obj1 =datetime.datetime.strptime(day_of_vaccine,"%d/%m/%y")+ datetime.timedelta(days = 1)
                        day_of_vaccine = day_of_vaccine_obj1.strftime("%d/%m/%y")
                        time_to_vax_obj2 = datetime.time(hour = 10, minute = 0)
                        time_to_vax = time_to_vax_obj2.strftime("%H:%M")
                        continue
                    my_cursor.execute("INSERT INTO vax_appointment VALUES(:username, :userid, :phone, :ic ,:vaxcenter ,:vaxid, :date, :time , :confirmation)",{
                            "username" :username,
                            "userid" : useroid,
                            "phone" : phone,
                            "ic" : ic,
                            "vaxcenter" : vax_name,
                            "vaxid" : vax_centerid,
                            "date" : day_of_vaccine,
                            "time" : time_to_vax,
                            "confirmation" : "N"
                        })
                    my_cursor.execute("""UPDATE person_data SET notification = :notif WHERE oid = :useroid""",{"notif" : 1 , "useroid" : useroid})
                    break
                elif counter == vax_capacityperhour: 
                    time_to_vax_obj1 = datetime.datetime.strptime(time_to_vax,"%H:%M") + datetime.timedelta(hours = 1)
                    time_to_vax = time_to_vax_obj1.strftime("%H:%M")
                    if time_to_vax[0:2] in ["18","19","20","21","22","23","24","00","01","02","03","04","05","06","07","08","09"]:
                        day_of_vaccine_obj1 =datetime.datetime.strptime(day_of_vaccine,"%d/%m/%y")+ datetime.timedelta(days = 1)
                        day_of_vaccine = day_of_vaccine_obj1.strftime("%d/%m/%y")
                        time_to_vax_obj2 = datetime.time(hour = 10, minute = 0)
                        time_to_vax = time_to_vax_obj2.strftime("%H:%M")

    connector.commit()
    connector.close()




