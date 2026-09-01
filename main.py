import requests
import matplotlib.pyplot as plt
import pandas as pd
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from datetime import date, timedelta
from dotenv import load_dotenv

load_dotenv()  # carrega o arquivo .env

EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

today = date.today()
last_month = today - timedelta(days=30)

url = "https://api.frankfurter.dev/v2/rates"
params = {
    "base": "USD",
    "quotes": "BRL",
    "from": last_month.isoformat(),
    "to": today.isoformat()
}

response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])

plt.plot(df["date"], df["rate"], marker="o", color="gray")
plt.title("Dollar price (USD/BRL) - Last 30 days")
plt.xlabel("Date")
plt.ylabel("Price (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("dollar-price.png")
plt.show()

msg = MIMEMultipart()
msg["Subject"] = "Daily report - USD/BRL price"
msg["From"] = EMAIL_FROM
msg["To"] = EMAIL_TO

msg.attach(MIMEText("Here is attached the graph of the dollar price over the last 30 days.", "plain"))

with open("dollar-price.png", "rb") as img_file:
    image = MIMEImage(img_file.read())
    image.add_header("Content-Disposition", "attachment", filename="dollar-price.png")
    msg.attach(image)

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(EMAIL_FROM, EMAIL_APP_PASSWORD)
    server.send_message(msg)