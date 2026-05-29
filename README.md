# swarmSETI
Project to conduct SETI searches using observations with the LWA Swarm. This project is an extension of a hitherto unpublished project by Savin Varghese and Tanvi Kulkarni to process Fast radio burst (FRB) observations from two LWA stations. Allowing for anti-coincidence verification of candidate detections and an exploration of the lowest frequency regime for SETI science. 

# Goals
The goals of this project are as follows:
 - Rebuild Savin's codebase into a pipeline that can injest a tarball from the interferometry pipeline that breaks observations into the necessary parts to be run with bliss, run bliss on the filterbank files, then process the hits for nti-coincidence across the three stations. The final data products are tbd, but generally should be some form of stamp file with an associated plot for visual inspection.
 - Assemble the resulting code into a github repository
 - Write an LWA Memo and/or a research note to summarize the project with a doi.
 - Find Technosignatures at low frequency. 

# Steps for REU Student:
1. Select a target from the list Savin provided or from what I have gathered from cross-matching NASA Exoplanets with VLASS 74 MHz sources
   - We would like to be able to use in-beam calibration
   - For the above, the student should be able to make a written argument as to why this target(s) are a good candidate.
2. Schedule and monitor the observation for problems, through correlation of the data.
3. Write a script to read interferometry metadata files such that a raw datafile can be subdivided into individual scans on the target field. This process breaks a long observation (6-8hrs) into bite-sized pieces that can individually be searched for technosignatures. 
4. Assemble Savin's pipeline into a single executable such that: Input => metadata tarball
   1. Script finds all of the raw data files
   2. Turns them into HDF5 files
   3. Aligns them in time as best as possible
   4. Chop them into chunks to run the drifting signal finder (bliss)
   5. Performs anti-coincidence on the hits produced across all three stations (if none found in all three, try just LWA1-LWASV, LWA-NA could see local RFI w/ LWA1)
   6. Produce .png files of the hits (including all 3 stations regardless)
5. Manually or Automated inspection of the hits to determine which are worth follow-up
6. Attempt to determine if the signal is local in origin or a potential SETI candidate

# Tentative Timeline:
May 29
-  LWA login credentials working
-  Get workspace set up on hercules/cluster to do tutorials
-  Get TOPCAT installed to retrieve tables of sources
-  Start working on target selection (need a crash course in interferometer calibrator sources), maybe in Callingham introduction?
-  Get setup with a coding environment, such as VS Code or Jupyter

June 5th
-  Practice scheduling an interferometry run (~10-15 minutes, two sources?)
-  Write own code to compare source locations, there is a snippet of code above but the files are on my personal machine
-  Start working through the LWA Jupiter, Solar, and CGP tutorials (make note of what we learned along the way)

June 12th - Spring Quarter ends
-  Start working on reorganizing the codebase that Savin has created
-  Take a look at what is in the notes folder on the github page and read through the descriptions of the code that is contained within.

June 19th - Week I am gone
-  First full testing of the pipeline w/ FRB or new data

June 26th (Halfway Mark)
-  Scheduling 8hr Observing Campaign (we could move this up). 
-  Break up raw data into individual scans
-  Start running reduction pipeline on data
-  Have dat file of hits

July 3rd 
-  Do anti-coincidence comparison between three stations. 

July 9
-  Classifying candidates signals
-  Identify best candidates for poster and make fancy plots
	-  if no detections, work on computing a sensitivity limit. 

--- GOAL July 16th (2 Weeks to go) = DONE with science
-  finish poster (we'll have to double check what the lead time for printing is w/ Chris)
-  Write up the work and finalize the github project page. 
