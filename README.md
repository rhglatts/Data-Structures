# Account Management System
Creates a list of usersnames that the user is then asked to enter a passowrd for each, creating a dictionary of usernames and passwords.

A function logs in the user. If the entered username is wrong, the process is restarted. If the username is right, but the password is wrong the user has 2 more 
trys to enter the correct password. If the password is entered wrong thrice, the login process is reset.

Another function allows a user to change their password if they are logged in, which updates the dictionary of users.

The admin user can use a function to add another user. Usernames must be unique.

The passowords are encrypted and decrypted before storing them in the dictionary and before using then. The encryption function uses a ceasar cipher to encrypt
before storing a password in the dictionary. A decryption function decrypts the password for comparison to an attempted login.
