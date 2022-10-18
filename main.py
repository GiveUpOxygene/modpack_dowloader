import json
import wget


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
urls = [x.split('">')[0] for x in raw_txt]

# récupération : www.URL/download/ID

if len(mod_file_IDs) != len(urls):
    print("Error: the number of mods in the manifest.json file is different from the number of mods in the modlist.html file")
    print("Number of mods in the manifest.json file: " + str(len(mod_file_IDs)))
    print("Number of mods in the modlist.html file: " + str(len(urls)))
    exit(-1)


