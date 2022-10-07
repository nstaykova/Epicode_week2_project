import csv


"""Questo progetto è mirato a verificare se nei paesi dove è presente maggior incertezza sulle vaccinazioni è possibile riscontrare un livello di vaccinazione pro capite più basso.
 Per svolgere questa comparazione sono stati utilizzati i dati estratti dallo studio della Wellcome Trust, che indicano la Francia come il paese con indice di fiducia inferiore al mondo, mentre in Spagna riscontriamo un indice di fiducia nei vaccini elevato. 
    Per calcolare il numero di vaccinazioni pro capite utilizzeremo i dataset COVID-19 di Our World in Dtat, in particolare i seguenti dati:
     - numero di vaccinazioni (new_vaccinations: New COVID-19 vaccination doses administered)
     - numero di popolazione (population: Latest available values)"""

#Con iterazione creamo la lista che contiene le nuove vaccinazioni in Francia escludendo i valori vuoti
with open ('covid_data.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    new_vaccinations_France = [float(line[38])
                               for line in csv_reader
                               if line[2] == "France"
                               and line[38] != ""]

#Calcoliamo la somma totale di vaccinazioni somministrati utilizzando sum e convertiamo il valore in mln
total_vaccinations_France = sum(new_vaccinations_France)/1000000

#Con iterazione creamo la lista che contiene i dati riguardo il numero della popolazione
with open('covid_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    population_France=[float(line[48])
                       for line in csv_reader
                       if line[2] == "France"
                       and line[48] != ""]
#Selezioniamo il valore più recente in mln
population_France_latest=population_France[-1]/1000000

#Ripetiamo le stesse operazioni per Spagna
with open('covid_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    new_vaccinations_Spain = [float(line[38])
                              for line in csv_reader
                              if line[2] == "Spain"
                              and line[38] != ""]
    total_vaccinations_Spain = sum(new_vaccinations_Spain)/1000000

with open('covid_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    population_Spain = [float(line[48])
                        for line in csv_reader
                        if line[2] == "Spain"
                        and line[48] != ""]
    population_Spain_latest = population_Spain[-1]/1000000

#Calcoliamo in valore pro capite
vaccination_rate_France = total_vaccinations_France/population_France_latest

vaccination_rate_Spain = total_vaccinations_Spain/population_Spain_latest

#Utiliziamo tabulate per stampare i dati ottenuti in una tabella
from tabulate import tabulate
data = [
['Total vaccinations(mln)', total_vaccinations_France, total_vaccinations_Spain],
['Population(mln)', population_France_latest, population_Spain_latest],
['Vaccination rate per capita', vaccination_rate_France, vaccination_rate_Spain]]
print (tabulate(data, headers=["Parameter", "France", "Spain"]))

#Con if compariamo i risultati ottenuti tra i due paesi e stampiamo la conclusione
if vaccination_rate_France > vaccination_rate_Spain:
    print('\nThe vaccination rate per capita is higher in France.\nThis contradicts the hypothesis that countries with low trust in vaccine safety have lower vaccination rates per capita.')

else: print('\nThe vaccination rate per capita is higher in Spain,\nThis confirms the hypothesis that countries with high trust in vaccine safety have higher vaccination rates per capita.')


