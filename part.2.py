"""Questo progetto è mirato a verificare se nei continenti dove è presente un undice di GDP pro capite più basso il livello di morte è più alto.
 Per svolgere questa analisi abbiamo deciso di concentrarci su North e South America dato che hanno parametri simili sulla popolazione e soprattuto per densità di popolazione:
  - popolazione: 578mln North America e 4225.5mln South America
  - densità della popolazione: 57 per mi2 per entrambi i paesi
 Per calcolare il numero di morti pro capite e l'indice GDP utilizzeremo i dataset COVID-19 di Our World in Dtat, in particolare i seguenti dati:
   - numero di morti (new_deaths: New deaths attributed to COVID-19)
   - numero di popolazione (gdp_per_capita: Gross domestic product at purchasing power parity (constant 2011 international dollars), most recent year available)"""


import csv


#Con iterazione creamo la lista che contiene il numero di morti in North America escludendo i valori vuoti
with open ('covid_data.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    new_deaths_n = [float(line[8])
                               for line in csv_reader
                               if line[1] == "North America"
                               and line[8] != ""]

#Calcoliamo la somma totale di morti sum e convertiamo il valore pro capite
total_deaths_n = sum(new_deaths_n)/579000000

#Con iterazione creamo la lista che contiene i dati riguardo il valore GDP
with open('covid_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    gdp_n=[float(line[53])
                       for line in csv_reader
                       if line[1] == "North America"
                       and line[53] != ""]

#Calcoliamo il gdp medio per North America creando un metodo

def calculate_average(num):
    sum_num = 0
    for i in num:
        sum_num = sum_num + i

    avg = sum_num / len(num)
    return avg

average_gdp_n = calculate_average(gdp_n)


#Ripetiamo le stesse operazioni per South America
with open ('covid_data.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    new_deaths_s = [float(line[8])
                               for line in csv_reader
                               if line[1] == "South America"
                               and line[8] != ""]


total_deaths_s = sum(new_deaths_n)/422500000


with open('covid_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    gdp_s=[float(line[53])
                       for line in csv_reader
                       if line[1] == "South America"
                       and line[53] != ""]



def calculate_average(num):
    sum_num = 0
    for i in num:
        sum_num = sum_num + i

    avg = sum_num / len(num)
    return avg
average_gdp_s = calculate_average(gdp_s)

#Utiliziamo tabulate per stampare i dati ottenuti in una tabella
from tabulate import tabulate
data = [
['Total deaths per capita', total_deaths_n, total_deaths_s],
['GDP', average_gdp_n, average_gdp_s]]
print (tabulate(data, headers=["Parameter", "North America", "South America"]))

#Con if compariamo i risultati ottenuti tra i due continenti e stampiamo la conclusione
if total_deaths_s > total_deaths_n and average_gdp_n>average_gdp_s:
    print('\nWe have confirmed the hypothesis that countries with lower GPD per capita have higher death rates.')

else: print('\nWe have contradicted the hypothesis that countries with lower GPD per capita have higher death rates.')

#Creamo due Bar Chart per mostrare i risultati ottenuti
 
import matplotlib.pyplot as plt

continent = ['North America', 'South America']
deaths_per_capita = [total_deaths_n, total_deaths_s]

plt.bar(continent, deaths_per_capita)
plt.title('Country Vs Deaths Per Capita')
plt.xlabel('Country')
plt.ylabel('Total deaths Per Capita')
plt.show()


import matplotlib.pyplot as plt

continent = ['North America', 'South America']
gdp_per_capita = [average_gdp_n, average_gdp_s]
plt.bar(continent, gdp_per_capita)
plt.title('Country Vs GDP Per Capita')
plt.xlabel('Country')
plt.ylabel('GDP Per Capita')
plt.show()
