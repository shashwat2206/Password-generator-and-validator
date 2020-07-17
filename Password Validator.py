def password_check(passwd): 
    
    SpecialSym =['$', '@', '#', '%'] 
    val = True
    
    if len(passwd) < 6: 
        print('The length of your should be at least 8 charecters long') 
        val = False
        
        
    if not any(char.isdigit() for char in passwd): 
        print('Password should have at least one numeral') 
        val = False
        
    if not any(char.isupper() for char in passwd): 
        print('Password should have at least one uppercase letter') 
        val = False
        
    if not any(char.islower() for char in passwd): 
        print('Password should have at least one lowercase letter') 
        val = False
        
    if not any(char in SpecialSym for char in passwd): 
        print('Password should have at least one of the symbols $@#') 
        val = False
    if val: 
        return val 


def main(): 
	passwd = input("Please enter your password here : ")
	
	if (password_check(passwd)): 
		print("Password is valid") 
	else: 
		print("Invalid Password !!") 
		
if __name__ == '__main__': 
	main() 
