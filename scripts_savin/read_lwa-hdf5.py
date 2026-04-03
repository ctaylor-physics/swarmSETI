import sys
import os
import h5py
import numpy as np
from lsl import astro as ast

filename = sys.argv[1]


hf = h5py.File(filename,'r')

#File start with an observation1 key which has several observation headers
obs_hdrs = hf['Observation1'].attrs.keys()
#[u'ObservationName', u'TargetName', u'tInt', u'tInt_Unit', u'LFFT', u'nChan', u'RBW', u'RBW_Units', u'RA', u'RA_Units', u'Dec', u'Dec_Units', u'Epoch', u'TrackingMode', u'ARX_Filter', u'ARX_Gain1', u'ARX_Gain2', u'ARX_GainS', u'Beam', u'DRX_Gain', u'sampleRate', u'sampleRate_Units']

time_hdr = hf['Observation1/time'].attrs.keys()
time = hf['Observation1/time']

#Times in unix time stamps
t0 = time[0][0]+time[0][1]

t0_mjd = ast.jd_to_mjd(ast.unix_to_utcjd(t0))



#Each observation has Tuning1, Tuning2 and time keys
#Each Tuning has the following keys. Time has 2 attributes but tuning does not have any attributes
# [u'I', u'Q', u'Saturation', u'U', u'V', u'freq']

idset1  = hf['Observation1/Tuning1/I']
idset2 = hf['Observation1/Tuning2/I']

#dataset attributes: [u'axis0', u'axis1']

#Frequencies will be different for each tuning and needs to be accessed seperately
#Converting to MHz
freq_tun1 = (hf['Observation1/Tuning1/freq'][()])/1e+6
freq_tun2 = (hf['Observation1/Tuning2/freq'][()])/1e+6

print(hf['Observation1/Tuning1'].keys())
#print(hf.attrs())
print(idset1.shape)
print(freq_tun1.shape)




#Now write them into a different files each with different tunings
# First tuning
outfile1 = os.path.splitext(os.path.basename(filename))[0]+"_tun1.h5"
print(outfile1)


hf1 = h5py.File(outfile1,"w")

hf1.attrs['CLASS'] = 'FILTERBANK'
hf1.attrs['VERSION'] = '1.0'

d1shape = (idset1.shape[0], 1, idset1.shape[1])
chunk_shape = (1, 1, idset1.shape[1])
print(d1shape)

dset1 = hf1.create_dataset("data", shape = d1shape, dtype = idset1.dtype)
#dset1 = hf1.create_dataset("data", shape = d1shape, chunks = chunk_shape, dtype = idset1.dtype)
#dset1 = hf1.create_dataset("data", shape = (327,1,12000), dtype = "float32")

dset1_mask = hf1.create_dataset("mask", shape = d1shape,  dtype = "uint8")
#dset1_mask = hf1.create_dataset("mask", shape = d1shape, chunks = chunk_shape, dtype = "uint8")

dset1.dims[2].label = b"frequency"
dset1.dims[1].label = b"feed_id"
dset1.dims[0].label = b"time"

dset1_mask.dims[2].label = b"frequency"
dset1_mask.dims[1].label = b"feed_id"
dset1_mask.dims[0].label = b"time"


dset1[:,0,:] = idset1
dset1_mask[:,0,:] = np.zeros(idset1.shape, dtype = 'uint8')

#Adding attributes now
#u'machine_id', u'telescope_id', u'src_raj', u'src_dej', u'az_start', u'za_start', u'data_type', u'fch1', u'foff', u'nchans', u'nbeams', u'ibeam', u'nbits', u'tstart', u'tsamp', u'nifs', u'source_name', u'rawdatafile']

#dset1.attrs['DIMENSION_LABELS'] = np.array(['time', 'feed_id', 'frequency'], dtype=object)
dset1.attrs['machine_id'] = 0
dset1.attrs['telescope_id'] = -1
dset1.attrs['src_raj'] = hf['Observation1'].attrs['RA']
dset1.attrs['src_dej'] = hf['Observation1'].attrs['Dec']
dset1.attrs['az_start'] = 0
dset1.attrs['za_start'] = 0
dset1.attrs['data_type'] = 1
dset1.attrs['fch1'] = freq_tun1[0]
dset1.attrs['foff'] = freq_tun1[1] - freq_tun1[0]
dset1.attrs['nchans'] = hf['Observation1'].attrs['nChan']
dset1.attrs['nbeams'] = 1
dset1.attrs['ibeam'] = -1
dset1.attrs['nbits'] = 32
dset1.attrs['tstart'] = t0_mjd
dset1.attrs['tsamp'] = hf['Observation1'].attrs['tInt']
dset1.attrs['nifs'] = 1
dset1.attrs['source_name'] = hf['Observation1'].attrs['TargetName']
dset1.attrs['rawdatafile'] = os.path.basename(filename).split('-')[0]

hf1.close()

#Now write them into a different files each with different tunings
# Second tuning
outfile2 = os.path.splitext(os.path.basename(filename))[0]+"_tun2.h5"
print(outfile2)


hf2 = h5py.File(outfile2,"w")

hf2.attrs['CLASS'] = 'FILTERBANK'
hf2.attrs['VERSION'] = '1.0'

d2shape = (idset2.shape[0], 1, idset2.shape[1])
chunk_shape = (1, 1, idset2.shape[1])
print(d2shape)

dset2 = hf2.create_dataset("data", shape = d2shape, dtype = idset2.dtype)

dset2_mask = hf2.create_dataset("mask", shape = d2shape,  dtype = "uint8")

dset2.dims[2].label = b"frequency"
dset2.dims[1].label = b"feed_id"
dset2.dims[0].label = b"time"

dset2_mask.dims[2].label = b"frequency"
dset2_mask.dims[1].label = b"feed_id"
dset2_mask.dims[0].label = b"time"


dset2[:,0,:] = idset2
dset2_mask[:,0,:] = np.zeros(idset2.shape, dtype = 'uint8')

#Adding attributes now
#u'machine_id', u'telescope_id', u'src_raj', u'src_dej', u'az_start', u'za_start', u'data_type', u'fch1', u'foff', u'nchans', u'nbeams', u'ibeam', u'nbits', u'tstart', u'tsamp', u'nifs', u'source_name', u'rawdatafile']

#dset2.attrs['DIMENSION_LABELS'] = np.array(['time', 'feed_id', 'frequency'], dtype=object)
dset2.attrs['machine_id'] = 0
dset2.attrs['telescope_id'] = -1
dset2.attrs['src_raj'] = hf['Observation1'].attrs['RA']
dset2.attrs['src_dej'] = hf['Observation1'].attrs['Dec']
dset2.attrs['az_start'] = 0
dset2.attrs['za_start'] = 0
dset2.attrs['data_type'] = 1
dset2.attrs['fch1'] = freq_tun2[0]
dset2.attrs['foff'] = freq_tun2[1] - freq_tun2[0]
dset2.attrs['nchans'] = hf['Observation1'].attrs['nChan']
dset2.attrs['nbeams'] = 1
dset2.attrs['ibeam'] = -1
dset2.attrs['nbits'] = 32
dset2.attrs['tstart'] = t0_mjd
dset2.attrs['tsamp'] = hf['Observation1'].attrs['tInt']
dset2.attrs['nifs'] = 1
dset2.attrs['source_name'] = hf['Observation1'].attrs['TargetName']
dset2.attrs['rawdatafile'] = os.path.basename(filename).split('-')[0]

hf2.close()

hf.close()


