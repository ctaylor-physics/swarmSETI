import pandas as pd
import numpy as np

benchmark_file = '/home/cat-work/work/SETI/swarmSETI/bliss_benchmark/m31_benchmark_hits.dat'
benchmark_file2 = '/home/cat-work/work/SETI/swarmSETI/bliss_benchmark/m31_benchmark_hits2.dat'

benchmark = pd.read_csv(benchmark_file,sep='\t', header=8, names=["Drift_Rate","SNR","Uncorrected_Frequency","Corrected_Frequency","Index","freq_start","freq_end","SEFD_freq1","SEFD_freq2","Coarse_Channel_Number","Full_number_of_hits"])
benchmark2 = pd.read_csv(benchmark_file2,sep='\t', header=8, names=["Drift_Rate","SNR","Uncorrected_Frequency","Corrected_Frequency","Index","freq_start","freq_end","SEFD_freq1","SEFD_freq2","Coarse_Channel_Number","Full_number_of_hits"])