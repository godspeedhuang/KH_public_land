import xml.etree.cElementTree as ET
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

for f in new_list:
    tree = ET.ElementTree(file='高雄市公有土地資訊\\'+f)
    root = tree.getroot()
    for elem in root.iter('土地標示部'):
        land = elem.find('段代碼').text
        land_name = elem.find('段小段').text
        land_code = elem.find('地號').text
        if int(land_code) % 10000 != 0:
            land_code = str(int(land_code)//10000)+'-' + \
                str(int(land_code) % 10000)
        else:
            land_code = str(int(land_code)//10000)
        name = elem.findall('所有權人')
        own_list = []
        class_list = []
        manage_list = []
        for n in name:
            n_own = n.find('所有權人名稱').text
            n_class = n.find('所有權人類別').text
            n_manage = n.find('管理者名稱').text
            if n_manage not in manage_list:
                manage_list.append(n_manage)
                class_list.append(n_class)
                own_list.append(n_own)
        print(land, land_name, land_code, own_list, class_list, manage_list)
        for i in data['features']:
            if i['properties']['SECTNO'] == land and i['properties']['PARCELNO'] == land_code:
                i['properties']['所有權人名稱'] = own_list
                i['properties']['所有權人類別'] = class_list
                i['properties']['管理者名稱'] = manage_list

with open('基地內公有地_權屬.geojson', mode='w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False)
