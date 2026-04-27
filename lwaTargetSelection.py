from astroquery.vizier import Vizier
import astropy.units as u
from astropy.coordinates import SkyCoord, match_coordinates_sky
from astropy.table import Table, Column

import numpy as np
import pandas as pd



def source_separations(sk1, sk2, df1, df2):
    """
    Take two lists of SkyCoords and the parent dataframes, 
    return the nearest neighbors according to a maximum offset of 1.5 degrees
    """

    # match_coordinates_sky returns (idx, d2d, d3d); unpack explicitly
    idx, d2d, _ = match_coordinates_sky(sk1, sk2, nthneighbor=1)
    real_hits = []
    # iterate by positional index to avoid non-consecutive DataFrame indices
    for pos in range(len(df1)):
        row = df1.iloc[pos]
        if d2d[pos] < (1.5 * u.deg):
            inx = idx[pos]
            other = df2.iloc[inx].squeeze()
            # ensure both pieces are pandas Series before concatenation
            left = row.copy() if isinstance(row, pd.Series) else pd.Series(row)
            right = other.copy() if isinstance(other, pd.Series) else pd.Series(other)
            rowdf = pd.concat((left, right))
            rowdf['separation'] = d2d[pos].value
            # convert to plain dict to avoid index-alignment issues when constructing DataFrame
            real_hits.append(rowdf.to_dict())

    result = pd.DataFrame(real_hits)
    # safely drop index column if present
    if 'Unnamed: 0' in result.columns:
        result = result.drop('Unnamed: 0', axis=1)
    # ensure consistent empty-DataFrame shape when no matches found
    if result.empty:
        cols = list(df1.columns) + list(df2.columns) + ['separation']
        result = pd.DataFrame(columns=cols)
    return result
    

"""
All of these tables were compiled using TOPCAT
the session is in the same directory as the tables

"""
sources_10jy = {
        'lolss': '/home/cat-work/work/SETI/swarmSETI/lolss_10jy_srcs.csv',
        'lotss': '/home/cat-work/work/SETI/swarmSETI/lotss_10jy_srcs.csv',
        'vlssr': '/home/cat-work/work/SETI/swarmSETI/vlssr_10jy_srcs.csv'
}
# Load VLSSr table for targets above 
vlssr_table = pd.read_csv(sources_10jy['vlssr'])
vlssr_table = vlssr_table[vlssr_table.DEJ2000.values > 10]
vlssr_sks = SkyCoord(frame='icrs',
                    ra = vlssr_table.RAJ2000.values,
                    dec = vlssr_table.DEJ2000.values,
                    unit=(u.deg, u.deg))

# This has the resolution to make a useful cutoff
lotss_table = pd.read_csv(sources_10jy['lotss'])
lotss_table = lotss_table[(lotss_table.dec > 10.) & (lotss_table.majax < 40.)]
lotss_sks = SkyCoord(frame='icrs',
                    ra = lotss_table.ra.values,
                    dec = lotss_table.dec.values,
                    unit=(u.deg, u.deg))

lolss_table = pd.read_csv(sources_10jy['lolss'])
lolss_table = lolss_table[(lolss_table.dec > 10.) & (lolss_table.maj_axis < 60.)]
lolss_sks = SkyCoord(frame='icrs',
                    ra = lolss_table.ra.values,
                    dec = lolss_table.dec.values,
                    unit=(u.deg, u.deg))


savin_targets = pd.read_csv('/home/cat-work/work/SETI/swarmSETI/savinSourceList.csv')
savin_targets_sks = SkyCoord(frame='icrs',
                    ra = savin_targets.RA.values,
                    dec = savin_targets.DEC.values,
                    unit=(u.deg, u.deg))

stellarHosts10pc = pd.read_csv('/home/cat-work/work/SETI/cosmicStellarHosts/prep_lists/stellarHosts_10pc.csv')
stellarHosts10pc = stellarHosts10pc.dropna(subset=['ra', 'dec'])
sH10pc_sks = SkyCoord(frame='icrs',
                    ra = stellarHosts10pc.ra.values,
                    dec = stellarHosts10pc.dec.values,
                    unit=(u.deg, u.deg))


lotss_savin_comp_hits = source_separations(savin_targets_sks, lotss_sks, savin_targets, lotss_table)
lolss_savin_comp_hits = source_separations(savin_targets_sks, lolss_sks, savin_targets, lolss_table)
vlssr_savin_comp_hits = source_separations(savin_targets_sks, vlssr_sks, savin_targets, vlssr_table)

lotss_sh_comp_hits = source_separations(sH10pc_sks, lotss_sks, stellarHosts10pc, lotss_table)
lolss_sh_comp_hits = source_separations(sH10pc_sks, lolss_sks, stellarHosts10pc, lolss_table)
vlssr_sh_comp_hits = source_separations(sH10pc_sks, vlssr_sks, stellarHosts10pc, vlssr_table)

# long_targets = pd.read_csv('/home/cat-work/work/SETI/swarmSETI/exoVLSSr_1.5deg.csv')

## Here is some extra stuff right quick
# exoVLSSr = Table.read('/home/cat-work/work/SETI/swarmSETI/exoVLSSr_1.5deg.ecsv')
# exo10pc = exoVLSSr[exoVLSSr['sy_dist']<10]
# exo10pc.sort('Sp', reverse=True)
# print(exo10pc['ra_1', 'dec_1', 'Sp', 'sy_name', 'sy_snum', 'sy_pnum', 'sy_dist'][:10])
