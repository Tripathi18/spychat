from datetime import datetime
class Spy:
    def __init__(self,name,salutation,age,rating):

        self.name = salutation + " " + name
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status = None

spy = Spy('Ayush','Mr.',20,3.0)
class chatmessage:
    def __init__(self,message,st):
     self.msg = chatmessage
     self.time = datetime.now()
     self.send_by_me = st
