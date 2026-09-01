import requests
import matplotlib.pyplot as plt
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
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

plt.plot(df["date"], df["rate"], marker="o", color="gray")
plt.title("Dolar price (USD/BRL) - Last 30 days")
plt.xlabel("Date")
plt.ylabel("Price (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Dolar-price.png")
plt.show()

msg = MIMEMultipart()
msg["Subject"] = "Diary report - Price USD/BRL"
msg["From"] = "ltdias07@gmail.com"
msg["To"] = "tamarindodiasl@gmail.com"

msg.attach(MIMEText("Here is attached the graphic of the price of dolar in the last 30 days.", "plain"))

with open("Dolar-price.png", "rb") as img_file:
    image = MIMEImage(img_file.read())
    image.add_header("Content-Disposition", "attachment", filename="dolar-price.png")
    msg.attach(image)

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login("ltdias07@gmail.com", "xrma fdgn ioec inpz")
    server.send_message(msg)