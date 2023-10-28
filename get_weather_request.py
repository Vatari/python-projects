import requests
city_name = input("Enter city: ")
print(city_name)
print("Displaying Weather report for: ", city_name)

url = f"https://wttr.in/{city_name}"

res = requests.get(url)
print(res.text)
input("Press Enter to exit")

