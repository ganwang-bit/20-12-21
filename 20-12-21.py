##with open('pi.txt') as file_object:
##    contents=file_object.read()
##    print(contents)
##with open('pi.txt') as file_object:
##    for line in file_object:
##        print(line.rstrip())
##with open("pi.txt") as file_object:
##    lines=file_object.readlines()
##for line in lines:
##    print(line.rstrip())
##pi_string=''.join(n.strip() for n in lines)
##print(pi_string)
##print(len(pi_string))
##with open("pi.txt",'a') as file:
##    file.write("python")
##try:
##    print(5/0)
##except ZeroDivisionError:
##    print("You can't divide by zero!")
##print("Give me two numbers, and I'll divide them.")
##print("Enter 'q' to quit.")
##while True:
##    first_number = input("\nFirst number: ")
##    if first_number == 'q':
##        break
##    second_number = input("Second number: ") 
##   try:
##        answer = int(first_number) / int(second_number)
##    except ZeroDivisionError:
##        print("You can't divide by 0!")
##   else:
##       print(answer)
##print("Give me two numbers, and I'll divide them.")
##print("Enter 'q' to quit.")
##while True:
##    first_number = input("\nFirst number: ")
##    if first_number == 'q':
##        break
##    else :
##        second_number = input("Second number: ")
##        if(int(second_number)!=0):
##            answer = int(first_number) / int(second_number)
##            print(answer)
##        else:
##            ZeroDivisionError: print("You can't divide by 0!")
#import json
#def get():
#    filename="username.json"
#    try:
#        with open(filename,'r') as f_obj:
#            username=json.load(f_obj)
#    except FileNotFoundError:
#        return None
#    else:
#        return username
#def greet():
#    username=get()
#    if username:
#        print("welcome back, "+str(username) +"!")
#    else:
#        username=input("what's your name?")
#        filename='username.json'
#        with open(filename,'w') as f_obj:
#            json.dump(username,f_obj)
#            print("we will remeber you come back, "+username +"!")
#greet()
#import json
#def get_stored_username():
#    """濡傛灉瀛樺偍浜嗙敤鎴峰悕锛屽氨鑾峰彇瀹"""
#    filename='username.json'
#    try:
#        with open(filename,'r') as o_obj:
#            username=json.load(o_obj)
#    except FileNotFoundError:
#        return None
#    else:
#        return username
#        
#def get_new_username():
#     """鎻愮ず鐢ㄦ埛杈撳叆鐢ㄦ埛鍚"""
#     username = input("What is your name? ")
#     filename = 'username.json'
#     with open(filename, 'w') as f_obj:
#         json.dump(username, f_obj)
#         return username
#def greet_user():
#    """闂鍊欑敤鎴凤紝骞舵寚鍑哄叾鍚嶅瓧"""
#username = get_stored_username()
#if username:
#    print("Welcome back, " + str(username) + "!")
#else:
#    username = get_new_username()
#    print("We'll remember you when you come back, " + username + "!")
#greet_user()
