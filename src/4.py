import requests
def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
if __name__ == "__main__":
    url = input("Enter the URL of the API: ")
    data = get_data(url)
    if data is not None:
        print("Data retrieved successfully")
else:
    print("An error occurred while retrieving data")