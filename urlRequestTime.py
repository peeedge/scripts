import requests
import time

def ping_urls(url_list):
    for url in url_list:
        try:
            start_time = time.time()
            response = requests.get(url)
            end_time = time.time()
            response_time = end_time - start_time

            print(f"URL: {url}, Response Time: {response_time} seconds")
        except requests.RequestException as e:
            print(f"URL: {url}, Error: {e}")

# Example usage:
urls_to_ping = ["https://www.example.com", "https://www.google.com", "https://www.github.com"]
ping_urls(urls_to_ping)



