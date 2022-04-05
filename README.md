# Check Redirects

## Rationale
The script reads the URLs from a CSV file and checks if the redirects are correct.

## Installation
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration
Specify base URL and CSV file.

Example:
```
BASE_URL = 'http://www.example.com/'   # Leave empty if URLs are absolute; otherwise, use http://www.example.com/ format
CSV_FILE = 'test_redirects.csv'
```
Note: leave BASE_URL empty if URLs in the CSV are absolute.

## CSV format
```
Original_URL_1,Redirect_URL_1
...
Original_URL_N,Redirect_URL_N
```
Make sure to put your own CSV file with redirects in the same directory as the script.

## Usage
```
source venv/bin/activate  # Not needed if the venv is already activated
python main.py
```

