from Password_generator.generate_function import generate_password
import time
import os

while True:
    try:
        user_length = int(input("\ntype length password to generate( click ENTER to Exit ): "))
        
        print(generate_password(user_length))

    except ValueError:
        os.system("cls" if os.name == 'nt' else 'clear')
        print("Goodbye! :)")
        time.sleep(1)
        break