import requests
import webbrowser

def get_location_by_ip(ip_address):
    try:
        # Fetch location data from ip-api
        url = f"http://ip-api.com/json/{ip_address}"
        response = requests.get(url)
        data = response.json()

        # Check if the request was successful
        if data['status'] == 'success':
            print("\n Location Details:")
            print(f"IP Address: {ip_address}")
            print(f"Country: {data['country']}")
            print(f"Region: {data['regionName']}")
            print(f"City: {data['city']}")
            print(f"ZIP Code: {data['zip']}")
            print(f"Latitude: {data['lat']}")
            print(f"Longitude: {data['lon']}")
            print(f"ISP: {data['isp']}")
            
            # Open the location in Google Maps
            google_maps_url = f"https://www.google.com/maps?q={data['lat']},{data['lon']}"
            print(f"\n Opening location in Google Maps: {google_maps_url}")
            webbrowser.open(google_maps_url)

        else:
            print(" Error: Unable to retrieve location. Check the IP address.")

    except Exception as e:
        print(f" Error: {e}")

if __name__ == '__main__':
    # Ask the user for an IP address
    ip_address = input("🔎 Enter the IP address: ").strip()
    get_location_by_ip(ip_address)
