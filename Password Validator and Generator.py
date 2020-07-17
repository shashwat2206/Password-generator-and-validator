import string
import random
s1 = string.ascii_letters
s2 = string.ascii_lowercase
s3 = string.ascii_uppercase
s4 = string.digits
s5 = string.hexdigits
s6 = string.octdigits
s7 = string.punctuation
print ("Welcome to the password Generator")
while True :

    check = int(input(" Enter 1 to generate a new password and 2 to check the security of your password : "))
    if check == 1  :
            password_length = int(input(" Enter the the length of the password to be generated : "))
            s = []
            s.extend(list(s1))
            s.extend(list(s2))
            s.extend(list(s3))
            s.extend(list(s4))
            s.extend(list(s5))
            s.extend(list(s6))
            s.extend(list(s7))
            random.shuffle(s)
            generated_password = "".join(s[0:password_length])
            random.shuffle(s)
            ot_pass1 = "".join(s[0:password_length])
            random.shuffle(s)
            ot_pass2 = "".join(s[0:password_length])
            random.shuffle(s)
            ot_pass3 = "".join(s[0:password_length])
            random.shuffle(s)
            ot_pass4 = "".join(s[0:password_length])
            random.shuffle(s)
            ot_pass5 = "".join(s[0:password_length])
            random.shuffle(s)
            print("The Secure Password generated is  : " , generated_password)
            print("The few other secure password options are " , ot_pass1 , "||" , ot_pass2 , "||" , ot_pass3, "||" , ot_pass4 , "||" , ot_pass5 )
    elif check == 2 :
        def password_check(passwd): 
        
            SpecialSym =['$', '@', '#', '%'] 
            val = True
            
            if len(passwd) < 6: 
                print('length should be at least 8') 
                val = False
                
            if not any(char.isdigit() for char in passwd): 
                print('Your Password should some numbers ') 
                val = False
                
            if not any(char.isupper() for char in passwd): 
                print('Your Password should have at least one uppercase letter') 
                val = False
                
            if not any(char.islower() for char in passwd): 
                print('Your Password should have at least one lowercase letter') 
                val = False
                
            if not any(char in SpecialSym for char in passwd): 
                print('Your Password should have at least one of the symbols $@#') 
                val = False
            if val: 
                return val 
    def main(): 
        passwd = input("Please enter your password here : ")
        
        if (password_check(passwd)): 
            print(" Your Password is Secure") 
        else: 
            print("Your Password is not secure I") 

    if __name__ == '__main__': 
        main() 
