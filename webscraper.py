"""
Amazon Price Tracker (Nintendo Switch)

Scrapes the product title and price of a Nintendo Switch from Amazon UK,
stores the results in a CSV file, and re-checks the price once a day to
track changes over time.
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from bs4 import BeautifulSoup   # HTML parsing
import requests                 # HTTP requests
import smtplib                  # Email support (not currently used)
import time                     # Delay between price checks
import datetime                 # Date handling (not currently used)
import csv                      # Writing results to a CSV file
import pandas as pd             # Reading and displaying the CSV data

# ---------------------------------------------------------------------------
# Step 1: Connect to the website and scrape the product details
# ---------------------------------------------------------------------------

# Product page to scrape
URL = 'https://www.amazon.co.uk/Nintendo-Switch-Neon-Red-blue/dp/B0BJ35S9MQ/ref=sr_1_3?keywords=nintendo%2Bswitch&qid=1679925074&sprefix=nintendo%2Bs%2Caps%2C73&sr=8-3&th=1'

# Browser-like User-Agent so Amazon treats the request as a normal visit
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0"}

# Download the page
page = requests.get(URL, headers=headers)

# Parse the raw HTML, then re-parse the prettified version to get clean,
# consistently formatted markup
soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

# Extract the product title
title = soup2.find(id='productTitle').get_text().strip()

# Extract the price, then strip the currency symbol (first character)
price = soup2.find("span", attrs={"class" : 'a-price aok-align-center reinventPricePriceToPayMargin priceToPay'}).find("span", attrs={"class" : 'a-offscreen'}).text.strip()[1:]

# Print the results to confirm the correct values were scraped
print(title)
print(price)

# ---------------------------------------------------------------------------
# Step 2: Create the CSV file and store the first result
# ---------------------------------------------------------------------------

header = ['Title', 'Price']
data = [title, price]

# Create the file (overwrites any existing file) and write the header row
# followed by the first data row
with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

# ---------------------------------------------------------------------------
# Step 3: Read the CSV back with pandas to verify the stored data
# ---------------------------------------------------------------------------

df = pd.read_csv(r'C:\Users\saleh\AmazonWebScraperDataset.csv')
print(df)

# ---------------------------------------------------------------------------
# Step 4: Append a new row to the existing CSV file
# ---------------------------------------------------------------------------

# Mode 'a+' adds to the end of the file without erasing existing rows
with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)

# ---------------------------------------------------------------------------
# Step 5: Combine the scraping and saving steps into a reusable function
# ---------------------------------------------------------------------------

def check_price():
    """Scrape the current title and price, and append them to the CSV file."""

    URL = 'https://www.amazon.co.uk/Nintendo-Switch-Neon-Red-blue/dp/B0BJ35S9MQ/ref=sr_1_3?keywords=nintendo%2Bswitch&qid=1679925074&sprefix=nintendo%2Bs%2Caps%2C73&sr=8-3&th=1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0"}

    # Download and parse the product page
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    # Extract the title and price (currency symbol removed)
    title = soup2.find(id='productTitle').get_text().strip()

    price = soup2.find("span", attrs={"class" : 'a-price aok-align-center reinventPricePriceToPayMargin priceToPay'}).find("span", attrs={"class" : 'a-offscreen'}).text.strip()[1:]

    data = [title, price]

    # Append the new reading to the dataset
    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

# ---------------------------------------------------------------------------
# Step 6: Automate the price check
# ---------------------------------------------------------------------------

# Run check_price() once every 24 hours (86,400 seconds).
# Note: this loop runs indefinitely, so any code placed after it will not
# execute until the script is stopped.
while(True):
    check_price()
    time.sleep(86400)

# ---------------------------------------------------------------------------
# Results
# ---------------------------------------------------------------------------

# After the script had been running for a day, the CSV showed a price change,
# confirming the tracker detects price drops. Run this in a separate cell or
# script to view the collected data.
df = pd.read_csv(r'C:\Users\saleh\AmazonWebScraperDataset.csv')
print(df)