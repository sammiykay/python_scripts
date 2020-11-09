import re
import time
i = 0
while i < 20:
	print('x' * i)
	time.sleep(0.09)
	i += 1
print('''
		Password Validator
		''')
x = ''

while x != 'quit' :
	password = input('Enter Password: ')
	if password == '':
		print('input a password')
	elif len(password)< 8:
		print('length of the password must be greater than equals to 8')
	elif not re.search('[a-z]', password):
		print('Password must contain letters')
	elif not re.search('[A-Z]', password):
		print('Password must contain atleast a Capital letter')
	elif not re.search('[0-9]', password):
		print('Input atleast a number')
	elif not re.search('[$#@]', password):
		print('input a special character')
	elif re.search('\s', password):
		break
	else:
		print(f'Your password is valid, Your password is {password}')
		break


if x:
	print('The password not valid')


