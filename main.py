import wget
import os
import configparser

# Import Config
config = configparser.ConfigParser()
if (os.path.exists('config.ini')):
    config.read('config.ini')
    print("config.ini file was found")
    print('\n')
else:
    config.read(os.path.dirname(__file__) + os.path.sep + 'config.ini')

# Check for Links
if (os.path.exists('links.txt')):
    print("links.txt file was found")
    print('\n')
else:
    while True:
        print("Because there was no links.txt file found, this session will pull all links from the default list from GitHub.")
        print('\n')
        links_input = input("Do you wish to continue? (y/n) ")
        print('\n')
        parsed_links_input = links_input.lower()
        if parsed_links_input == 'y':
            default_link_list = 'https://github.com/Piblokto/FileSmasher.py/lists/list.txt'
            wget.download(default_link_list)
            print('The default link list has been downloaded')
            print('\n')
            break
        elif parsed_links_input == 'n':
            open('links.txt', 'w+')
            print("A links.txt file has been made in this directory...")
            print("Please refer to the documentation.")
            print('\n')
            exit()
        else:
            print("Unable to read response.")
            exit()

        break

# Download File Loop
def main():
    with open("links.txt", "r") as links:
        for line in links:
            stripped = line.strip()
            url = stripped
            filename = wget.download(url)
            print("File Downloaded")
            print('\n')

            os.remove(filename)
            print("File Deleted")
            print('\n')

# Parse loop from config
loopconf = config.get("Config", "loop")
parsedloopconf = loopconf.lower()

# Run depending on loop variable from config
if parsedloopconf == '1':
    print("Loop Config Loaded. The download will now repeat indefinitely, please close Python if you wish to stop.")
    print('\n')
    while True:
        main()
elif parsedloopconf == '0':
    print("Loop Config Loaded. The download will now repeat once.")
    print('\n')
    main()
    print("Download Finished")
    exit()
else:
    print("Unable to read loop configuration...")
    print("Please refer to the documentation.")
    print('\n')
    exit()