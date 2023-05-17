import json

import folium, requests, os.path

address = '서울 마포구 신수동 451번지 세양청마루아파트 상가 101호'

# url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address


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
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
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

address_latlng = getGeocoder(address)
latitude = address_latlng[0]
longitude = address_latlng[1]

print('주소지 : ', address)
print('위도 : ', latitude)
print('경도 : ', longitude)

shopinfo = '교촌 신수점'
folium_map = folium.Map(location=[latitude, longitude], zoom_start=17)
myicon = folium.Icon(color='lightred', icon='info-sign')
folium.Marker([latitude,longitude], popup=shopinfo, icon=myicon).add_to(folium_map)

folium.CircleMarker([latitude, longitude], radius=300, color='darkblue', fill_color='lightred', fill=False, popup=shopinfo).add_to(folium_map)
folium_map.save('./xx_kyochon.html')
print('file saved...')