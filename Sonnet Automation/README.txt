This programme was developed by Cathal McAleer and Colm Bracken on  in order to facilitate the quick automation of data retrieval from the Electromagnetic Simulation Software package Sonnet.
The programme may be used for other EM simulation software that exports .csv data files.

This code dictated as OpenSource by it's authors on 22/10/21 and may be used for any use.

The only edit of the code required by the author is a change in file directory on line 40.

The programme imports a .csv file and exports for each parameter sweep: parameter title, resonant frequency and S21 magnitude.

****************************************************************************************************************************
WARNING:
The only bug detected with this programme is the user MUST manually go into the .csv file exported by Sonnet and save it. This bug is believed to be due to Sonnet's file exportation protocol.
****************************************************************************************************************************

A test .csv file named "Test MKID Finger Length" was simulated from Sonnet using a Microwave Kinetic Inductance Detector structure (shown in MKID_Diagram.png) which includes S-parameters and demonstrates the python script capability.
This file only contains the required data for this python script to conserve file size to upload to github.com, however the titles for the other S-Params are left in the file.
This code may be editted to import other file formats from other EM simulation programmes by similar methods.