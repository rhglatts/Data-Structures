#Rebecca Glatts
#Project 3

#Problem 1

#(1)
shell_types = ['Puka', 'Cone', 'Driftwood', 'Sea Glass', 'Starfish']

#(2)
print("Enter the number of shells collected for each ")
counts = []

#for each shell in shell_types, output the shell name and ask the user for 
#how many they collected. then ad to counts[] array
for item in shell_types:
    print(item, ": ", end = "")
    count = int(input(""))
    counts.append(count)

#(3)
prices = [1.00, 1.50, 0.50, 2.00, 2.50]
shells = []
#for each shell name, count, and price, add them to a tuple and append the tuple to a list of tuples
for a, b, c in zip(shell_types, counts, prices):
    temp = (a, b, c)
    shells.append(temp)

#(4)
total_count = 0
worth = 0
#for each shell type, count, and price, add each count to the total and add the counts*prices to
#the total
for a, b, c in zip(shell_types, counts, prices):
    total_count += b
    worth += b*c
print("Total: ",total_count)
print("Total (worth) of sea shells:", worth)
print("")

#5
#prints barchart of how many shells were collected by each type
import numpy as np
import matplotlib.pyplot as plt
plt.bar(shell_types,counts)
plt.title('Shells Found in Hawaii')
plt.xlabel('Types of Shells')
plt.ylabel('Number of Shells Found')
plt.show()




#Problem 2
#(5)
#encrypts the password sent to it with a ceaser cipher with a shift of 10 in ASCII
def encrypt(password):
    encrypted = ""
    for x in password:
        temp = ord(x) + 10
        encrypted += chr(temp)
    return encrypted

#decrypts the password sent to it by decreasing the ASCII value by 10 and returning the 
#plaintext password
def decrypt(password):
    decrypted = ""
    for x in password:
        temp = ord(x) - 10
        decrypted += chr(temp)
    return decrypted
    
#(1)
user_names = {"Jesse", "John", "James", "Kim", "Anna"}
passwords = set()
users = {}
#for each username in the list, it asks the user to enter a password
for name in user_names:
    password = input("Enter password " + name + ": ")
    #it calls the encrypt method to encrypt the password before adding it to the
    #list of passwords and the dictionary of users+passwords
    passwords.add(encrypt(password))
    users[name] = (encrypt(password))

#prints sets and dictionary content of usernames, passwords, and users with their passwords
print("User names: ", user_names)
print("Passwords: ", passwords)
print("Users: ", users)


#(2)
#logs in users
def login():
    print("\nStarting login process...")
    global user_logged_in 
    user_logged_in = ""
    global logged_in
    logged_in = False
    while logged_in == False:
        username = input("Username: ")
        #if the username is in the list of users, it starts to ask for the password
        if username in users:

        #it gives the user 3 tries to enter the password. if they cannot, it
        #starts the login process over and asks for their username again
         for x in range(3):
            password = input("Password: ")
            #if the password matches what the user has as their password in the
            #database (after decrypting it) it sucessfully logs in the user
            if password == decrypt(users[username]):
                print("Sucessfully logged in!\n ")
                user_logged_in = username
                logged_in = True
                return
            print(f"Not a valid password. {2-x} attemps remaining.")
        print("Out of password attemps. Starting login process over.")
    print("Not a valid username")


#(3)
#resets the password for a user by first asking them to login, and then asking for
#a new password. Then it updates the key-value pair in the dictionary
def reset_password():
    print("Starting reset password: ")
    if logged_in == True:
        new_password = input("New password: ")
        users.update({user_logged_in:encrypt(new_password)})
    else:
        print("Not logged in.")

#(4)
#admin is the first person in the dictionary of users
admin = next(iter(users.keys()))

#adds a user if the person logged in is an admin. Asks for a unique username and corresponding password
#if the user logged in is not the admin, it does not add.
def add_user():
    print("Starting to add user:")
    if (user_logged_in == admin):
        new_username = input("Add the new user's username: ")
        if (new_username not in users):
            new_password = input("Add the new user's password: ")
            users.update({new_username : encrypt(new_password)})
        else:
            print("Usernames must be unique.")
    else:
        print("Not an admin; can't add a new user.")



def main():
    login()
    print("Before resetting password: ",users)
    reset_password()
    print("After resetting password: ",users)
    print("\nBefore add user:", users)
    add_user()
    print("After add user:", users)

main()
"""
Enter the number of shells collected for each 
Puka : 2
Cone : 36
Driftwood : 3 
Sea Glass : 14 
Starfish : 26
Total:  81
Total (worth) of sea shells: 150.5

Enter password Jesse: sadk 
Enter password James: gw3gr
Enter password Kim: tohjw
Enter password John: ojefhf
Enter password Anna: igwij
User names:  {'Jesse', 'James', 'Kim', 'John', 'Anna'}
Passwords:  {'}knu', 'sq\x81st', 'ytoprp', '~yrt\x81', 'q\x81=q|'}
Users:  {'Jesse': '}knu', 'James': 'q\x81=q|', 'Kim': '~yrt\x81', 'John': 'ytoprp', 'Anna': 'sq\x81st'}

Test 1:
Starting login process...
Username: Jesse
Password: sadk
Sucessfully logged in! 

Test 2: 
Starting login process...
Username: Jesse
Password: idk
Not a valid password. 2 attemps remaining.
Password: sadg 
Not a valid password. 1 attemps remaining.
Password: sadk
Sucessfully logged in!

Test 3: 
Starting login process...
Username: Jesse
Password: adjagoja
Not a valid password. 2 attemps remaining.
Password: sdogja
Not a valid password. 1 attemps remaining.
Password: ifjagoa
Not a valid password. 0 attemps remaining.
Out of password attemps. Starting login process over. 

Before resetting password:  {'Jesse': '}knu', 'James': 'q\x81=q|', 'Kim': '~yrt\x81', 'John': 'ytoprp', 'Anna': 'sq\x81st'}
Starting reset password:
New password: password
After resetting password:  {'Jesse': 'zk}}\x81y|n', 'James': 'q\x81=q|', 'Kim': '~yrt\x81', 'John': 'ytoprp', 'Anna': 'sq\x81st'}

Before add user: {'Jesse': 'zk}}\x81y|n', 'James': 'q\x81=q|', 'Kim': '~yrt\x81', 'John': 'ytoprp', 'Anna': 'sq\x81st'}
Starting to add user:
Add the new user's username: newuser
Add the new user's password: newpassword
After add user: {'Jesse': 'zk}}\x81y|n', 'James': 'q\x81=q|', 'Kim': '~yrt\x81', 'John': 'ytoprp', 'Anna': 'sq\x81st', 'newuser': 'xo\x81zk}}\x81y|n'}


"""