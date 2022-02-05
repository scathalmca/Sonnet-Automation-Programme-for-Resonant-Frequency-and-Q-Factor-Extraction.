# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 15:13:01 2021

@author: Cathal McAleer
Description:
    This programme allows the user to import a .csv file from the \
    EM simulation software Sonnet, extracts and prints;\
    Parameter titles, Resonant Frequency and Quality Factor from the file.
"""

#............................................................................#
#Importing libraries
import csv
from scipy.interpolate import splev, splrep, sproot
import numpy as np


#...........................................................................#
#Lists to append to

all_Mag = [] #list for entire row of Mag in excel file
all_Freq=[] #list for entire row of Freq in excel file
Param=[] #List for reading all dimension parameters 

ac_res_freq = [] #Actual resonant frequencies list of each sweep
title=[] #Actual Parameter titles for each sweep
forloop=[0] #number of frequencies being scanned
Qual_Fac=[] #list to append Quality Factor values to for each parameter
#............................................................................#
#Only input into code
print("\nThis programme allows the user to import a .csv file from Sonnet\
 and exports the parameters swept, resonant frequencies and corresponding\
 quality factor from the file.")

#...........................................................................#

#File directory where file is imported
with open("C:\\Users\\Test MKID Finger Length.csv",\
          "r") as csvfile:
    
    csvReader=csv.reader(csvfile)
          
    for row in csvReader:
        
        try:
            Param.append(row[0]) #Read entire first row
            all_Freq.append(float(row[0])) #Read in first row of values
            all_Mag.append(float(row[5])) #Read in 6th row of values
            
            
        except ValueError: #for Freq and mag. If row isn't a float, continue
            continue
        
End_Freq = max(all_Freq)
#looping through each value of frequencies

for i in range(len(all_Freq)):
    
    a=all_Freq[i] 
    
    
    if a==End_Freq: #if a = end of frequency sweep. 
    #Get's # of frequencies swept by Sonnet
        
        forloop.append(i) #append to forloop list
        
    else:
        continue

#number of sweeps performed = elemenets in forloop list - 1 
num_of_sweeps=len(forloop)-1

#Main prog

for n in range(0,num_of_sweeps):
    
    b=all_Freq[forloop[n]+1:forloop[n+1]+1]
    
        
    num_mag = all_Mag[forloop[n]+1:forloop[n+1]+1]
    
    dB = np.empty(len(num_mag)) #Actual magnitude values for resonant freq of each sweep
    c=forloop[n]+9*n+8
    
    if c==8:
        start=Param[8]
        title.append(start)
        
    else:
        
        start=Param[forloop[n]+9*n+9]
        title.append(start)
     
    #converting magnitude to Decibels
    for t in range(len(num_mag)):
        dB[t]=20*np.log10(num_mag[t])
            
    minimum_db = min(dB) #minimum S21 corresponding to res. frequency
    HM=(dB[0]+minimum_db)/2 #Half-width of dip   
    
    #Spline interpolate data to obtain roots at 
    tck=splrep(b, dB) # spline coeff returned as a tuple
    y_output = splev(b, tck)
    
    #Move data from y=HM to y=0 and solve roots for x
    tck2=splrep(b, y_output-HM)
    
    x=sproot(tck2)#Roots (I.e points at Half-Max)
    
    FWHM=x[1]-x[0] #Full width-Half-Maximum
    

    #Finding corresponding res. frequency in list
    for t in range(len(dB)):
        if dB[t]==minimum_db:
            #Append all resonant frequencies to empty list
            ac_res_freq.append(b[t])
            
            #Append quality factor (res.freq/Fullwidth-halfmax)
            Qual_Fac.append(b[t]/FWHM)

        else:  #else, continue code
            continue

#.........................Printing Table of Results.........................#

#Print titles 
print("\n{:<8}{:>25}{:>20}".format("Parameter(\u03BCm)", "Res.Freq(GHz)"\
                                   ,"Quality Factor"))
for i in range(len(ac_res_freq)):
    
    print("\n{:<8}{:>20.4f}{:>20.2f}".format(title[i], ac_res_freq[i]\
                                       ,Qual_Fac[i]))
        

#...........................................................................#
