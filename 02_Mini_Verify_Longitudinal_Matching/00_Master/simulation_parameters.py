import os
import numpy as np
c = 299792458

# Folder flags
########################################################################
cwd = os.getcwd() # Get the present directory
folder = cwd.split('/')[-1] # Last part of cwd is folder name
# name folder like 1_0_3, or 01_00_03
#dir_sc = int(folder.split('_')[0]) # First number is sc flag
#indir_sc = int(folder.split('_')[1]) # Second number is indirect sc flag
#case = int(folder.split('_')[2]) # Last number is case flag

parameters = {}

parameters['MADX_File']         = 'Create_PTC_flat_file.madx'
parameters['lattice_start']     = 'BWSH65'
parameters['tunex']             = '614'
parameters['tuney']             = '635'

# Currently use BLonD generated longitudinal distribution
parameters['BLonD_file'] = 'BLonD_Longitudinal_Distn_TOF_80kV.npz'

parameters['n_macroparticles']  = int(1E4)      # Simulated macroparticles
parameters['intensity']	        = 700E10        # Protons in bunch
parameters['epsn_x']	        = 12E-6         # 12 mm mrad
parameters['epsn_y']	        = 8E-6          # 8 mm mrad
parameters['bunch_length']	= 220E-9        # 4 sigma
parameters['blength']		= 220E-9        # 4 sigma
parameters['eps_z']		= 2.6           # 2.6 eVs
parameters['dpp_rms']		= 1.7e-03

parameters['LongitudinalJohoParameter'] = 1.2
parameters['LongitudinalCut'] 	        = 2.4
parameters['TransverseCut']		= 5

parameters['rf_voltage']		= 0.080
parameters['phi_s']			= 0


parameters['circumference']		= 2*np.pi*100

parameters['macrosize']			= parameters['intensity']/float(parameters['n_macroparticles'])

# PS Injection 1.4 GeV
parameters['gamma'] 	= 2.49253731343
parameters['beta'] 	= np.sqrt(parameters['gamma']**2-1)/parameters['gamma']
parameters['sig_z'] 	= (parameters['beta'] * c * parameters['blength'])/4.

parameters['turns_max'] = int(2200)
tu1 = range(-1, parameters['turns_max'], 200)
tu2 = range(50, 100, 10)
tu3 = range(1, 50)
tu = tu2 + tu1 + tu3 
tu.append(874) # WS 172s
tu.append(2185)# WS 175s
# ~ tu = range(-1, parameters['turns_max']) # every turn

parameters['turns_print'] = tu
parameters['turns_update'] = tu

switches = {
        'Direct_Space_Charge':          True,
        'Indirect_Space_Charge':        False,
	'Print_SC_Grid':	        False,
	'CreateDistn':		        True,
	'Update_Twiss':		        False,
	'GridSizeX': 64, #128, #312
	'GridSizeY': 64, #128, #206
	'GridSizeZ': 32 #64
}

parameters['Space_Charge_GridSizeX'] = switches['GridSizeX']
parameters['Space_Charge_GridSizeY'] = switches['GridSizeY']
parameters['Space_Charge_GridSizeZ'] = switches['GridSizeZ']

# PTC RF Table Parameters
harmonic_factors = [1] # this times the base harmonic defines the RF harmonics (for SPS = 4620, PS 10MHz 7, 8, or 9)
time = np.array([0,1,2])
ones = np.ones_like(time)
Ekin_GeV = 1.4*ones
RF_voltage_MV = np.array([parameters['rf_voltage']*ones]).T # in MV
RF_phase = np.array([np.pi*ones]).T

RFparameters = {
	'harmonic_factors': harmonic_factors,
	'time': time,
	'Ekin_GeV': Ekin_GeV,
	'voltage_MV': RF_voltage_MV,
	'phase': RF_phase
}
