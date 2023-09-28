import requests
import random
import string
from colorama import Fore, Style, init

# colroama
init(autoreset=True)

# change "k=4" to the number that you want the usernames to be.
def generate_username():
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(characters, k=4))

# API
replit_api_url = 'https://replit.com/data/users/'

# Change the number in range(10000): to the number u want it to search.
for _ in range(10000):
    username = generate_username()
# hi there
    # API REQUEST
    response = requests.get(replit_api_url + username)
    if response.status_code == 404:
        # if user is not taken
        print(f"{Fore.GREEN}Username: {username} - Available{Style.RESET_ALL}")
        with open('valid.txt', 'a') as valid_file:
            valid_file.write(username + '\n')
    elif response.status_code == 200:
        # if the user is infact taken
        print(f"{Fore.RED}Username: {username} - Taken{Style.RESET_ALL}")
        with open('invalid.txt', 'a') as invalid_file:
            invalid_file.write(username + '\n')
    else:
        # Nut pls
        print(f"{Fore.RED}Username: {username} - Invalid{Style.RESET_ALL}")
# blah blah
print("Username checks completed.")
print("Available usernames saved to valid.txt")
print("Taken or invalid usernames saved to invalid.txt")
