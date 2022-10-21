import json
import wget
import requests as r
import random

user_agents = [ 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 
	'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148', 
	'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36' 
] 
headers_list = [{ 
	'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"', 
	'upgrade-insecure-requests': '1', 
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36', 
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
	'sec-fetch-site': 'cross-site', 
	'sec-fetch-mode': 'navigate', 
	'sec-fetch-user': '?1', 
	'sec-fetch-dest': 'document', 
	'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7', 
    'accept-encoding': 'gzip, deflate, br',
    'device-memory': '8',
    'downlink': '10',
    'dpr': '1.5',
    'ect': '4g',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua-arch': 'x86',
    'sec-ch-ua-platform': 'Windows',
    'sec-ch-ua-platform-version': '10.0.0',
    'viewport-width': '853',
} # , {...} 
]


# Getting the data from the json file
with open('./test/manifest.json', 'r') as file:
    raw_txt = file.read().replace('\n', '').replace(' ', '')

data = json.loads(raw_txt)

mod_file_IDs = [x['fileID'] for x in data['files']]

#getting the data from the html file

with open('./test/modlist.html', 'r') as file:
    raw_txt = file.read().replace('<li><a href="',"").splitlines()
del raw_txt[0]
del raw_txt[-1]
url_list = [x.split('">')[0] for x in raw_txt]

# get file name from url
user_agent = random.choice(user_agents)
headers = random.choice(headers_list)
url = url_list[0]
url += "/files"
req = r.get(url, headers=headers, verify=False)
html_text = req.text
# scraper = cfscrape.create_scraper()
# html_text = scraper.get(url).text.splitlines()
print(len(html_text))
with open('temp.html', 'w') as file:
    file.write(html_text)



# print(url)
# req = r.get(url + "/files", 'html.parser')
# lines = req.text.splitlines()
# print(len(lines))
# with open('temp_file.txt', 'w') as f:
#     f.write(req.text)




if len(mod_file_IDs) != len(url_list):
    print("Error: the number of mods in the manifest.json file is different from the number of mods in the modlist.html file")
    print("Number of mods in the manifest.json file: " + str(len(mod_file_IDs)))
    print("Number of mods in the modlist.html file: " + str(len(url_list)))
    exit(-1)

dl_url_list = []
for i in range(len(url_list)):
    url = "https://mediafilez.forgecdn.net/files/" + str(mod_file_IDs[i])[:4] + "/" + str(mod_file_IDs[i])[4:] + "/" + url_list[i].split('/')[-1]
    # print(url)
    dl_url_list.append(url)

# https://mediafilez.forgecdn.net/files/file_ID/file_name.jar