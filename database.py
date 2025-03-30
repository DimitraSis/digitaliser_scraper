import os
import json
from config import Config



def save_to_db(new_data):
    """
    Appends new service status data to database.txt without loading existing data.
    Writes new data directly to the file, one entry at a time.
    """
    try:
        # Open the file in append mode
        # If we want to overwrite the file, i can use "w" mode instead of "a"
        with open(Config.DB_FILE, "a", encoding="utf-8") as f:
            for entry in new_data:
                # Write each new entry as a JSON object, one per line
                json.dump(entry, f, ensure_ascii=False)
                f.write("\n")  # Ensure each entry is on a new line
    except (TypeError, ValueError) as json_error:
        print(f"Skipping invalid data entry: {json_error}")
    except FileNotFoundError:
        print(f"Database file {Config.DB_FILE} not found.")
    except Exception as e:
        print(f"Error saving data: {e}")
    


def load_from_db():
    """
    Loads the service status data from database.txt.
    Reads each line of the file and returns it as a list of dictionaries.
    """
    if not os.path.exists(Config.DB_FILE):
        print(f"Database file {Config.DB_FILE} does not exist. Returning empty list.")
        return []

    data = []
    try:
        with open(Config.DB_FILE, "r", encoding="utf-8") as f:
            for line in f:
                data.append(json.loads(line.strip()))  # Load each JSON object from each line
    except json.JSONDecodeError:
        print(f"Warning: Skipping corrupted JSON entry: {line.strip()}")
    except FileNotFoundError:
        print(f"Database file {Config.DB_FILE} not found.")
    except Exception as e:
        print(f"Error loading data: {e}")

    return data
