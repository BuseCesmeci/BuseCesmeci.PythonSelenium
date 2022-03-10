"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, request
from selenium import webdriver
import time


app = Flask('') # Flask web servis, ve bunu baslatti.
@app.route('/') # ana dizine yonlendirme 
def home(): # ana dizinde calisacak bir fonks. tanimi
    _extcolor = request.args.get('extcolor')  # query parametreleri yani apiye gelen parametreler. argumanlardan extcoloru get et
    _brand = request.args.get('brand')
    _transmission = request.args.get('transmission')
    _year = request.args.get('year')

   
    browser = webdriver.Chrome() # selenium icin tarayıcı tanimladik
    query = "" # query degiskeni
    if _transmission:
        query += "&transmission_slugs[]=" + _transmission
    if _brand:
        query += "&makes[]=" + _brand
    if _extcolor:
        query += "&exterior_color_slugs[]=" + _extcolor
    if _year:
        query += "&year_max="+ _year + "&year_min=" + _year

    url = "https://www.cars.com/shopping/results/?page=1&page_size=50"+query
    browser.get(url)
       
    #scroll buraya yazilacak
    # eger sleep yazilacaksa buraya yazilmali

    araclist = browser.find_elements_by_class_name('vehicle-card   ') #tum araclari class ismine gore getirip araclist degiskenine atandi
    responsearray = []  # araclar liste olarak geldigi icin bir responsearray dizi tanimlandi     
    for arac in araclist :
       # click()
        title = arac.find_element_by_xpath('.//*[@class="title"]').text # . en bastan okumasin diye
        price = arac.find_element_by_xpath('.//*[@class="primary-price"]').text
        try :
            photoUrl = arac.find_element_by_xpath('.//*[@class="vehicle-image"]').get_attribute("src") # sayfa yuklenirken gelmeyen fotograflar icin try catch 
        except :
            photoUrl = " " # cathe duserse yuklenmeyen foto null gelsin
        brand = title.split(' ')[1] # title'i splitle bolup marka ve yili ordan çekildi
        year = title.split(' ')[0]        
        #extcolor = arac.find_element_by_xpath('').text  # bunlar sayfanin icinde old. icin alamadım.
        #transmission = arac.find_element_by_xpath('').text
        
        responsearray.append({  # append: ekle # for'da donen her bir arac itemini append ile responarray'ine eklendi
                                    'title': title, # 'title' jsondaki key adi
                                    'price': price,
                                    'photoUrl' : photoUrl,
                                    'brand': brand,
                                    'year': year,
                                    #'extcolor': extcolor,
                                    #'transmission': transmission                    
                             }) 
    return {'data': responsearray} # responsearray data key'inde tutuluyor

   
if __name__ =="__main__": #pythonın genel kurali baslangic koruması gibi bisey if icerisinde calistiryor. calisan class __main__ classi ana fonks.
    app.run(host='localhost', port=8080, debug = True)

# not: localhost açıldıgında 8080 degilse 8080'e cekince dogru bir seikle geliyor.

