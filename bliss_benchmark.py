import pandas as pd
import numpy as np
import os
import glob
import matplotlib.pyplot as plt
import hdf5plugin
import h5py

def filter_Lband_RFI(df):
    start_freq = np.array([1525.5,1545.8,1552.5,1560,1563.5,1566,1568.8,1570.5,1571.5,1573.5,1598,1598.8,1601.5,1679.6,1681.3])
    stop_freq =  np.array([1537,1551.5,1556,1562.5,1565,1566.5,1569.8,1571,1572,1582,1598.5,1599.7,1604.5,1680.1,1681.7])
    for start, stop in zip(start_freq, stop_freq):
        df = df[~df['Corrected_Frequency'].between(start,stop)]
    return df

DIR = '/home/cat-work/work/SETI/swarmSETI/bliss_benchmark'
h5data_fn = os.path.join(DIR,"power_law_blc73_guppi_58832_16209_MESSIER031_0057.rawspec.0000.h5")

# ## Reading in the injected signals:
hd = h5py.File(h5data_fn)
# spectra = hd['data']
# fch1 = spectra.attrs['fch1']
# foff = spectra.attrs['foff']
# dset = spectra[:]
# freq = np.arange(fch1, fch1 + foff*dset.shape[-1], foff)

#Setigen stuff
setigen = hd['setigen']
drift_rate = np.array(setigen['drift_rate'])
signal_frequency = np.array(setigen['start_frequency'])
gen_srn = np.array(setigen['zscore'])

benchmark_files = sorted(glob.glob(DIR + "/m31_benchmark_hits_*.dat"))
datfile_cols = ["Drift_Rate","SNR","Uncorrected_Frequency","Corrected_Frequency","Index","freq_start","freq_end","SEFD_freq1","SEFD_freq2","Coarse_Channel_Number","Full_number_of_hits"]
benchmark_rs1 = pd.read_csv(benchmark_files[0],sep='\t', header=8, names=datfile_cols)
benchmark_L30 = pd.read_csv(benchmark_files[1],sep='\t', header=8, names=datfile_cols)
benchmark_rs3 = pd.read_csv(benchmark_files[2],sep='\t', header=8, names=datfile_cols)
benchmark_rs5 = pd.read_csv(benchmark_files[3],sep='\t', header=8, names=datfile_cols)
benchmark_snr8 = pd.read_csv('/home/cat-work/work/SETI/swarmSETI/bliss_benchmark/m31_benchmark_snr8.dat',sep='\t', header=8, names=datfile_cols)

for set in [benchmark_rs1, benchmark_L30, benchmark_rs3, benchmark_rs5, benchmark_snr8]:
    filtered_set = filter_Lband_RFI(set)

    ## Plot
    fig, ax = plt.subplots(1,1, sharex=True, constrained_layout=True)
    ax.scatter(signal_frequency, gen_srn, s=5, c='k', label='Inj. Signals')
    ax.scatter(filtered_set['Corrected_Frequency'], filtered_set['SNR'], s=3, c='r', label='Recovered')
    ax.set_title('Ground Truth vs Benchmark')
    ax.set_xlabel('signal frequency (MHz)')
    ax.set_ylabel('SNR')
    ax.set_ylim(0,100)
    plt.legend()
    plt.show()

## Running this code, I don't understand what I even am getting back to be honest....