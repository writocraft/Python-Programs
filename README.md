# https://www.facebook.com/permalink.php?story_fbid=1289077461428963&id=100009801635737
# subscribed jay vijay
# Python-Programs

python program for live corona graph


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import mysql.connector as mysql
import requests
import math
from bs4 import BeautifulSoup
from prettytable import PrettyTable


from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk



url='https://www.worldometers.info/coronavirus/'
r = requests.get(url)

data =r.text
soup=BeautifulSoup(data,'html.parser')


#Basic data
print(soup.title.text)
print()
live_data = soup.find_all('div',id="maincounter-wrap")
for i in live_data:
    
    print(i.text) 
print()
all_rows = soup.find_all('tr')

print('Analyisis based on indivdual countries')
print()
#Extrs=acting table data
table_body = soup.find('tbody')
table_rows = table_body.find_all('tr')

no = []
countries = []
cases = []
todays =[]
deaths = []

for tr in table_rows:
    td=tr.find_all('td')
    countries.append(td[1].text.strip())
    cases.append(td[2].text.strip())
    todays.append(td[3].text.strip())
    deaths.append(td[4].text.strip())
#print(countries)

headers = ['Countries','Total cases','Todays cases','death']
df = pd.DataFrame(list(zip(countries[8:],cases[8:],todays[8:],deaths[8:])),columns=headers)
df.to_csv('corona_analyse.csv')



df["Total cases"] = df["Total cases"].str.replace('[\,\.]', '').astype(int)

tc = list(df["Todays cases"])
for i in range(len(tc)):
    if(str(tc[i]) == ''):
        tc[i] = "0"
        
df["Todays cases"] = tc
df["Todays cases"] = df["Todays cases"].str.replace('[\+\,]','').astype(int)

tc = list(df["death"])
for i in range(len(tc)):
    if(str(tc[i]) == ''):
        tc[i] = "0"
df["death"] = tc
df["death"] = df["death"].str.replace('[\$\,\.]', '').astype(int)




#df.to_Mysql('coronaData.db')
print(df)

# y_pos =[i for i in range(1,len(countries)+1)]

# plt.bar(y_pos,cases[::-1],align='center',alpha=0.5)
# plt.xticks(y_pos,countries[::-1],rotation=5000)
# plt.ylabel('Total Cases')

# plt.title('Petsonals affect by corona')
# plt.savefig('corona-analyse.png',dpi=600)
# plt.show()

country = input("Enter the name of the country : ")


selectedCountry=country


if (country in list(df['Countries'])):
    #print("Hello1")
    country_details = df[df['Countries'].isin([country])]
    print(country_details)
    case_count = list(country_details["Total cases"])[0]
    todays_count = list(country_details["Todays cases"])[0]
    death_count = list(country_details["death"])[0]
    print("country: " + str(country))
    print("case_count : " + str(case_count))
    print("todays_count :" +str(todays_count))
    print("death_count : " + str(death_count))

#---------------------------------------------------------
r=requests.get('https://pomber.github.io/covid19/timeseries.json')
data = r.json()

def getChart():
    
    #country=name.get()
    country=selectedCountry
    print(country)
    
    
    if country=='':
        return
    df=DataFrame(data[country])


    figure = plt.figure()
    subplot=figure.add_subplot(111)
    subplot.plot(df['date'],df['confirmed'],label='confirmed',color='blue')
    subplot.plot(df['date'],df['deaths'],label='deaths',color='red')
    subplot.plot(df['date'],df['recovered'],label='recovered',color='green')

    subplot.legend(loc='upper left')

    start,end=subplot.get_xlim()
    subplot.xaxis.set_ticks(np.arange(start,end,5))


    for tick in subplot.get_xticklabels():
        tick.set_rotation(60)

    #canvas = FigureCanvasTkAgg(figure)
    #canvas.get_tk_widget().grid(row=1,column=4,columnspan=3,rowspan=20)
    plt.show()

'''window =tk.Tk()

name=tk.StringVar()
nameEntered=ttk.Entry(window,width=30,textvariable=name)
nameEntered.grid(column=0,row=1)

button=ttk.Button(window,text="Search trend for country",command=getChart)
button.grid(column=0,row=2)
window.mainloop()'''

getChart()


