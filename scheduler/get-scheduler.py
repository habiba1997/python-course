import requests
import schedule
import time


def send_request():
    url = "https://boycott-f7kw.onrender.com/fetchall"
    response = requests.get(url)

    # You can handle the response if needed
    print(f"Request sent to {url}. Status code: {response.status_code}")


# Schedule the request every 12 minutes
schedule.every(12).minutes.do(send_request)

# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)