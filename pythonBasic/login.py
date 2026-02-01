try:
    username=input("Enter the username")
    if username=="":
        print("username is not empty")
    print(f"welcome {username}")
except ValueError  as e:
    print("Error",e)