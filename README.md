# Public Data Scraping Project

## Project Overview
This project is designed to scrape public data from the IBGE website, specifically state indicators for a given Brazilian state (UF). The script uses `requests` to fetch the page content, `BeautifulSoup` to parse the HTML, and `pandas` to structure the data into a readable format.

## Installation
To run this project, you will need Python installed on your system. Additionally, you'll need to install the following packages:
- BeautifulSoup4
- pandas

You can install these with pip using the following command:
pip install beautifulsoup4
pip install pandas

## Usage
To use this script, simply call the `scraping_uf` function with the UF code of the Brazilian state you want to scrape. For example:
```python
state = scraping_uf('rj')
