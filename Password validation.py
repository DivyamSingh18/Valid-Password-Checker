class short_pass(Exception):
    pass
class no_special_character(Exception):
    pass
class no_uppercase_letter(Exception):
    pass
class long_pass(Exception):
    pass
class no_digit_present(Exception):
    pass
class weak_pass_error(Exception):
    pass

list=["123","hello","abc","987","456","xyz","0123"]

def isnum(x):
    for i in x: 
        if i.isnumeric():
            global val
            val = 1
            break

def wkpass(x):
    for i in list:
        if x.find(i)>-1:
            return True
        elif x.find(i)==-1:
            return False


while True:
   
    try:
        pswd = input("\nEnter your password: ")
        val =0
        isnum(pswd)
        if len(pswd)<5:
            raise short_pass
        elif len(pswd)>30:
            raise long_pass    
        elif pswd.isalnum():
            raise no_special_character 
        elif pswd.islower():
            raise no_uppercase_letter   
        elif val == 0:
            raise no_digit_present  
        elif wkpass(pswd):
            raise weak_pass_error
        else:
            print("Your Password is Strong i.e.   ",pswd )
            break

    except short_pass:
        print("The password is too Short")
    except long_pass:
        print("The password is too long")    
    except no_special_character:
        print("Your password has no special character such as @, #, &, * etc.")    
    except no_uppercase_letter:
        print("Your password has no captial letter.") 
    except no_digit_present:
        print("Your password has no digits in it.") 
    except weak_pass_error:
        print("You have used a common password.") 
