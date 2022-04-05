import requests
import csv
from urllib.parse import urljoin

BASE_URL = 'http://0.0.0.0:5000/'   # Leave empty if URLs are absolute; otherwise, use http://www.example.com/ format
CSV_FILE = 'test_redirects.csv'

def read_csv(filename: str) -> list:
    url_list = []

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            url_list.append([row[0], row[1]])

    return url_list


def get_redirect_url(url: str) -> str:
    try:
        r = requests.get(urljoin(BASE_URL, url), allow_redirects=False)
        if r.status_code == 301 or r.status_code == 302:
            return r.headers['location']
        else:
            return None
    except:
        pass


def check_redirects(url_list):
    valid_count = 0
    invalid_count = 0

    for urls in url_list:
        redir_url = get_redirect_url(urls[0])
        # print('# ', urljoin(BASE_URL, redir_url), urljoin(BASE_URL, urls[1]))
        if redir_url is None or urljoin(BASE_URL, redir_url) != urljoin(BASE_URL, urls[1]):
            print('"{}" -> "{}"; expected "{}"'.format(urls[0], redir_url, urls[1]))
            invalid_count += 1
        else:
            valid_count += 1

    print('Result: {} valid, {} invalid redirects'.format(valid_count, invalid_count))


def main():
    url_list = read_csv(CSV_FILE)
    check_redirects(url_list)


if __name__ == '__main__':
    main()
