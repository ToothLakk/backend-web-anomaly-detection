class Camera:
    def __init__(self, cam_id, cam_name, cam_fps, cam_type):
        self.cam_id = cam_id
        self.cam_name = cam_name
        self.cam_fps = cam_fps
        self.cam_type = cam_type
    
class EmailList:
    def __init__(self, emailList_id, user_id, notification_id, email):
        self.emailList_id = emailList_id
        self.user_id = user_id
        self.notification_id = notification_id
        self.email = email
    
class Event:
    def __init__(self, notification_id, cam_id, emailList_id, message, datetime):
        self.notification_id = notification_id
        self.cam_id = cam_id
        self.emailList_id = emailList_id
        self.message = message
        self.datetime = datetime

class Help:
    def __init__(self, help_id, answer, question):
        self.help_id = help_id
        self.answer = answer
        self.question = question

class HistoryCamera:
    def __init__(self, historycamera_id, cam_id, filepath, datetime):
        self.historycamera_id = historycamera_id
        self.cam_id = cam_id
        self.filepath = filepath
        self.datetime = datetime


class Notification:
    def __init__(self, notification_id, cam_id, emailList_id, message):
        self.notification_id = notification_id
        self.cam_id = cam_id
        self.emailList_id = emailList_id
        self.message = message

class User:
    def __init__(self, user_id, user_name, password, role):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.role = role