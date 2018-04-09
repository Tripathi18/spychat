#my first program
from steganography.steganography import Steganography
#importing details from spydetails.py
from spydetails import spy,Spy,chatmessage
from datetime import datetime#importing date and time
#Select friend function
def select_friend():
    print "Select your friend"
    serial_no = 1
    for friend in friends:
        print str(serial_no) + ". " + friend.name
        serial_no = serial_no + 1
        user_selected_friend = input("Enter your choice::")
        user_selected_friend_index = user_selected_friend - 1
        return user_selected_friend_index
#send message function
def send_message():
    friend_choice = select_friend()#selecct friend by user
    original_image = raw_input("what is the name of the image? ")# image name
    output_path = "output.jpg"
    text = raw_input("what do you want to say:: ")#typing message inside image
    Steganography.encode(original_image,output_path,text)#encoding of messgae
    print "Message Encoded Successfully"
    new_chat = chatmessage(secret_text,True)#store message details
    friends[friend_choice].chats.append(new_chat)
    print "your secret message is ready"
#Read message function
def read_message():
    sender = select_friend()
    output_path = input("What is the name of the file? ")
    secret_text = Steganography.decode(output_path)#decoding of message
    print "The decoded message " + secret_text
    new_chat = chatmessage(secret_text,False)
    friends[sender].chats.append(new_chat)
    print "your secret message has been saved!"

# Adding Friend Function
def add_friend():
    frnd = Spy("","",0,0.0)
    firstname = raw_input("enter your friends name ")
    frnd.sal = raw_input("enter friend salutation:")
    frnd.age = input("enter age of friend::")
    frnd.rating = input("enter rating:")
    frnd.name = frnd.spy + " " + frndname
    if len(frnd.name) >= 2 and 12 < frnd.age < 60 and frnd.rating >= spy.rating:
        friends.append(frnd)
    else:
        print "Sorry enter Valid Details"
        return len(friends)

#Adding new status function
def add_status(c_status):
    if c_status != None:
        print "your current status is " + c_status
    else:
        print "You don\'t have any status currently"
    existing_status = raw_input("you want to select old status? (Y/N) ")
    if existing_status.upper() == "N":
        new_status = raw_input("enter your status")
        if len(new_status) > 0:
            updated_status = new_status
            print "Your Updated Status is " + updated_status
            STATUS_MESSAGE.append(updated_status)
            return updated_status
        else:
            print "enter valid status"
    elif existing_status.upper() == "Y":
        serial_no = 1
        for old_status in STATUS_MESSAGE:
            print str(serial_no) + ". " + old_status
            serial_no = serial_no + 1
        user_choice = input("enter your choice ")
        updated_status = STATUS_MESSAGE[user_choice - 1]
        print "Your Updated Status " + updated_status
        return updated_status
#Spy chat function
def spy_chat(spy_name,spy_age,spy_rating):
    current_status = None
    #set choice variable to -1
    choice = -1
    print 'Here are your option ' + spy_name
    #loop run until user choose exit option
    while choice != 0:
        #choice selection
        print 'Menu \n 1. Add a status \n 2. Add a Friend \n 3.Send a message \n 4.Read a message \n 0. Exit'
        choice = input('Enter your choice: ')
        if choice == 1:
            current_status = add_status(current_status)
        elif choice == 2:
            friend_no = 1
            new_friend = add_friend()
            print "You have "+str(new_friend)+ " number of friends"
            for f in friends:
                print str(friend_no) + ". " + f['name']
                friend_no = friend_no + 1
        elif choice == 3:
            send_message()
        elif choice == 4:
            read_message()
        elif choice == 5:
            print "will read message of user"
        elif choice == 0:
            print "Exit"
        #if input is wrong
        else:
            print "Enter Valid Input"
#welcome of user
f = datetime.now()
print f.strftime('%b %d %Y %H:%M:%S')
print "Hello!"
print 'Let\'s get started'
#friends name with details
frnd1 = Spy('ANIL','Mr.',20,5.3)
frnd2 = Spy('Pooja','Ms.',21,7.0)
friends = [frnd1,frnd2]#list of friends
# available status list
STATUS_MESSAGE = ['Sleeping','Available','Busy','At Work']
#asking user if user is already present or not
spy_reply=raw_input('Are you a new user? Y/N')
if spy_reply.upper() == 'N':
    #details of already present user
    print 'Welcome back..!! ' + spy.name+'. Your age is '+ str(spy.age)+' and your rating is '+str(spy.rating)
    #function calling
    spy_chat(spy.name,spy.age,spy.rating)
if spy_reply.upper() == 'Y':
    spy = Spy('','',0,0.0)
    spy.name=raw_input("what is your name?")
    #if user enter space in spy_name
    if spy.name.isspace():
        print 'enter valid name'
    #if user enter digit in spy_name
    elif spy.name.isdigit():
        print "enter valid name"
# Name condition
    elif len(spy.name) >= 2:
        print 'Welcome '+spy.name+ ' Glad to have back with us'
        spy.sal = raw_input("What should we call you (Mr. or Ms.)")
        if spy.sal == 'Mr.' or spy_salutation == 'Ms.':
            spy_name = spy.sal + " " + spy.name
            print "Alright " + spy_name + " I\'d like to know a little more about you before we proceed..."
            spy.age = input("enter your age")
    #Age condition and rating
            if 12<spy.age<60:
                spy.rating = input("enter spy rating::")
                if spy.rating > 4.5:
                    print "Great SPY"
                elif 3.5 < spy.rating <= 4.5:
                    print "A good one SPY"
                elif 2.5 <= spy.rating <= 3.5:
                    print "can do better"
                else:
                     print "NOT AT ALL A GOOD SPY WHAT ARE YOU DOING HERE Do Hard Wok"
                spy_is_online = True
                #integer converted into string using typecasting
                print "Authentication complete. Welcome " + spy_name + " age::" + str(spy.age) + " and rating of spy is::" + str(spy.rating)
            #function calling
                spy_chat(spy.name,spy.age,spy.rating)
            #if age is not in the range
            else:
                print "Sorry you cannnot become spy please enter valid age"
        #if user enter wrong salutation
        else:
            print "enter valid salutation"
    #if name has less than 2 character
    else:
        print "enter valid name"