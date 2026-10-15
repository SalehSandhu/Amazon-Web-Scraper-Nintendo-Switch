# Amazon Price Tracker: Nintendo Switch

A Python web scraper that collects the title and price of a Nintendo Switch from Amazon UK, stores the results in a CSV file, and re-checks the price automatically once a day to track changes over time.

## Features

- Scrapes the product title and current price from an Amazon UK product page
- Saves results to a CSV file with `Title` and `Price` columns
- Appends a new row on every check, building a price history
- Runs automatically every 24 hours in the background
- Reads the CSV back with pandas for quick inspection of the collected data

## Results

After leaving the script running, a price change was detected within a day, resulting in a cheaper Nintendo Switch. This confirmed the tracker works as intended for spotting price drops.

## How It Works

1. **Connect:** sends an HTTP request to the product page using `requests`, with a browser-style User-Agent header.
2. **Parse:** loads the HTML into `BeautifulSoup` and locates the product title and price elements.
3. **Clean:** strips whitespace and the currency symbol from the scraped values.
4. **Store:** writes the data to `AmazonWebScraperDataset.csv` using Python's `csv` module.
5. **Inspect:** reads the CSV into a pandas DataFrame to verify the stored data.
6. **Automate:** wraps the logic in a `check_price()` function and calls it in a loop with a 24-hour delay (`time.sleep(86400)`).

## Getting Started

### Prerequisites

- Python 3
- The following libraries:

```bash
pip install requests beautifulsoup4 pandas
```

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SalehSandhu/Amazon-Web-Scraper-Nintendo-Switch.git
   cd Amazon-Web-Scraper-Nintendo-Switch
   ```

2. Install the dependencies (see above).

### Running the Script

```bash
python webscraper.py
```

The script prints the product title and price, creates `AmazonWebScraperDataset.csv`, and then keeps checking the price once a day. Press `Ctrl + C` to stop it.

To track a different product, replace the `URL` value in the script with another Amazon product page. Note that Amazon's page layout can change, so the HTML class names used to find the price may need updating.

## Example Output

The CSV file has the following structure:

| Title | Price |
|-------|-------|
| Nintendo Switch (product title) | price at time of check |
| Nintendo Switch (product title) | price at next check |

## Project Structure

```
Amazon-Web-Scraper-Nintendo-Switch/
├── webscraper.py                # Scraper, CSV writer and daily automation
├── AmazonWebScraperDataset.csv  # Collected title and price data
└── README.md
```

## Technologies Used

- Python
- Requests
- Beautiful Soup 4
- pandas
- csv, time (standard library)

## What I Learned

- Sending HTTP requests and parsing HTML to extract data
- Locating elements with HTML ids and class names
- Cleaning scraped text and storing it in a structured CSV file
- Reading and displaying tabular data with pandas
- Automating a repeating task with a loop and timed delay

## Future Improvements

- Send an email alert (using `smtplib`) when the price drops below a target
- Add a timestamp column so each price reading is dated
- Track multiple products from a list of URLs
- Chart the price history over time
- Add error handling for failed requests and layout changes

## Disclaimer

This project was built for educational purposes. Keep request frequency low.

## Author

**Saleh Sandhu**
Computer Science graduate, University of Westminster

- GitHub: [@SalehSandhu](https://github.com/SalehSandhu)
- Portfolio: [salehsandhu.github.io/SalehPortfolio](https://salehsandhu.github.io/SalehPortfolio/)
