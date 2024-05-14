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
        listings = soup.find_all('div', class_='listing')

        data = []

        # Iterate through each listing
        for listing in listings:
            # Extract the name of the business
            business_name = listing.find('h2', class_='name').text.strip()
            
            # Extract the name of the owner(s) (if available)
            owner_name = listing.find('span', class_='nombre-dueno')
            owner_name = owner_name.text.strip() if owner_name else ''
            
            # Extract the personal + professional phone of the business
            phone = listing.find('span', class_='telefono')
            phone = phone.text.strip() if phone else ''
            
            # Extract the email from the business and from the owner
            business_email = listing.find('a', class_='correo')
            business_email = business_email['href'].split(':')[1] if business_email else ''
            
            owner_email = listing.find('span', class_='correo-dueño')
            owner_email = owner_email.text.strip() if owner_email else ''
            
            # Extract the location of the business
            location = listing.find('span', class_='l-address')
            location = location.text.strip() if location else ''
            
            # Extract the website of the business
            website = listing.find('a', class_='url')
            website = website['href'] if website else ''

            # Append the extracted data to the list
            data.append([business_name, owner_name, phone, business_email, owner_email, location, website])

        return data

"""def save_to_csv(data, filename):
    # Write the data to a CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Business Name', 'Owner Name', 'Phone', 'Business Email', 'Owner Email', 'Location', 'Website'])
        writer.writerows(data)
"""
def main():
    url = "https://www.seccionamarilla.com.mx/resultados/dentistas/1"
    data = extract_data(url)
    print(data)
    #save_to_csv(data, "dentists_data.csv")

if __name__ == "__main__":
    main()
