#Rebecca Glatts
#Project 3


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
