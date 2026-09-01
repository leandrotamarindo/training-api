# USD/BRL Price Automation

A Python script that automates the process of fetching, visualizing, and reporting the USD to BRL exchange rate. It collects the last 30 days of exchange rate data, generates a chart, and automatically sends the report by email.

## What it does

1. Fetches USD/BRL exchange rate data for the last 30 days using the [Frankfurter API](https://frankfurter.dev/)
2. Processes the data with `pandas`
3. Generates a line chart of the exchange rate over time using `matplotlib`
4. Sends the chart as an email attachment via Gmail's SMTP server

## Tech Stack

- Python
- `requests` — API requests
- `pandas` — data processing
- `matplotlib` — data visualization
- `smtplib` / `email` — sending emails
- `python-dotenv` — managing environment variables securely

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/leandrotamarindo/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the root of the project with the following variables:

```
EMAIL_FROM=your_email@gmail.com
EMAIL_TO=recipient_email@gmail.com
EMAIL_APP_PASSWORD=your_gmail_app_password
```

> **Note:** `EMAIL_APP_PASSWORD` must be a Gmail [App Password](https://myaccount.google.com/apppasswords), not your regular account password. This requires 2-Step Verification to be enabled on your Google account.

The `.env` file is included in `.gitignore` and should never be committed to version control.

### 4. Run the script

```bash
python main.py
```

## Output

- A chart image (`dollar-price.png`) is saved locally
- An email with the chart attached is sent automatically to the configured recipient

## Possible Improvements

- Support for additional currency pairs
- Scheduled execution (e.g., via `cron` or a task scheduler)
- Sending reports via Telegram in addition to email
- Exporting the data to an Excel spreadsheet

## Author

Leandro Tamarindo Dias
[LinkedIn](https://www.linkedin.com/in/leandro-tamarindo-dias-84800a245/) · [GitHub](https://github.com/leandrotamarindo)
