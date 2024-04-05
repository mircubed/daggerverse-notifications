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

# Main script execution starts here
current_modules = fetch_modules()
known_modules = read_known_modules(known_modules_file_path)

# Find new modules by comparing the current list to the known list
new_modules = current_modules - known_modules

if new_modules:
    print("New modules detected:")
    for module in new_modules:
        print(module)
    # Update the known modules list with the current list
    known_modules.update(new_modules)
    write_known_modules(known_modules_file_path, known_modules)
else:
    print("No new modules detected.")