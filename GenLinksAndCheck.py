import random
import string
import requests
import time

#the generating function
def generate_invite_links(num_links, file_name):
    invite_links = []
    for _ in range(num_links):
        invite_code = 'https://discordapp.com/api/v6/invite/' + ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        invite_links.append(invite_code)
    with open(file_name, 'w') as file:
        file.write('\n'.join(invite_links))
#the invite checker function
def check_invite_acceptance(url):
    try:
        check_discord = requests.get(url)
    except Exception:
        raise Exception

    if check_discord.status_code == 404:
        return False
    elif check_discord.status_code == 200:
        return url
    else:
        return "Unknown, try again."


#the number of links you want to generate, you can change to whatever you like


num_links = 10
file_name = 'invite_links.txt'
generate_invite_links(num_links, file_name)

with open(file_name, 'r') as file:
    invite_links = file.read().splitlines()


# I added the time.sleep function so you dont get rate limited, you can change it if you want
for invite_link in invite_links:
    print(check_invite_acceptance(invite_link))
    time.sleep(3)
    x = check_invite_acceptance(invite_link)


#the if function is to add the working links in seperete txt file, beware that once you run it again all the links will get deleted from the txt file
    if x != False:
        with open('working invites.txt','w') as file:
            file.write(''.join(x)+'\n')