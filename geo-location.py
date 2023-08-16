import requests

def get_geolocation(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    ip_address = input("Enter your ip address:")
    geolocation_data = get_geolocation(ip_address)
    
    print("Geolocation info : ")
    print(f"IP Address: {geolocation_data['ip']}")
    print(f"City : {geolocation_data['city']}")
    print(f"Region: {geolocation_data['region']}")
    print(f"Country: {geolocation_data['country']}")
    print(f"Location: {geolocation_data['loc']}")
    
if __name__ == "__main__":
    main()