# Urban_mobility_in_Cracow
**Analiza mobilności miejskiej miasta Krakowa. Zebraliśmy i przedstawiliśmy dane dotyczące zagęszczenia poruszania się po naszym mieście.**  

## Dane do analizy
- **Monitorowanie komunikacji miejskiej:**  
 GTFS (General Transit Feed Specification) to otwarty, międzynarodowy standard zapisu danych o publicznym transporcie zbiorowym, jest on udostępniany również przez ZTP Kraków. 
 https://gtfs.ztp.krakow.pl

- **Pomiary ruchu rowerowego:**  
 ZTP prowadzi pomiary ruchu rowerowego w Krakowie w kilkunastu stałych lokalizacjach które aktualizowane są na bieżąco.
 https://ztp.krakow.pl/rower/pomiary-ruchu-rowerowego

- **Monitorowanie samochodów TOMTOM**  
 TomTom to firma od lat produkująca nawigacje samochodowe. Posiadają własny system map oraz natężenia komunikacyjnego. Ich urządzenia wysyłają anonimowe informacje o położeniu - korzystając z ich API, 
 (które jednak w wersji darmowej udostępnia jedynie cząstkowe dane) możemy oszacować natężenie ruchu ulicznego w danej lokalizacji.

- **Punkty stałego pomiaru natężenia ruchu (GOV)**  
 Generalna Dyrekcja Dróg Krajowych i Autostrad udostępnia nam dane pomiarowe z ich punktów. Niestety jednak jest to system ogólnokrajowy mierzący natężenie głównie w łącznikach dróg ekspresowych i autostrad.
 Na terenie samego miasta Krakowa znajduje się jedynie kilka z nich, nie uzyskaliśmy z nich znaczących danych lecz stanowią cegiełkę która dołożyła się do zsumaryzowania wszystkich danych do projektu.

## Dane pomocnicze
- **Siatki dróg i mapy:**  
 OpenStreetMap projektu tworzącej darmową, swobodnie dostępnej i edytowalnej mapy świata.
 https://www.openstreetmap.org



## Notatniki (Colab)

### Podprojekt:
Analiza opóźnień komunikacji miejskiej  
  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aszczi/Urban_mobility_in_Cracow/blob/main/Opoznienia_KMK.ipynb)  

    
### Projekt właściwy:
Analiza całkowitego ruchu miejskiego  
  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aszczi/Urban_mobility_in_Cracow/blob/main/Mobilnosc_miejska_w_Krakowie_JOIN.ipynb)

## Dokumentacja
- [Opis projektu (PDF)](Opis_projektu.pdf)
- [Analiza projektu (PDF)](Analiza_projektu.pdf)


