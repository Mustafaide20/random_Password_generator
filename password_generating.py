#🔐 Random Password Generator – Project Instructions

import random
import string
characters=string.ascii_letters+string.digits+string.punctuation
def password_generating(length):
 password=''.join(random.choice(characters) for _ in range(length))
 return password
if __name__=="__main__":
 password_length=input("enter password length (Max.12 ) \n")
 if password_length.isdigit():
  length=int(password_length)
 else:
  length=12
generated_Password=password_generating(length)
print("Ur generated Password is  " + generated_Password )