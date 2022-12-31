from clrprint import *  #pip install clrprint
import pandas as pd  #pip install pandas
import matplotlib.pyplot as pl  #pip install matplotlip
import time  #To delay execution (looks good with it !)
import csv
from csv import writer
import webbrowser
import numpy as np
df=pd.read_csv("D:\\School\\IP\\IPP\\iatafinal.csv",encoding="ISO-8859-1")
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
#####################################################################################################################################################################
while True:  
    clrprint("\n\t\t\t\t\t\tWELCOME TO THE IATA DATA GUIDE ",clr='r')
    time.sleep(2)
    clrprint('\nEnter "1" to know more "ABOUT IATA" \nEnter "2" to go to "IATA AIRPORTS FINDER" \nEnter "3" for "Passenger Statistics of Top 10 Airports"\nEnter"4" for some Interesting Airport Statistics \nEnter "5" to access civilian Flight Radar and Ground conditions at Airport (Requires Wi-Fi) \nEnter "6" to leave this program ',clr='d')
    time.sleep(2)
    opt=eval(clrinput("Your Choice: ",clr='b'))

    if opt == 1 :

        time.sleep(1)
        clrprint("\nABOUT IATA",clr='r')
        clrprint("\nThe IATA is the trade association of the world's airlines representing some 290 airlines or 82% of total air traffic. ",clr='y')
        clrprint("IATA supports many aviation activity and help formulate industry policy on critical aviation issues.",clr='y')
#####################################################################################################################################################################
    elif opt==2:
        time.sleep(0.5)
        clrprint('\t\t    WELCOME TO THE IATA AIRPORTS FINDER',clr='y')
        clrprint('\t\tWe provide data for more than 7200 Airports',clr='default')
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        print(df)
        
        mal=clrinput('What do u want to do (add or remove or show):',clr='g')
        mal=mal.upper()
        if mal=='ADD':
           newcode=input('Code:')
           newcode=newcode.upper()
           newairport=input('airport:')
           newlocation=input('location:')
           newcountry=input('Country:')
           newrow=[newcode,newairport,newlocation,newcountry]
           clrprint('IATA record added!\nThank you for helping us improve!!',clr='r')
           #drop command for append csv
           row_contents = [newcode,newairport,newlocation,newcountry]
           append_list_as_row('iatafinal.csv', row_contents)
           df=pd.read_csv("D:\\School\\IP\\IPP\\iatafinal.csv",encoding="ISO-8859-1")
           
        elif mal=='REMOVE':
            del_iata=input(str('Insert the iataCode to remove:'))
            del_iata=del_iata.upper()
            #drop command for drop csv
            for(row_index,row_value) in df.iterrows():
                for idel in row_value:
                    if del_iata==idel:
                       yon=clrinput('Are you sure u want to remove yes/no:',clr='p')
                       yon=yon.upper()
                       if yon=='YES':
                                 df=df.drop([row_index],axis=0)
                                 clrprint(row_index,'has been deleted',clr='y')
                                 df.to_csv("D:\\School\\IP\\IPP\\iatafinal.csv",index=False)
                       else:
                           clrprint('Nothing has been removed',clr='r')
                           break
            else:
                clrprint('IATA record removed!\nThank you for helping us improve!!',clr='r')

        elif mal=='SHOW':
            while True:
                clrprint("\nTo exit enter 'exit'",clr='red')
                iata=(clrinput("IATA CODE:",clr='m'))
                iata=iata.upper()
                
                pd.set_option('display.max_columns', 500)
                pd.set_option('display.width', 1000)
                sh=df['iataCode']== iata
                a=df[sh]
                if iata == 'EXIT':
                    break
                elif a.empty==True:
                    clrprint("\t\t\tAirport not Found ! Please enter another IATA code",clr='r')    
                else:
                    time.sleep(0.5)
                    print(a)       
