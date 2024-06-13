import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# List of websites to scrape
websites = [
    'https://www.aljazeera.net/encyclopedia/2024/2/12/%D9%82%D8%B6%D9%8A%D8%A9-%D8%A5%D8%A8%D8%B3%D8%AA%D9%8A%D9%86-%D8%B4%D8%A8%D9%83%D8%A9-%D9%84%D9%84%D8%AF%D8%B9%D8%A7%D8%B1%D8%A9-%D8%A8%D8%A7%D9%84%D9%82%D8%A7%D8%B5%D8%B1%D8%A7%D8%AA',
    'https://arabic.rt.com/world/1551763-%D8%AA%D9%82%D8%B1%D9%8A%D8%B1-%D8%AC%D8%AF%D9%8A%D8%AF-%D9%8A%D9%83%D8%B4%D9%81-%D9%85%D8%B9%D9%84%D9%88%D9%85%D8%A7%D8%AA-%D8%B5%D8%A7%D8%AF%D9%85%D8%A9-%D8%B9%D9%86-%D8%AC%D8%B2%D9%8A%D8%B1%D8%A9-%D8%A5%D8%A8%D8%B3%D8%AA%D9%8A%D9%86-%D9%84%D9%84%D8%A7%D8%B3%D8%AA%D8%BA%D9%84%D8%A7%D9%84-%D8%A7%D9%84%D8%AC%D9%86%D8%B3%D9%8A-%D9%84%D9%84%D8%A3%D8%B7%D9%81%D8%A7%D9%84/#',
    'https://www.alhurra.com/hl-hqa/2024/01/08/%D8%B4%D8%B1%D8%A8-%D8%AF%D9%85%D8%A7%D8%A1-%D9%88%D8%A3%D8%B9%D9%85%D8%A7%D9%84-%D9%85%D8%B1%D9%88%D8%B9%D8%A9-%D9%85%D8%A7-%D8%AD%D9%82%D9%8A%D9%82%D8%A9-%D8%B4%D9%87%D8%A7%D8%AF%D8%A9-%D8%B7%D9%81%D9%84%D9%8A%D9%86-%D8%B9%D9%85%D8%A7-%D8%AC%D8%B1%D9%89-%D8%A8%D8%AC%D8%B2%D9%8A%D8%B1%D8%A9-%D8%A5%D8%A8%D8%B3%D8%AA%D9%8A%D9%86%D8%9F',
    'https://asharq.com/politics/76612/%D9%82%D8%B6%D9%8A%D8%A9-%D8%AC%D9%8A%D9%81%D8%B1%D9%8A-%D8%A5%D8%A8%D8%B3%D8%AA%D9%8A%D9%86-%D9%85%D8%A7%D8%B0%D8%A7-%D9%86%D8%B9%D8%B1%D9%81-%D8%B9%D9%86-%D8%A3%D9%83%D8%A8%D8%B1-%D9%81%D8%B6%D9%8A%D8%AD%D8%A9-%D8%AC%D9%86%D8%B3%D9%8A%D8%A9-%D9%81%D9%8A-%D8%A3%D9%85%D9%8A%D8%B1%D9%83%D8%A7/',
    'https://www.aljazeera.net/news/2024/1/4/%D9%88%D8%AB%D8%A7%D8%A6%D9%82-%D8%A5%D8%A8%D8%B3%D8%AA%D9%8A%D9%86-%D8%AA%D9%83%D8%B4%D9%81-%D8%AA%D9%88%D8%B1%D8%B7-%D8%B1%D8%A4%D8%B3%D8%A7%D8%A1-%D8%AF%D9%88%D9%84-%D9%88%D8%B1%D8%AC%D8%A7%D9%84',
    'https://arabicpost.net/%D9%85%D9%86%D9%88%D8%B9%D8%A7%D8%AA/2024/01/08/%D8%AC%D8%B2%D9%8A%D8%B1%D8%A9-%D8%A5%D8%A8%D8%B3%D8%AA%D9%8A%D9%86/',
    
]

# Function to scrape paragraphs from a single website
def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract all paragraphs from the website
        paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]
        return paragraphs
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve {url}: {e}")
        return None

# List to hold the data
data = []

# Scrape each website
for website in websites:
    print(f"Scraping {website}")
    paragraphs = scrape_website(website)
    if paragraphs:
        for paragraph in paragraphs:
            # Append each paragraph with a default score of 0
            data.append([paragraph, 0])
    else:
        print(f"No text found for {website}")

# Convert the data to a DataFrame
df = pd.DataFrame(data, columns=['text', 'score'])

# Remove empty rows
df = df[df['text'].str.strip().astype(bool)]

# Save the DataFrame to a CSV file
output_file = 'paragraphs.csv'
df.to_csv(output_file, index=False, encoding='utf-8')

print(f"Data saved to {output_file}")
