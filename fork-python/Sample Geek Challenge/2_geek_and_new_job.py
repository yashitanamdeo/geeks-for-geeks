# Password validation in Python
# using naive method

# Function to validate the password
def password_check(passwd):
	
	val = True
	
		
	if not any(char.isdigit() for char in passwd):
		#print('Password should have at least one numeral')
		val = False
		
	if not any(char.isupper() for char in passwd):
		#print('Password should have at least one uppercase letter')
		val = False
		
	if not any(char.islower() for char in passwd):
		#print('Password should have at least one lowercase letter')
		val = False
		
	if val:
		return val

# Main method
def main():
    T = int(input())
    for _ in range(T):
    	passwd = input()
    	if (password_check(passwd)):
    		print("YES")
    	else:
    		print("NO")
		
# Driver Code		
if __name__ == '__main__':
	main()
