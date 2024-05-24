import random

lower_case = 'asdfghjklizxcvbnmqwertyuop'
upper_case = lower_case.upper()
nums = '0123456789'
chars = '-_.!?&+/#'
len = int(input("enter the lenght for your password: "))
pool = lower_case + upper_case + nums + chars
random_password = ''

#random_password = ''.join(random.choice(pool) for i in range(len)) 
for i in range(len):
  random_password += random.choice(pool)

print("your new password is "+ str(random_password))

