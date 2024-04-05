import os
import requests
from bs4 import BeautifulSoup

# URL of the Daggerverse listing page
url = 'https://daggerverse.dev/'

# Path to the file where known modules will be stored
known_modules_file_path = 'known_modules.txt'

def fetch_modules():
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Assuming module URLs are contained in 'a' tags
        module_urls = {link.get('href') for link in soup.find_all('a') if '/mod/' in link.get('href')}
        return module_urls
    else:
        print("Failed to fetch modules.")
        return set()

def read_known_modules(file_path):
    try:
        with open(file_path, 'r') as file:
            return {line.strip() for line in file}
    except FileNotFoundError:
        return set()

def write_known_modules(file_path, modules):
    with open(file_path, 'w') as file:
        for module in sorted(modules):
            file.write(module + '\n')

def send_discord_notification(new_modules):
    webhook_url = os.getenv('DISCORD_WEBHOOK_URL')
    if not webhook_url:
        print("Discord webhook URL is not set.")
        return
    message = f"New Daggerverse modules detected: {', '.join(new_modules)}"
    data = {"content": message}
    response = requests.post(webhook_url, json=data)
    print(f"Discord notification sent with status code {response.status_code}")

# Main script execution starts here
current_modules = fetch_modules()
known_modules = read_known_modules(known_modules_file_path)

new_modules = current_modules - known_modules

if new_modules:
    print("New modules detected:")
    for module in new_modules:
        print(module)
    # Send a Discord notification for new modules
    send_discord_notification(new_modules)

    # Update the known modules list with the current list
    known_modules.update(new_modules)
    write_known_modules(known_modules_file_path, known_modules)
else:
    print("No new modules detected.")