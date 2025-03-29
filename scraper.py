from config import Config
import requests
from bs4 import BeautifulSoup
import json
from database import save_to_db, load_from_db


def fetch_service_status() -> list[dict]:
    """
    Scrapes service status information from digitaliser.dk and returns it as a list of dictionaries.
    """
       
    try:
        response = requests.get(Config.BASE_URL, timeout=10)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract "last updated" timestamp from the page
    last_updated_tag = soup.find("span", {"data-servicevariable": "LatestUpdate"})
    last_updated = last_updated_tag.get_text(strip=True) if last_updated_tag else "Unknown"

    services = soup.find_all("div", class_="item")

    service_data = []
    for service in services:
        try:
            name_tag = service.find("strong", {"data-servicevariable": "Description"})
            status_tag = service.find("span", class_="info")
            name = name_tag.get_text(strip=True) if name_tag else "Unknown"
            status = status_tag.get_text(strip=True).split(":")[-1].strip() if status_tag else "Unknown"

            service_data.append({
                "service_name": name,
                "status": status,
                "timestamp": last_updated  # Use scraped timestamp
            })
        except AttributeError:
            print("Warning: A service entry is missing expected data.")

    return service_data



if __name__ == "__main__":
    service_data = fetch_service_status()

    if service_data:
        save_to_db(service_data)  # Save to the JSON database
        print("Fetched Data (Saved to database.json):")
        print(json.dumps(service_data, indent=4, ensure_ascii=False))

    #print("\n--- Database Content ---")
    #print(json.dumps(load_from_db(), indent=4, ensure_ascii=False))