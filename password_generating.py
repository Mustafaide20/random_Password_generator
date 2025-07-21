
#🔐 Random Password Generator – Project Instructions


import string
import random
characters=string.ascii_letters+string.digits+string.punctuation
def password_generating(length) :             
 password=''.join(random.choice(characters) for _ in range(length))
 return password

if __name__ == "__main__":
    user_length = input("enter password length (max.12) \n")
    if user_length.isdigit():
        length = int(user_length)
    else:
        length = 12

    generated = password_generating(length)
    print("ur password is  " + generated)

