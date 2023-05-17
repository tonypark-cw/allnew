import json

import folium, requests, os.path
import pandas as pd

url_header = 'https://dapi.kakao.com/v2/local/search/address.json?query='

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath('./')))
secret_file = os.path.join(BASE_DIR, 'secret.json')

with open(secret_file) as f:
    secret_val = json.loads(f.read())

def get_secret(setting, secrets=secret_val):
    try:
        return secrets[setting]
    except KeyError:
        errmsg = 'Key Error'
        return errmsg


header = {'Authorization' : 'KakaoAK ' + get_secret('api_key')}

def getGeocoder(address):
    result = ''
    url = url_header + address
    r = requests.get(url, headers=header)

    if r.status_code == 200:
        try:
            result_address = r.json()["documents"][0]["address"]
            result = result_address["y"], result_address["x"]
        except Exception as err:
            return None
    else:
        result = "ERROR[" + str(r.status_code) + "]"

    return result

def makeMap(brand, store, get_info):
    shopinfo  =store + '('+brand_dict[brand] + ')'
    mycolor = brand_color[brand]
    latitude, longitude = float(get_info[0]), float(get_info[1])
    marker = folium.Marker([latitude, longitude], popup=shopinfo, icon=folium.Icon(color=mycolor, icon='info-sign')).add_to(map_object)


ex_latitude = 37.4946203470469
ex_longitude = 127.027606136235
map_object = folium.Map(location=[ex_latitude, ex_longitude], zoom_start=13)

brand_dict = {'cheogajip':'처가집', 'pelicana':'페리카나'}
brand_color = {'cheogajip':'lightred', 'pelicana':'orange'}

csvfile = 'chicken_result.csv'
myframe = pd.read_csv(csvfile, index_col=0, encoding='utf-8')

where='강남구'
brand_name= 'cheogajip'
condition1 = myframe['gungu'] == where
condition2 = myframe['brand'] == brand_name
map_data01 = myframe.loc[condition1 & condition2]

brand_name= 'pelicana'
condition1 = myframe['gungu'] == where
condition2 = myframe['brand'] == brand_name
map_data02 = myframe.loc[condition1 & condition2]

mylist = []
mylist.append(map_data01)
mylist.append(map_data02)

map_data = pd.concat(mylist, axis=0)

ok = 0
notok = 0

for i in range(len(map_data.index)):
    brand = map_data.iloc[i]['brand']
    store = map_data.iloc[i]['store']
    address = map_data.iloc[i]['address']
    get_info = getGeocoder(address)

    if get_info == None:
        print('Not OK : ', address)
        notok += 1
    else:
        print('OK : ', address)
        ok += 1
        makeMap(brand, store, get_info)
    print('%'*40)

total = ok + notok
print('ok : ', ok)
print('notok : ', notok)
print('total : ', total)

filename = 'xx_chickenMap.html'
map_object.save(filename)
print('file saved')