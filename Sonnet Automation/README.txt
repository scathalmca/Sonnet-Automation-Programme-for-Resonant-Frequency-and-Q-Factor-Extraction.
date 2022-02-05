This programme was developed by Cathal McAleer and Colm Bracken from Dept. of Experimental Physics, Maynooth Univeristy, Ireland, in order to facilitate the quick automation of data retrieval from the Electromagnetic Simulation Software package Sonnet.

The programme may be used for other EM simulation software that exports .csv data files with simple edits to the code including the file reading library and columns in which frequency and S21 data is stored. However, it should be noted that currently, the program skips the first 8 rows in the data file as these rows are saved for comments from Sonnet.

This code dictated as OpenSource by it's authors on 22/11/21 and may be used for any use.

The only edit of the code required by the author is a change in file directory on line 39, in which the user must enter the file directory of the .csv data file being used.

The programme imports a .csv file and exports for each parameter sweep: parameter title, resonant frequency and Q_c factor.

A test .csv file named "Test MKID Finger Length.csv" was simulated from Sonnet using a Microwave Kinetic Inductance Detector structure (shown in MKID_Diagram.png) which includes S-parameters and demonstrates the python script capability.

This file only contains the required data for this python script to conserve file size to upload to github.com, however the titles for the other S-Params are left in the file.

For enquires, email: cathal.mcaleer@mu.ie
