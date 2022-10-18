import json
import wget
import requests as r


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

url = url_list[0]
url += "/files"
print(url)
req = r.get(url + "/files", 'html.parser')
lines = req.text.splitlines()
print(len(lines))
with open('temp_file.txt', 'w') as f:
    f.write(req.text)
        

# récupération : www.URL/download/ID

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