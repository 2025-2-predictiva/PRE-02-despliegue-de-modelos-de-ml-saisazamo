# api_client.py

#
# Usage from command line:
# curl http://127.0.0.1:5000 -X POST -H "Content-Type: application/json" -d '{"bathrooms": "2", "bedrooms": "3", "sqft_living": "1800", "sqft_lot": "2200", "floors": "1", "waterfront": "1", "condition": "3"}'
#
import requests


def make_request():
    """Make a request to the API server"""

    url = "http://127.0.0.1:5000"

    data = {
        "bathrooms": "6",
        "bedrooms": "3",
        "sqft_living": "1900",
        "sqft_lot": "2700",
        "floors": "2",
        "waterfront": "1",
        "condition": "5",
    }

    response = requests.post(url, json=data, timeout=5)

    print(f'The price predicted based on the data is: {response.text} USD')


if __name__ == "__main__":
    make_request()
