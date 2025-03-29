import os
import json
from config import Config



def save_to_db(new_data):
    """
    Appends new service status data to database.json without loading existing data.
    Writes new data directly to the file, one entry at a time.
    """
    try:
        # Open the file in append mode
        with open(Config.DB_FILE, "a", encoding="utf-8") as f:
            for entry in new_data:
                # Write each new entry as a JSON object, one per line
                json.dump(entry, f, ensure_ascii=False)
                f.write("\n")  # Ensure each entry is on a new line
    except Exception as e:
        print(f"Error saving data: {e}")


def load_from_db():
    """
    Loads the service status data from database.json.
    Reads each line of the file and returns it as a list of dictionaries.
    """
    if not os.path.exists(Config.DB_FILE):
        return []

    data = []
    try:
        with open(Config.DB_FILE, "r", encoding="utf-8") as f:
            for line in f:
                data.append(json.loads(line.strip()))  # Load each JSON object from each line
    except Exception as e:
        print(f"Error loading data: {e}")

    return data
