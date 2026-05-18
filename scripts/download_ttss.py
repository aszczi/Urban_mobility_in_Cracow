import requests
import json
import os
import datetime

def fetch_ttss():
    print("Pobieranie aktualnych pozycji pojazdów MPK Kraków (TTSS)...")
    
    # Adresy API TTSS dla Krakowa
    urls = {
        "trams": "https://ttss.krakow.pl/internetservice/geoserviceDispatcher/services/vehicleinfo/vehicles?positionType=CORRECTED",
        "buses": "https://ttss.mpk.krakow.pl/internetservice/geoserviceDispatcher/services/vehicleinfo/vehicles?positionType=CORRECTED"
    }

    output_dir = os.path.join(os.path.dirname(__file__), "..", "data", "TTSS")
    os.makedirs(output_dir, exist_ok=True)
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Wyłączenie ostrzeżeń o braku certyfikatu przy weryfikacji False
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    
    for vehicle_type, url in urls.items():
        try:
            response = requests.get(url, timeout=10, verify=False)
            response.raise_for_status()
            
            # Weryfikacja czy odpowiedź to faktycznie JSON
            if "application/json" not in response.headers.get('Content-Type', ''):
                print(f"Ostrzeżenie: Endpoint dla {vehicle_type} nie zwrócił poprawnego formatu JSON. Serwer może być przeciążony lub adres został zmieniony.")
                continue
            
            data = response.json()
            
            output_path = os.path.join(output_dir, f"{vehicle_type}_{timestamp}.json")
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                
            print(f"Zapisano dane ({vehicle_type}) do: {output_path}")
        except Exception as e:
            print(f"Błąd podczas pobierania {vehicle_type}: {e}")

if __name__ == "__main__":
    fetch_ttss()
