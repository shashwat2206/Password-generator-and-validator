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

def password_checker():
    while True:
        password_length = int(input(" Enter the the length of the charecters to be generated in the password : "))
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
        print("The Secure Password generated is  : " , generated_password )
        print("The few other secure password options are " , ot_pass1 , "||" , ot_pass2 , "||" , ot_pass3, "||" , ot_pass4 , "||" , ot_pass5 )
if __name__ == "__main__":
    password_checker()