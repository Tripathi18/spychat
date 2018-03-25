#my first program
#importing varibles from spydetails.py
from spydetails import spy_name,spy_age,spy_rating
def spy_chat(spy_name,spy_age,spy_rating):
    #set choice variable to -1
    choice = -1
    print 'Here are your option ' + spy_name
    #loop run until user choose exit option
    while choice != 0:
        #choice selection
        print 'Menu \n 1. Add a status \n 2. Add a Friend \n 0. Exit'
        choice = input('Enter your choice: ')
        if choice == 1:
            print "Status added and changed"
        elif choice == 2:
            print("Add person as a friend")
        elif choice == 0:
            print "Exit"
        #if input is wrong
        else:
            print "Enter Valid Input"
#welcome of user
print "Hello!"
print 'Let\'s get started'
#asking user if user is already present or not
spy_reply=raw_input('Are you a new user? Y/N')
if spy_reply.upper() == 'N':
    #details of already present user
    print 'Welcome back..!! ' + spy_name+'. Your age is '+ str(spy_age)+' and your rating is '+str(spy_rating)
    #function calling
    spy_chat(spy_name,spy_age,spy_rating)
if spy_reply.upper() == 'Y':
    spy_name=raw_input("what is your name?")
    #if user enter space in spy_name
    if spy_name.isspace():
        print 'enter valid name'
    #if user enter digit in spy_name
    elif spy_name.isdigit():
        print "enter valid name"
# Name condition
    elif len(spy_name) >= 2:
        print 'Welcome '+spy_name+ ' Glad to have back with us'
        spy_salutation = raw_input("What should we call you (Mr. or Ms.)")
        if spy_salutation == 'Mr.' or spy_salutation == 'Ms.':
            spy_name = spy_salutation + " " + spy_name
            print "Alright " + spy_name + " I\'d like to know a little more about you before we proceed..."
            spy_age = input("enter your age")
    #Age condition and rating
            if 12<spy_age<60:
                spy_rating = input("enter spy rating::")
                if spy_rating > 4.5:
                    print "Great SPY"
                elif 3.5 < spy_rating <= 4.5:
                    print "A good one SPY"
                elif 2.5 <= spy_rating <= 3.5:
                    print "can do better"
                else:
                     print "NOT AT ALL A GOOD SPY WHAT ARE YOU DOING HERE" \
                           " Do Hard Wok"
                spy_is_online = True
                #integer converted into string using typecasting
                print "Authentication complete. Welcome " + str(spy_name) + " age::" + str( spy_age) + " and rating of spy is::" + str(spy_rating)
            #function calling
                spy_chat(spy_name, spy_age, spy_rating)
            #if age is not in the range
            else:
                print "Sorry you cannnot become spy please enter valid age"
        #if user enter wrong salutation
        else:
            print "enter valid salutation"
    #if name has less than 2 character
    else:
        print "enter valid name"