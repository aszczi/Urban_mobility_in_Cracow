import osmnx as ox
import os

def fetch_osm():
    print("Pobieranie infrastruktury rowerowej dla Krakowa z OpenStreetMap...")
    
    # Konfiguracja osmnx
    ox.settings.use_cache = True
    ox.settings.log_console = True
    
    place = "Kraków, Poland"
    tags = {'highway': ['cycleway', 'path'], 'bicycle': 'designated'}
    
    try:
        # Pobieranie tylko wybranych elementów infrastruktury
        print("Zapytanie Overpass API w toku...")
        gdf = ox.features_from_place(place, tags)
        
        output_dir = os.path.join(os.path.dirname(__file__), "..", "data", "OSM")
        os.makedirs(output_dir, exist_ok=True)
        
        output_path = os.path.join(output_dir, "krakow_bike_infrastructure.geojson")
        
        # Oczyszczanie kolumn typu list przed zapisaniem do geojson
        for col in gdf.columns:
            if col != gdf._geometry_column_name:
                if any(isinstance(val, list) for val in gdf[col]):
                    gdf[col] = gdf[col].apply(lambda x: str(x) if isinstance(x, list) else x)
                
        gdf.to_file(output_path, driver="GeoJSON")
        print(f"Sukces! Zapisano infrastrukturę rowerową (GeoJSON) w: {output_path}")
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"Błąd podczas pobierania danych OSM: {e}")

if __name__ == "__main__":
    fetch_osm()
