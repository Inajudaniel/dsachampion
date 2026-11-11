def create_password():

    create = input("create your password, not less than 8 characters: ")
    verify = input("verify your password: ")
    if create < 8:
        print("weak password")
    else:
        print("strong password")
    if create == verify:
        print("password was successfully created")

def password_check(password):
    #return create_password()
    password = len(create) >= 8
    attempt = 0
    
    while attempt < 3:
        password_check = input("Enter your Password: ")
        if password == password_check:
            print("Access Granted")
            break
        else:
            print("incorrect password")
            attempt += 1
            remaining_attempts = 3 - attempt 
            if attempt < 3:
                print(remaining_attempts, "Attempts Remaining", )
            
    if attempt == 3:
        print("account blocked") 
        return create
    result = create_password
        
        
    

password_check()
create_password()