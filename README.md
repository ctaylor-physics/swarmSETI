# swarmSETI
Project to conduct SETI searches using observations with the LWA Swarm

# Steps for REU Student:
1. Select a target from the list Savin provided or from what I have gathered from cross-matching NASA Exoplanets with VLASS 74 MHz sources
   - We would like to be able to use in-beam calibration
   - For the above, the student should be able to make a written argument as to why this target(s) are a good candidate.
2. Schedule and monitor the observation for problems, through correlation of the data.
3. Assemble Savin's pipeline into a single executable such that: Input => metadata tarball
   1. Script finds all of the raw data files
   2. Turns them into HDF5 files
   3. Aligns them in time as best as possible
   4. Chop them into chunks to run the drifting signal finder (bliss)
   5. Performs anti-coincidence on the hits produced across all three stations (if none found in all three, try just LWA1-LWASV, LWA-NA could see local RFI w/ LWA1)
   6. Produce .png files of the hits (including all 3 stations regardless)
4. Manually or Automated inspection of the hits to determine which are worth follow-up
5. Attempt to determine if the signal is local in origin or a potential SETI candidate
