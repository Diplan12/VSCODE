import requests
from bs4 import BeautifulSoup
import csv

def extract_data(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all the listings on the page
        listings = soup.find_all('div', class_='result')
        
        data = []

        # Iterate through each listing
        for listing in listings:
            # Extract the name of the business
            business_name = listing.find('h2', class_='business-name').text.strip()
            
            # Extract the name of the owner(s) (if available)
            owner_name = listing.find('span', class_='owner-name')
            owner_name = owner_name.text.strip() if owner_name else ''
            
            # Extract the phone number
            phone = listing.find('span', class_='phones phone-primary')
            phone = phone.text.strip() if phone else ''
            
            # Extract the email (if available)
            email = listing.find('a', class_='email-business')
            email = email['href'].split(':')[1] if email else ''
            
            # Extract the location
            location = listing.find('div', class_='street-address').text.strip()
            
            # Extract the website (if available)
            website = listing.find('a', class_='track-visit-website')
            website = website['href'] if website else ''

            # Append the extracted data to the list
            data.append([business_name, owner_name, phone, email, location, website])

        return data

def save_to_csv(data, filename):
    # Write the data to a CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Business Name', 'Owner Name', 'Phone', 'Email', 'Location', 'Website'])
        writer.writerows(data)

def main():
    url = "https://www.yellowpages.com/search?search_terms=dentists&geo_location_terms=New+York%2C+NY"
    data = extract_data(url)
    save_to_csv(data, "yellow_pages_data.csv")

if __name__ == "__main__":
    main()
