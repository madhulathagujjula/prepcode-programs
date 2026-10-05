blocked = { "admin", "root", "user123"}
username = input("enter the username:")
if username not in blocked:
    print("username is allowed")
else:
    print("username is  blocked")    
