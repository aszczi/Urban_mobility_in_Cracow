import requests
import json
import os
from bs4 import BeautifulSoup
import re

def download_ztp_bike_counters():
    print("Próba pobrania danych lub metadanych liczników rowerowych ZTP Kraków...")
    output_dir = os.path.join(os.path.dirname(__file__), "..", "data", "Micromobility")
    os.makedirs(output_dir, exist_ok=True)
    
    # Strona ZTP poświęcona rowerom
    url = "https://ztp.krakow.pl/rower/pomiary-ruchu-rowerowego"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Szukamy linków do plików z danymi (często ZTP wrzuca podsumowania w postaci Excela lub CSV)
        links = soup.find_all('a', href=True)
        data_links = [link['href'] for link in links if ('.csv' in link['href'] or '.xls' in link['href'])]
        
        if not data_links:
            print("Skrypt nie znalazł bezpośrednich linków do plików (.csv/.xls) na głównej stronie ZTP.")
            print("W takim wypadku ZTP zazwyczaj osadza interaktywną mapę (np. Eco-Counter) lub system MSIP.")
            
            # Wyszukajmy osadzone iframe'y (np. web public Eco-Counter)
            iframes = soup.find_all('iframe', src=True)
            for iframe in iframes:
                print(f" -> Zauważono osadzony system pomiarowy (iframe): {iframe['src']}")
        else:
            for d_link in data_links:
                print(f"Znaleziono plik: {d_link}")
                # Tutaj można go pobrać - zależnie od ścieżki
                
        # Zapiszmy treść jako referencję HTML do folderu Micromobility (by np. później sparsować tabele)
        debug_path = os.path.join(output_dir, "ztp_rowery_page_dump.html")
        with open(debug_path, "w", encoding='utf-8') as f:
            f.write(soup.prettify())
            
        print(f"\nZrzut ze strony ZTP pomiary (aby np. wyłuskać dane z tabel w Pandas) zapisany w: {debug_path}")
            
    except Exception as e:
        print(f"Błąd podczas połączenia ze stroną ZTP: {e}")

def fetch_msip_roadworks():
    print("\nPobieranie utrudnień i inwestycji drogowych ze standardu otwartych danych MSIP / ZDMK...")
    
    output_dir = os.path.join(os.path.dirname(__file__), "..", "data", "MSIP")
    os.makedirs(output_dir, exist_ok=True)
    
    # Większość map ZDMK i krakowskich otwartych danych działa w przestrzeni WMS/WFS
    # ArcGIS REST Services Directory dla MSIP Kraków
    # Przykładowy otwarty publiczny endpoint MSIP z Warstwami drogowymi (Inwestycje)
    arcgis_url = "https://msip.krakow.pl/arcgis/rest/services/Zarzadzanie_Ruchem/ZDMK_utrudnienia/MapServer/0/query"
    
    params = {
        "where": "1=1", # Pobierz wszystko
        "outFields": "*",
        "f": "geojson"  # Bezpośrednio GeoJSON aby łatwo było wczytać w GeoPandas!
    }
    
    try:
        req = requests.get(arcgis_url, params=params, timeout=15)
        # Nie zwracamy błędu jeśli to nie zadziała, bo endpointy REST mogą się zmieniać - przechwytujemy.
        if req.status_code == 200:
            data = req.json()
            if data.get('features'):
                out_path = os.path.join(output_dir, "zdmk_utrudnienia.geojson")
                with open(out_path, "w", encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print(f"Sukces! Pobrane utrudnienia / roboty ZDMK: {out_path}")
            else:
                print("Endpoint ZDMK dostępny, ale tymczasowo pusty lub warstwa uległa zmianie.")
        else:
            print(f"Nie udało się połączyć z API ZDMK (ArcGIS). HTTP Status: {req.status_code}")
    except Exception as e:
        print(f"Błąd podczas pobierania wektorów inwestycji MSIP/ZDMK: {e}")

if __name__ == "__main__":
    download_ztp_bike_counters()
    fetch_msip_roadworks()
