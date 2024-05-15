"""nombre=soup.find('h2', class_="yp-result-card-title mt-1 md:mt-0").text
data.append(nombre)
print(data)"""



import requests 
from bs4 import BeautifulSoup 
import csv 



def guardar_en_csvtest(lista_valores, nombre_archivo):
    # Abre el archivo CSV en modo de escritura
    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        # Crea un escritor CSV
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(['Business Name'])
        # Itera sobre la lista y escribe cada valor en una fila
        for valor in lista_valores:
            escritor_csv.writerow([valor])




data=[]
#URL = "https://www.seccionamarilla.com.mx/resultados/dentistas/1"
URL="https://paginasamarillas.com.do/en/business/search/santiago/c/dentistas"
page = requests.get(URL) 
   
soup=BeautifulSoup(page.text,'html')
text=soup.find('div')
#print(soup)
#print(soup.find_all('div',class_='-ml-2 mb-1 flex justify-items-stretch gap-1 ng-star-inserted'))
#print(soup.find_all('h2', class_="yp-result-card-title mt-1 md:mt-0"))

listings = soup.find_all('h2', class_="yp-result-card-title mt-1 md:mt-0")

for listing in listings:
    print(listing.text)
    data.append(listing.text)
    
print(data)



def save_to_csv(data, filename):
    # Write the data to a CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Business Name'])
        writer.writerows(data)



guardar_en_csvtest(data,"data.csv")

   

