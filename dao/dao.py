from config.mysqlConnection import mydb
from flask import Response
mycursor = mydb.cursor()

def addCamera(userid):
    try:
        mycursor.execute("INSERT INTO Camera(userid) VALUES ({})".format(userid))
        mydb.commit()

        return "Insert success"
    except Exception:
        print(Exception)
        return "Insert fail"

def getCameraById(id):
    mycursor.execute("SELECT * FROM Camera WHERE CameraID =" + str(id))
    myresult = mycursor.fetchall()

    return myresult

def getCameraByUserId(userId):
    mycursor.execute("SELECT * FROM Camera WHERE UserID =" + str(userId))
    myresult = mycursor.fetchall()

    return myresult

def deleteCamera(id):
    try:
        mycursor.execute("DELETE from Camera WHERE CameraID =" + str(id))
        mydb.commit()

        return "Delete success"
    except Exception:
        print(Exception)
        return "Delete fail"

def createEmail(userId, notificationId, email):
    try:
        mycursor.execute("INSERT INTO Email(UserID, NotificationId, Email) VALUES ({}, {}, '{}')".format(userId, notificationId, email))
        mydb.commit()

        return "Insert success"
    except Exception:
        print(Exception)
        return "Insert fail"

def getEmailById(id):
    mycursor.execute("SELECT * FROM Email WHERE EmailID =" + str(id))
    myresult = mycursor.fetchall()

    return myresult

def getEmailByUserId(userId):
    mycursor.execute("SELECT * FROM Email WHERE UserID =" + str(userId))
    myresult = mycursor.fetchall()

    return myresult

def createEvent(camId, message, datetime):
    try:
        mycursor.execute("INSERT INTO Event(CameraID, Message, datetime) VALUES ({}, '{}', '{}')".format(camId, message, datetime))
        mydb.commit()

        return "Insert success"
    except Exception:
        print(Exception)
        return "Insert fail"

def getEventById(id):
    mycursor.execute("SELECT * FROM Event WHERE EventID =" + str(id))
    myresult = mycursor.fetchall()

    return myresult

def getEventByCamId(camId):
    mycursor.execute("SELECT * FROM Event WHERE CameraID =" + str(camId))
    myresult = mycursor.fetchall()

    return myresult

def getAllHelp():
    mycursor.execute("SELECT * FROM Help")
    myresult = mycursor.fetchall()

    return myresult

def getHelpById(id):
    mycursor.execute("SELECT * FROM Help WHERE HelpID =" + str(id))
    myresult = mycursor.fetchall()

    return myresult

def createCamHistory(camId, filePath, datatime):
    try:
        mycursor.execute("INSERT INTO CameraHistory(CameraID, FilePath, datetime) VALUES ({}, '{}', '{}')".format(camId, filePath, datatime))
        mydb.commit()

        return "Insert success"
    except Exception:
        print(Exception)
        return "Insert fail"

def getCamHistoryById(id):
    mycursor.execute("SELECT * FROM CameraHistory WHERE CameraHistoryID =" + str(id))
    myresult = mycursor.fetchall()

    return myresult

def getCamHistoryByCamId(camId):
    mycursor.execute("SELECT * FROM CameraHistory WHERE CameraID =" + str(camId))
    myresult = mycursor.fetchall()

    return myresult

def createNotification(camId, message, datetime):
    try:
        mycursor.execute("INSERT INTO Notification(CameraID, Message, datetime) VALUES ({}, '{}', '{}')".format(camId, message, datetime))
        mydb.commit()

        return "Insert success"
    except Exception:
        print(Exception)
        return "Insert fail"

def getNotificationById(id):
    mycursor.execute("SELECT * FROM Notification WHERE NotificationID =" + str(id))
    myresult = mycursor.fetchall()

    return myresult

def getNotificationByCamId(camId):
    mycursor.execute("SELECT * FROM Notification WHERE CameraID =" + str(camId))
    myresult = mycursor.fetchall()

    return myresult

def createUser(id, username, password, role):
    try:
        mycursor.execute("INSERT INTO User(UserID, UserName, Password, Role) VALUES ('{}','{}', '{}', '{}')".format(id, username, password, role))
        mydb.commit()

        return Response("Insert success", status=200, mimetype='application/json')
    except Exception:
        print(Exception)
        return Response("Insert fail", status=404, mimetype='application/json')

def getUserById(id):
    mycursor.execute("SELECT * FROM user WHERE UserID =" + str(id))
    myresult = mycursor.fetchall()

    return myresult

def getUser():
    mycursor.execute("SELECT * FROM User")
    myresult = mycursor.fetchall()
    return myresult

def getUserByUsername(username):
    mycursor.execute("SELECT * FROM user WHERE UserName ='{}'".format(username))
    myresult = mycursor.fetchall()

    return myresult

def updateUsername(username, id):
    try:
        mycursor.execute("UPDATE user SET UserName = '{}' WHERE UserID ='{}'".format(username, id))
        mydb.commit()

        #return "Update success"
        return Response("Update success", status=200, mimetype='application/json')
    except Exception:
        print(Exception)
        #return "Update fail"
        return Response("Update fail", status=404, mimetype='application/json')

def updateUserPassword(password, id):
    try:
        mycursor.execute("UPDATE User SET PassWord = '{}' WHERE UserID= '{}'".format(password, id))
        mydb.commit()

        return Response("Update success", status=200, mimetype='application/json')
    except Exception:
        print(Exception)
        return Response("Update fail", status=404, mimetype='application/json')

def deleteUser(id):
    try:
        mycursor.execute("DELETE from User WHERE UserID =" + str(id))
        mydb.commit()

        return "Delete success"
    except Exception:
        print(Exception)
        return "Delete fail"
