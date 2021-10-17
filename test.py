import json
with open('基地內國有地.geojson', mode='r', encoding='utf-8') as file:
    data = json.load(file)
code_list = []
for i in data['features']:
    if i['properties']['SECTNO'] not in code_list:
        code_list.append(i['properties']['SECTNO'])
new_list = []
for i in code_list:
    str1 = 'e_'+i+'.xml'
    new_list.append(str1)
print(new_list)
