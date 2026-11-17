import requests 

api_key = "30d4741c779ba94c470ca1f63045390a"

user_input = input("Enter a city:")

url = f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"

response = requests.get(url, timeout = 10)
print(response.status_code)
data = response.json()

if response.json()['cod'] == 200:
    temp = round(response.json()['main']['temp'])
    weather = response.json()['weather'][0]['main']

    print(f"The temperature in {user_input} is {temp}F")
    print(f"The weather in {user_input} is {weather}")

elif response.json()['cod'] == '404':
    print("City not found!")

else:
    print("Something went wrong:", data)

