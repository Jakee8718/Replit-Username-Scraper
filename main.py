import requests
import random
import string
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Function to generate random 4-character username
def generate_username():
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(characters, k=4))

# URL for Replit API
replit_api_url = 'https://replit.com/data/users/'

# Generate 10000 random usernames
for _ in range(10000):
    username = generate_username()

    # Make API request to check if the username exists
    response = requests.get(replit_api_url + username)
    if response.status_code == 404:
        # Username is not taken
        print(f"{Fore.GREEN}Username: {username} - Available{Style.RESET_ALL}")
        with open('valid.txt', 'a') as valid_file:
            valid_file.write(username + '\n')
    elif response.status_code == 200:
        # Username is taken
        print(f"{Fore.RED}Username: {username} - Taken{Style.RESET_ALL}")
        with open('invalid.txt', 'a') as invalid_file:
            invalid_file.write(username + '\n')
    else:
        # Handle other response codes as invalid
        print(f"{Fore.RED}Username: {username} - Invalid{Style.RESET_ALL}")

print("Username checks completed.")
print("Available usernames saved to valid.txt")
print("Taken or invalid usernames saved to invalid.txt")
