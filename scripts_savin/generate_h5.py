#Generating a simulated h5 file for a LWA dataset

from astropy import units as u
import setigen as stg
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('Tkagg')

nchans = 8388608
n_coarse = 1
tbins = 20
df =  2.336502070932056*u.Hz   
dt = 2.9959314285714287*u.s   

fch1 = 53.499999962560835*u.MHz   
drift_rate = 0*u.Hz/u.s
width = 1*u.Hz
snr = 100

frame = stg.Frame(fchans = nchans*n_coarse, tchans = tbins, df = df, dt = dt,
                  fch1 = fch1, ascending = True)

noise = frame.add_noise(x_mean=5)


signal = frame.add_signal(stg.constant_path(f_start=frame.get_frequency(216051),
                                            drift_rate=drift_rate),
                          stg.constant_t_profile(frame.get_intensity(snr=snr)),
                          stg.box_f_profile(width=width),
                          stg.constant_bp_profile(level = 1))






#frame.save_h5(filename='data_setigen_check.h5')
frame.save_fil(filename='data_setigen_check.fil')
