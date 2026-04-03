# Given a tarball file, find out the corresponding drx file from the .csv list we have
# use hdfWaterfall.py to upchannelize and average the data

import os
import glob
import csv

#Directory with .tgz files
tar_path = '/data/network/recent_data/savin/alltar/DD002_90[5,6,7]*.tgz'

#Directory with drx data
drx_path = '/data/network/recent_data/savin/drx_seti/' 

tarballs = sorted(glob.glob(tar_path))

#Getting metadata info from csv file

metacsv1 = '/data/local/savin/seti/scripts/metadata_lwa1.csv'
metacsv2 = '/data/local/savin/seti/scripts/metadata_lwa-sv.csv'

metafiles1 =[]
beam_ids1 = []
drx_files1 = []

with open(metacsv1, mode='r') as csv_file1:
    csv_reader1 = csv.DictReader(csv_file1)
    for line in csv_reader1:
        metafile1 = line['tarball']
        beam_id1 = line['beamid']
        drx_file1 = line['datafile']

        metafiles1.append(metafile1.lstrip())
        beam_ids1.append(beam_id1)
        drx_files1.append(drx_file1.lstrip())

metafiles2 =[]
beam_ids2 = []
drx_files2 = []

work_dir = os.getcwd()

with open(metacsv2, mode='r') as csv_file2:
    csv_reader2 = csv.DictReader(csv_file2)
    for line in csv_reader2:
        metafile2 = line['tarball']
        beam_id2 = line['beamid']
        drx_file2 = line['datafile']

        metafiles2.append(metafile2.lstrip())
        beam_ids2.append(beam_id2)
        drx_files2.append(drx_file2.lstrip())

for tarball in tarballs:
    
    tarball_base = os.path.basename(tarball)
    
    if tarball_base in metafiles1:
        ind = metafiles1.index(tarball_base)
        datafile = drx_files1[ind]
        datafile_path = drx_path + datafile 
        print(f"Data from LWA1, metafile : {tarball_base}, datafile: {datafile_path}")
        
        if os.path.exists(datafile_path):
            cmd1 = f'/usr/local/extensions/Commissioning/DRX/HDF5/hdfWaterfall.py -a 3.0 -l 8388608 -m {tarball} -k {datafile_path}'
            os.system(cmd1)

            waterfall_file = os.path.join(work_dir, os.path.basename(datafile_path)+'-waterfall.hdf5')
            print(waterfall_file)
            
            if os.path.exists(waterfall_file):
                print("Starting the converstion of hdf5 file into the blimpy format for the seti search")
                cmd2 = f"python3 /data/local/savin/seti/scripts/read_lwa-hdf5.py {waterfall_file}"
                os.system(cmd2)
                
                print("conversion finished")
                print("removing the original hdf5 file")
                os.remove(waterfall_file)

            else:
                print("Waterfall file is not produced, check the raw file/scripts")

        else:
            print("datafile does not exists")

    elif tarball_base in metafiles2:
        ind = metafiles2.index(tarball_base)
        datafile = drx_files2[ind]
        datafile_path = drx_path + datafile
        print(f"Data from LWA-SV, metafile : {tarball_base},  datafile : {datafile_path}")
        
        if os.path.exists(datafile_path):
            cmd1 = f'/usr/local/extensions/Commissioning/DRX/HDF5/hdfWaterfall.py -a 3.0 -l 8388608 -m {tarball} -k {datafile_path}'
            os.system(cmd1)
            
            waterfall_file = os.path.join(work_dir, os.path.basename(datafile_path)+'-waterfall.hdf5')
            print(waterfall_file)
            if os.path.exists(waterfall_file):
                print("Starting the converstion of hdf5 file into the blimpy format for the seti search")
                cmd2 = f"python3 /data/local/savin/seti/scripts/read_lwa-hdf5.py {waterfall_file}"
                os.system(cmd2)

                print("conversion finished")
                print("removing the original hdf5 file")
                os.remove(waterfall_file)

        else:
            print("datafile does not exists")
    
    else:
        print("The metafile is not in the common 2 station list")



