####################################################################################################################################################################3
    elif opt==3:
        time.sleep(1)
        clrprint('\t\tWelcome to the Passenger Statistics of the Top 10 Airports!',clr='y')
        df=pd.read_csv("D:\\School\\IP\\IPP\\airports1.csv")
        time.sleep(1)
        clrprint("\nAvailaible Airport Statistics:\n",clr='r')
        time.sleep(1)
        print(df)
        
        while True:
            time.sleep(0.5)
            Code=clrinput("\nTo go back to main menu, press any key or enter Enter the IATA Code of the airport:",clr='m')
            Cod=Code.upper()
            if Cod=='DXB':
                data=pd.read_csv("D:\\School\\IP\\IPP\\Dubai.csv")
                Year=data['Year']
                Passengers=data['Passengers']
                pl.xlabel('Year')
                pl.ylabel('Passengers per Year in 10 millions')
                pl.title("Yearly Passengers for Dubai")
                pl.ylim(60000000,105000000)
                pl.bar(Year,Passengers,color=['r','b','y','g','m'],width=0.6)
                print(data)
                pl.show()
            elif Cod=='ATL':
                data=pd.read_csv("D:\\School\\IP\\IPP\\Atlanta.csv")
                Year=data['Year']
                Passengers=data['Passengers']
                pl.xlabel('Year')
                pl.ylabel('Passengers per Year in 10 millions')
                pl.title("Yearly Passengers for Atlanta")
                pl.ylim(90000000,105000000)
                pl.bar(Year,Passengers,color=['r','b','y','g','m'],width=0.6)
                print(data)
                pl.show()
            elif Cod=='PEK':
                data=pd.read_csv("D:\\School\\IP\\IPP\\Beijing.csv")
                Year=data['Year']
                Passengers=data['Passengers']
                pl.xlabel('Year')
                pl.ylabel('Passengers per Year in 10 millions')
                pl.title("Yearly Passengers for Beijing")
                pl.ylim(80000000,105000000)
                pl.bar(Year,Passengers,color=['r','b','y','g','m'],width=0.6)
                print(data)
                pl.show()
            elif Cod=='HND':
                data=pd.read_csv("D:\\School\\IP\\IPP\\Tokyo.csv")
                Year=data['Year']
                Passengers=data['Passengers']
                pl.xlabel('Year')
                pl.ylabel('Passengers per Year in 10 millions')
                pl.title("Yearly Passengers for Tokyo")
                pl.ylim(60000000,105000000)
                pl.bar(Year,Passengers,color=['r','b','y','g','m'],width=0.6)
                print(data)
                pl.show()
            elif Cod=='LAX':
                data=pd.read_csv("D:\\School\\IP\\IPP\\Los Angeles.csv")
                Year=data['Year']
                Passengers=data['Passengers']
                pl.xlabel('Year')
                pl.ylabel('Passengers per Year in 10 millions')
                pl.title("Yearly Passengers for Los Angeles")
                pl.ylim(60000000,105000000)
                pl.bar(Year,Passengers,color=['r','b','y','g','m'],width=0.6)
                print(data)
                pl.show()
            elif Cod=='ORD':
                data=pd.read_csv("D:\\School\\IP\\IPP\\Chicago.csv")
                Year=data['Year']
                Passengers=data['Passengers']
                pl.xlabel('Year')
                pl.ylabel('Passengers per Year in 10 millions')
                pl.title("Yearly Passengers for Chicago")
                pl.ylim(60000000,105000000)
                pl.bar(Year,Passengers,color=['r','b','y','g','m'],width=0.6)
                print(data)
                pl.show()
            elif Cod=='LHR':
                data=pd.read_csv("D:\\School\\IP\\IPP\\London.csv")
                Year=data['Year']
                Passengers=data['Passengers']
                pl.xlabel('Year')
                pl.ylabel('Passengers per Year in 10 millions')
                pl.title("Yearly Passengers for London Heathrow")
                pl.ylim(70000000,80000000)
                pl.bar(Year,Passengers,color=['r','b','y','g','m'],width=0.6)
                print(data)
                pl.show()
            elif Cod=='HKG':
                data=pd.read_csv("D:\\School\\IP\\IPP\\Hong Kong.csv")
                Year=data['Year']
                Passengers=data['Passengers']
                pl.xlabel('Year')
                pl.ylabel('Passengers per Year in 10 millions')
                pl.title("Yearly Passengers for Hong Kong")
                pl.ylim(50000000,80000000)
                pl.bar(Year,Passengers,color=['r','b','y','g','m'],width=0.6)
                print(data)
                pl.show()
            elif Cod=='PVG':
                data=pd.read_csv("D:\\School\\IP\\IPP\\Shangai.csv")
                Year=data['Year']
                Passengers=data['Passengers']
                pl.xlabel('Year')
                pl.ylabel('Passengers per Year in 10 millions')
                pl.title("Yearly Passengers for Shanghai")
                pl.ylim(40000000,80000000)
                pl.bar(Year,Passengers,color=['r','b','y','g','m'],width=0.6)
                print(data)
                pl.show()
            elif Cod=='CDG':
                data=pd.read_csv("D:\\School\\IP\\IPP\\Paris.csv")
                Year=data['Year']
                Passengers=data["Passengers"]
                pl.xlabel("Year")
                pl.ylabel("Passengers per Year in 10 millions")
                pl.title("Yearly Passengers for Paris")
                pl.ylim(60000000,70000000)
                pl.bar(Year,Passengers,color=['r','b','y','g','m'],width=0.6)
                print(data)
                pl.show()
            else:
                break
        else:
            break
#####################################################################################################################################################################
    elif opt == 4:
        ds =pd.read_csv("D:\\School\\IP\\IPP\\pie.csv",encoding="ISO-8859-1")
        csfont = {'fontname':'Comic Sans MS'}
        lab=ds['Category']
        s = (0.05, 0.2, 0.2, 0.2,0.2,0.2)
        patches, texts=pl.pie(ds['Total Number'],explode=s,shadow=False, startangle=90,wedgeprops   = { 'linewidth' : 0.5, 'edgecolor' : "black" },frame= True)
        pl.legend(patches, lab, loc="best")
        pl.title('Different types of airports in the world',**csfont,size=12,color='r')
        pl.axis('equal')
        time.sleep(0.5)
        pl.show()

        object=('JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC')
        x_pos=np.arange(len(object))
        y=[80,72,55,38,71,63,94,90,99,86,83,91]
        pl.plot(x_pos,y,color='b')
        pl.xticks(x_pos,object)
        pl.xlabel("Months")
        pl.ylabel("Passenger Traffic in %")
        pl.grid(True)
        pl.title("Monthly Passenger Traffic (2019)")
        pl.show()

#####################################################################################################################################################################
    elif opt == 5:
        print("Find airports and track flights")
        arp=input("IATA CODE:")
        s=arp.lower()
        clrprint("Realtime global flight tracking ",clr='r')
        clrprint("Source: www.flightradar24.com",clr='r')
        time.sleep(4)
        webbrowser.open(("https://www.flightradar24.com/airport/"+s))
    elif opt == 6:
        time.sleep(1)
        clrprint("Thank you for using IATA DATA guide !",clr='r')
        clrprint("See you soon !",clr='r')
        break

