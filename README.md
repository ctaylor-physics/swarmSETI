# swarmSETI - Project Description
The search for extraterrestrial intelligence (SETI) is conducted across the electromagnetic spectrum to understand the distribution of intelligent life in the universe and seek the answer to the profound question, Are we alone in the Universe? At radio frequencies, this effort focuses on searching for “technosignatures”, observable indicators of technological emissions consistent with our understanding of an advanced civilization. Historically, the microwave regime from 1-10GHz has been the primary frequency range searched for these technosignatures, but recent SETI experiments utilizing low frequency radio telescopes, such as the LOw Frequency Array (LOFAR) and the Murchison Widefield Aray, have begun probing the insufficiently studied frequency range below 1 GHz. Even so, the lowest radio frequencies (<100 MHz) have been even less explored for technosignatures, despite significant human communication signals occupying this band. 

The Long Wavelength Array (LWA) is a low frequency (3-88 MHz) interferometer array telescope collaboration comprised of dipole 'stations' distributed across the southwestern United States. This summer project will conduct a targeted search for technosignatures at 45-84 MHz using the LWA Swarm, the aperture synthesis telescope consisting of interconnected LWA Stations making joint observations as a long baseline interferometer. An earlier SETI pipeline for the LWA was build by Savin Varghese and Tanvi Kulkarni done using triggered observations of Fast Radio Bursts and older versions of the standard Breakthrough Listen drifting signal search tools (turboseti/seticore). This project will build on this work by introducing current SETI processing tools and the incorporate interferometric imaging using the newly characterized LWA Swarm telescope.  

The goals of this project are to build a data reduction pipeline for SETI science by combining existing tools in the LWA software libraries with the technosignature search software package called the Breakthrough Listen Interesting Signal Search (BLISS; https://github.com/UCBerkeleySETI/bliss). This pipeline will be designed to ingest multi-station LWA Swarm observation to search through raw voltage data for narrowband technosignatures, then perform an anti-coincidence comparison to identify unique signals that appear at geographically separate LWA stations. The kilometer scale distribution of LWA stations for these observations provides a robust basis for anti-coincidence rejection of anthropogenic signals and extraction of radio frequency interference. This new pipeline will be vetted using injection and recovery test with simulated LWA data modified by the SETI signal generator tool setigen (https://github.com/bbrzycki/setigen). 

Using the LWA Swarm, we will then conduct interferometry observations of exoplanet systems from the NASA Exoplanet archive to search for low frequency radio technosignatures. Data from each LWA station will be processed using this new SETI pipeline to identify candidate signals at coarse ($\delta \nu = 4.83$ kHz, $\delta t = 0.2$ s) and fine ($\delta \nu = 2.36$ Hz, $\delta t = 3.0$ s) channelization to provide sensitivity to narrowband or slightly broadband radio signals. Each observation will also be correlated using the ELWA Correlator, and the exoplanet fields will be imaged using standard VLBI processing techniques to search for localized technosignatures associated with each system. 

# Goals / Milestones 
The goals of this project are as follows:

**A.** Demonstrate the ability to manipulate data and write basic analysis software using standard Python libraries. Complete modules from the LWA Data Reduction Tutorials by collecting and using the LWA software stack hosted on github. Utilize the TOPCAT catalog tool to collect information on exoplanet systems and radio galaxies from different catalog references. 

**B.** Reconstruct the first iteration of the LWA SETI pipeline using up-to-date tools to streamline data processing of multi-station LWA data. Designed for ease of use, such that a single observation metadata file can be used to fully analyze a LWA Swarm run for technosignatures. 

**C.** Compile the results into a new Github repository to host the LWA SETI codebase. This should include a description of the pipeline, the associated code to process data, and the software requirements to use the reduction pipeline. 

**D.** Write an LWA Memo or Research Note summarizing the project results. Create a poster for the UNM REU Poster Session that visualizes this project.

**E.** Find intelligent alien transmissions at Low Frequency?

# Steps for REU Student:
1. Identify targets to observe using the LWA Swarm:
	- Collect the NASA Exoplanet Archive (NEA) Stellar Hosts table and the VLSSr 74 MHz Survey catalogs. 
		- Filter NEA catalog for exoplanet systems within 10pc of Earth
		- Filter the VLSSr catalog for radio sources with a Declination $> 10^\circ$ degrees and Peak Flux $>10$ Jy.
	- Cross-match these two filtered tables to find the closest 10 Jy radio source to each exoplanet system.
		- The student should identify a few sources that they think would be good candidates for this study and be able to make a small written justification as to why. (This is mostly to help with the final poster introduction).
2. Schedule and monitor the observation
	- Using the LWA session_schedules package, create a valid interferometry observing schedule for the chosen exoplanet system.
	- Upload the observing schedule to the LWA Observing File Validator & Submission Tool
	- Monitor the LWA station health leading up to the observation and ensure that the data is being delivered to the ELWA correlator in a timely manner.
	- Preserve copies of the Single Station Data so they can be processed using the SETI pipeline. 
3. Write a script to read interferometry metadata files such that a raw datafile can be subdivided into individual scans on the target field. This process breaks a long observation (6-8hrs) into bite-sized pieces that can individually be searched for technosignatures. (I'll probably help out with this step)
	- Unpack information held in a tarball for LWA observations using the metabundle tools 
	- Determine the offsets and duration of each exoplanet target field scan
	- Write them out to individual scan files or integrate this into the HDF5 conversion step below. 
4. Assemble Savin's pipeline into a single executable pipeline
   1. Find all of the raw data files associated with an interferometry tarball
   2. Subdivide each station raw data into HDF5 files for individual scans of target field
   3. Run the BLISS drifting signal finder on each target scan and compile the hits into a table for anti-coincidence comparison
	   - SNR: 6-10
	   - Drift Rate: $\pm 5$ Hz/s
   4. Performs anti-coincidence on the hits produced across all three stations with a tolerance of $\pm 10$ Hz in frequency and $\pm 0.8$ Hz/s in drift rate. 
	   - These could be adjusted a bit if we find no coincident detections
	   - If no common hits across all three, try just the comparison of LWA1-LWASV (LWA-NA could see local RFI w/ LWA1)
   5. For common hits, produce time-frequency postage stamps and save to .png files for review (include all 3 stations regardless to see difference in data quality)
5. Manually or Automated inspection of the hits to determine which, if any, are worth follow-up in more detail.
6. Attempt to determine if candidate signals are local in origin or a potential SETI candidate. 
	- Is there a known source of RFI at this frequency?
	- Is the drift rate consistent with what we would expect for an exoplanet around this star based on the orbit?
	- Was the exoplanet behind the host star at the time of this observation? (May vary significantly depending on the orbit period since we will observe over ~8 hours)
