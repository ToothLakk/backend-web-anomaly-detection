from config.mysqlConnection import mydb

mycursor = mydb.cursor()

def addCamera(userid, cameraName):
    try:
        mycursor.execute("INSERT INTO Camera(UserID, CameraName, delete_flag) VALUES ({}, '{}', {})".format(userid, cameraName, 0))
        mydb.commit()

        return "Insert success"
    except Exception as e:
        print(e)
        return "Insert fail"

def getCameraById(id):
    mycursor.execute("SELECT * FROM Camera WHERE CameraID =" + str(id))
    myresult = mycursor.fetchall()

    return myresult

def getCameraByUserId(userId):
    mycursor.execute("SELECT * FROM Camera WHERE UserID =" + str(userId))
    myresult = mycursor.fetchall()

    return myresult

def updateCameraName(newName):
    try:
        mycursor.execute("UPDATE Camera SET CameraName = {} WHERE CameraID = {}".format(newName, id))
        mydb.commit()

        return "Update success"
    except Exception as e:
        print(e)
        return "Update fail"

def deleteCamera(id):
    try:
        mycursor.execute("UPDATE Camera SET delete_flag = {} WHERE CameraID = {}".format(1, id))
        mydb.commit()

        return "Update success"
    except Exception as e:
        print(e)
        return "Update fail"

def createEmail(userId, notificationId, email):
    try:
        mycursor.execute("INSERT INTO Email(UserID, NotificationId, Email) VALUES ({}, {}, '{}')".format(userId, notificationId, email))
        mydb.commit()

        return "Insert success"
    except Exception as e:
        print(e)
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
    except Exception as e:
        print(e)
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
    except Exception as e:
        print(e)
        return "Insert fail"

def getCamHistoryById(id):
    mycursor.execute("SELECT * FROM CameraHistory WHERE CameraHistoryID =" + str(id))
    myresult = mycursor.fetchall()

    return myresult

def getCamHistoryByCamId(camId):
    mycursor.execute("SELECT * FROM CameraHistory WHERE CameraID =" + str(camId))
    myresult = mycursor.fetchall()

    return myresult

def createNotification(userId, camId, eventId, message, datetime):
    try:
        if camId is not None and eventId is not None:
            mycursor.execute("INSERT INTO Notification(UserID, CameraID, EventID, Message, datetime) VALUES ({}, {}, {}, '{}', '{}')".format(userId, camId, eventId, message, datetime))
        else:
            if camId is None and eventId is None:
                mycursor.execute("INSERT INTO Notification(UserID, CameraID, EventID, Message, datetime) VALUES ({}, null, null, '{}', '{}')".format(userId, message, datetime))
            elif camId is None:
                mycursor.execute("INSERT INTO Notification(UserID, CameraID, EventID, Message, datetime) VALUES ({}, null, {}, '{}', '{}')".format(userId, eventId, message, datetime))
            else:
                mycursor.execute("INSERT INTO Notification(UserID, CameraID, EventID, Message, datetime) VALUES ({}, {}, null, '{}', '{}')".format(userId, camId, message, datetime))
            
        mydb.commit()

        return "Insert success"
    except Exception as e:
        print(e)
        return "Insert fail"

def getNotificationById(id):
    mycursor.execute("SELECT * FROM Notification WHERE NotificationID =" + str(id))
    myresult = mycursor.fetchall()

    return myresult

def getNotificationByUserId(userId):
    mycursor.execute("SELECT * FROM Notification WHERE UserID =" + str(userId))
    myresult = mycursor.fetchall()

    return myresult

def createUser(username, password, role):
    try:
        mycursor.execute("INSERT INTO User(UserName, Password, Role, delete_flag) VALUES ('{}', '{}', {}, {})".format(username, password, role, 0))
        mydb.commit()

        return "Insert success"
    except Exception as e:
        print(e)
        return "Insert fail"

def getUserById(id):
    mycursor.execute("SELECT * FROM User WHERE UserID =" + str(id))
    myresult = mycursor.fetchall()

    return myresult

def getUserByUsername(username):
    mycursor.execute("SELECT * FROM User WHERE UserName =" + str(username))
    myresult = mycursor.fetchall()

    return myresult

def updateUsername(id, username):
    try:
        mycursor.execute("UPDATE User SET UserName = '{}' WHERE UserID={}".format(username, id))
        mydb.commit()

        return "Update success"
    except Exception as e:
        print(e)
        return "Update fail"

def updateUserPassword(id, password):
    try:
        mycursor.execute("UPDATE User SET Password = '{}' WHERE UserID={}".format(password, id))
        mydb.commit()

        return "Update success"
    except Exception as e:
        print(e)
        return "Update fail"

def deleteUser(id):
    try:
        mycursor.execute("UPDATE User SET delete_flag = {} WHERE UserID = {}".format(1, id))
        mydb.commit()

        return "Delete success"
    except Exception as e:
        print(e)
        return "Delete fail"
