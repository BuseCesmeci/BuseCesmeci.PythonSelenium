# BuseCesmeci.PythonSelenium
Selenium

# nasıl çalışır?
1.Calistirmak icin localhostu : 8080 poruna getirmek gerekiyor.
2.Filtreler url ile çalışıyor. 

#Case'de istenen şekilde filtre url'leri.
1. İlk 50 arac
localhost:8080 oldugunda direkt ilk 50 arac geliyor
 http://localhost:8080
2. Siyah renkli araclar 
 http://localhost:8080/?extcolor=black
3. Siyah renkli bmw araclar
http://localhost:8080/?brand=bmw&extcolor=black
4. Otomatik vites türündeki 2018 Ford araclar
http://localhost:8080/?brand=ford&year=2018&transmission=automatic
