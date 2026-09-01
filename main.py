import requests
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date, timedelta

today = date.today()
last_month = today - timedelta(days=30)

url = "https://api.frankfurter.dev/v2/rates"
params = {
    "base": "USD",
    "quotes": "BRL",
    "from": last_month.isoformat(),
    "to": today.isoformat()
}

awnser = requests.get(url, params=params)
data = awnser.json()  

df = pd.DataFrame(data)  
df["date"] = pd.to_datetime(df["date"])

plt.plot(df["date"], df["rate"], marker="o", color="red")
plt.title("Dolar price (USD/BRL) - Last 30 days")
plt.xlabel("Date")
plt.ylabel("Price (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Dolar-price.png")
plt.show()
