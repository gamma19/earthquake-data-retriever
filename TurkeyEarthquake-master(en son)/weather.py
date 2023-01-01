from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import json
from datetime import date

# instantiate an empty dict
weather = {}

# Selenium Ayarları
browserProfile = webdriver.ChromeOptions()
browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'tr,tr_TR'})
browser = webdriver.Chrome(service= Service('Desktop/Python/chromedriver.exe'), options=browserProfile)
browser.minimize_window()

cities =["Adana", "Adıyaman", "Afyon", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Isparta", "İçel (Mersin)", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"]

# Kullanıcıdan Bilgi Alma
#il = input("İl: ").lower().capitalize()         # Girilen karakterleri lower ile küçült, capitalize ile ilk harfi büyüt.
for j in range(0,81):
    url = browser.get(f"https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il={cities[j]}")
    time.sleep(0.5)
    # Kaynak kodlarını çekiyor
    kaynak = browser.page_source
    #time.sleep(1)
    # Beautifulsoup ile parse ediyor
    soup = BeautifulSoup(kaynak, "html.parser")
    #orijinal time.sleep()
    # Etiketler
    anlikDerece = soup.find("div", {"class":"anlik-sicaklik-deger ng-binding"})
    anlikHava = soup.find("div", {"class":"anlik-sicaklik-havadurumu-ikonismi ng-binding"})
    anlikNem = soup.find("div", {"class":"anlik-nem-deger-kac ng-binding"})

    weather[j] = {'City': str(cities[j]), 'Temp': str(anlikDerece.text), 'Condition': str(anlikHava.text), 'Humidity': str(anlikNem.text)}

    print(f"""
    İl: {cities[j]}
    Sıcaklık: {anlikDerece.text}°C
    Hava: {anlikHava.text}
    Nem: %{anlikNem.text}
    """)

with open('weather_old\\{}.json'.format(date.today()), 'w', encoding='utf-8') as f:
    json.dump(weather, f, indent=4, ensure_ascii=False)
