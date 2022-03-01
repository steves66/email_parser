from re import M
import requests
from bs4 import BeautifulSoup




url = 'http://www.enron-mail.com/email/arnold-j/sent/'

search_string = "Re"

page = requests.get(url)
data = page.text
folder_soup = BeautifulSoup(data, 'html.parser')

list = []

open("data.txt", 'w')

for link in folder_soup.find_all('a'):
    if "Re_" in link.get('href'):
        list.append(link.get('href'))

for link in list:
    response = requests.get(url + link)
    page = BeautifulSoup(response.text, 'html.parser')
    text = page.get_text("\n")
    if search_string in text:
        messages = text.split(search_string, -1)
        final_reply = messages[len(messages) - 1].split("Subject: ", -1)
        reply_body = final_reply[len(final_reply) - 1].strip().partition("\n")[2]
        print(link)
        with open('data.txt', 'a') as f:
            f.write("Email: ")
            f.write(reply_body)
            f.write("\n\nReply: True\n\n")

    



