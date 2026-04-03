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
