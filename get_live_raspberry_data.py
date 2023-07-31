import requests

raspberry = open("raspberry_ip.txt").read()
port = 5000
url = f"http://{raspberry}:{port}/data"

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("Received data:", data)
    else:
        print("Failed to get data. Status code: ", response.status_code)
except requests.exceptions.RequestException as e:
    print("Error:", e)