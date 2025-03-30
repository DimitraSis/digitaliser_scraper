# Digitaliser.dk Service Status Scraper by Dimitra Siskou

This is a Python script that scrapes service status information from [Digitaliser.dk](https://digitaliser.dk/driftsstatus). It extracts the names and operational status of the listed services and saves the data in JSON format.

## Features
- Scrapes service status from Digitaliser.dk
- Extracts service name and operational status
- Saves data in a structured JSON format
- Appends new data to a local txt file
- Implements some error handling
- Unit and intergration test 


### 1. Clone the repository from git:
```bash
 https://github.com/DimitraSis/digitaliser_scraper.git

```

### 2. Create and activate a virtual environment:
```bash
# Windows (PowerShell)
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script to fetch service status data and save it to a txt file:
```bash
python scraper.py
```

By default, the scraped data is saved in `database.txt`.

## Project Structure
```
📂 digitaliser_scraper/
│── 📄 scraper.py           # Scrapes data from Digitaliser.dk
│── 📄 database.py          # Handles saving data to a database
│── 📄 config.py            # Stores configuration (e.g., base URL)
│── 📄 requirements.txt     # List of dependencies
│── 📄 README.md            # Project documentation
│── 📄 database.txt         # A file (mocup) database
│── 📄 tests/
│   │── test_scraper.py      # Unit test
│   │── test_scraper_integration.py  # Integration test
```

## Configuration

The base URL is stored in `config.py`:
```python
class Config:
    BASE_URL = "https://digitaliser.dk/driftsstatus"
```
If the URL changes, update it in this file.
The same for the database.


## Tests

To run all test files (unit + integration), use:
```python
python -m unittest discover tests
```

