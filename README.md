# KH_public_land
高雄公有地與公有地資訊結合
## XML資料parse
- STEP1
```=python
import xml.etree.cElementTree as ET
```
- STEP2 資料解析
```
for f in new_list: #這裡new_list是xml檔案集
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
```
其他參考網站 
- https://pycoders-weekly-chinese.readthedocs.io/en/latest/issue6/processing-xml-in-python-with-element-tree.html
- 
