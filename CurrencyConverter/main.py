import requests



# Base currency and target

base = input("Enter base currency (e.g., USD): ").upper()
target = input("Enter target currency (e.g., INR): ").upper()
amount = float(input(f"Enter amount in {base}: "))


url = f"https://api.exchangerate-api.com/v4/latest/{base}"

try:
    response=requests.get(url)
    data=response.json()
    print(data)

    if "rates" in data and target in data["rates"]:
        rate=data["rates"][target]
        converted=amount*rate
        print(f"{amount} {base} = {converted:.2f} {target}")
    else:
        print("Currency not supported or wrong base")
except Exception as e:
    print("Error fetching real-time rates: ",e)