from itertools import count

from p340_ChickenUtil import ChickenStore

brandName = 'pelicana'
baseurl = 'https://pelicana.co.kr/store/stroe_search.html'
def getData():
    saveData = []
    for page_idx in count():
        url = baseurl + '?page=' + str(page_idx + 1)
        chickenStore = ChickenStore(brandName, url)
        print(url)
        soup = chickenStore.getSoup()
        mytable = soup.find('table', attrs={'class':'table mt20'})
        mytbody = mytable.find('tbody')
        # print(mytbody)
        shopExists = False
        for mytr in mytbody.findAll('tr'):
            shopExists = True
            mylist = list(mytr.strings)
            print(mylist)

            tempphone = mytr.select_one('td:nth-of-type(3)').string
            if tempphone != None:
                phone = tempphone.strip()
            else:
                phone = ""

            store = mylist[1]
            address = mylist[3]

            if len(address) >= 2:
                temp = address.split()
                sido = temp[0]
                gugun = temp[1]


            mydata = [brandName, store, sido, gugun, address, phone]
            saveData.append(mydata)
        if shopExists == False:
            chickenStore.save2Csv(saveData)
            break

print(brandName + '매장 크롤링 시작')
getData()
print(brandName + '크롤링 끝')