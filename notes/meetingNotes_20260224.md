**INTRO**

Savin Varghese and Tanvi Kulkarni started this first experiment using FRB triggered data to search for technosignatures. This resulted in a relatively small dataset of observations to process using the methods described below: 

Savin's code and data are available at lwaucf3 
 - Code: /data/local/savin/seti/scripts/
 - Data: /data/network/recent_data/savin/drx_seti/

Important points: 
 - Data was sampled at $\nu = 2 \ Hz$, $t_{acc} = 3 / seconds$ using the hdfWaterfall.py code from the commissioning package. Something like 8e6 point fft?
 - Most of the SETI codes take a generic dynamic spectra that is in the 'Blimpy' format (whatever that is).
 - The above locations detail where the code to do this is.

General Workflow: 
 - Observe 
 - Convert to desired resolution w/ hdfWaterfall.py via upchannelize scripts code directory 
 - Use Savin's read_lwa-hdf5.py to split tunings into 'FILTERBANK' files  
 - run these split files on turboseti/seticore/bliss  
 - Anticoincidence check between stations 
 - Generate pngs for quicklooking AND make barycentric correction to hits if found (or if required) 
 - Hits that remain are to be inspected by an algorithm/criteria that is tbd. 

