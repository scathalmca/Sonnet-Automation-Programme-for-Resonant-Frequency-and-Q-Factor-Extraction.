# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 15:13:01 2021

@author: Cathal McAleer
Description:
    This programme allows the user to import a .csv file from the \
    EM simulation software Sonnet, extracts and prints the S-Parameters;\
    Parameter titles, Resonant Frequency and Magnitude at S21 from the file.
"""

#............................................................................#
#Importing libraries
import csv

#...........................................................................#
#Lists to append to

all_Mag = [] #list for entire row of Mag in excel file
all_Freq=[] #list for entire row of Freq in excel file
Param=[] #List for reading all dimension parameters 


min_mag = [] #Actual magnitude values for resonant freq of each sweep
ac_res_freq = [] #Actual resonant frequencies list of each sweep
title=[] #Actual Parameter titles for each sweep
forloop=[0] #number of frequencies being scanned

#............................................................................#
#Only input into code
print("\nThis programme allows the user to import a .csv file from Sonnet\
 and exports the parameters swept, resonant frequencies and corresponding\
 magnitudes from the file.")



#...........................................................................#

#File directory where file is imported
with open('C:\\Users\\35385\\Desktop\\Sonnet Automation\\Test MKID Finger Length.csv',\
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
    
    c=forloop[n]+9*n+8
    
    if c==8:
        start=Param[8]
        title.append(start)
        
    else:
        
        start=Param[forloop[n]+9*n+9]
        title.append(start)
        
            
    minimum_db = min(num_mag)
    min_mag.append(minimum_db)
        
    #Finding corresponding res. frequency in list
    for t in range(len(num_mag)):
        
        if num_mag[t]==minimum_db:
            #Append all resonant frequencies to empty list
            ac_res_freq.append(b[t]) 
            
        else:  #else, continue code
            continue

#.........................Printing Table of Results.........................#
#Print titles 
print("\n{:<8}{:>25}{:>12}".format("Parameter(\u03BCm)", "Res.Freq(GHz)"\
                                   ,"Mag S21(dB)"))


#Print resonant frequencies and magnitudes for each parameter swept.
for i in range(len(title)):
    print("{}{:>16}{:>16}".format(title[i],ac_res_freq[i],min_mag[i]))
    
    
#outputting values to a txt file
"""
out_file=open("Outfile.txt", "w")

for i in range(len(title)):
    if i % 2== 0:
        print(ac_res_freq[i], file=out_file)
        
    else:
        continue
    
out_file.close()
"""    
#End of prog
#...........................................................................#
