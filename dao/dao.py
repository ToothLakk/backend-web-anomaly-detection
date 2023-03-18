from config.mysqlConnection import mydb


mycursor = mydb.cursor()

def get_dta_by_id(id):
    mycursor.execute("SELECT * FROM table1 WHERE id =" + str(id))

    myresult = mycursor.fetchall()

    return myresult

def innsert_to_tb1(name, age):
    try:
        print("INSERT INTO table1(name, age) VALUES ('{}', {})".format(name, age))
        mycursor.execute("INSERT INTO table1(name, age) VALUES ('{}', {})".format(name, age))
        mydb.commit()

        return "True"
    except Exception:
        print(Exception)
        return "False"