import requests
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
data = awnser.json()  # agora é uma LISTA, não um dicionário

df = pd.DataFrame(data)  # dados vindos da API
df["date"] = pd.to_datetime(df["date"])
