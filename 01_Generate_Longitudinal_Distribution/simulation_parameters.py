import os
import numpy as np

# parameters
########################################################################       
parameters = {}

parameters['intensity']	        = 700E10        # Protons in bunch
parameters['epsn_x']	        = 12E-6         # 12 mm mrad
parameters['epsn_y']	        = 8E-6          # 8 mm mrad
parameters['bunch_length']	= 220E-9        # 4 sigma
parameters['blength']		= 220E-9        # 4 sigma
parameters['eps_z']		= 2.6           # 2.6 eVs

parameters['rf_voltage']= 40.0                  # in kV

parameters['BLonD_file']='../../06_Dispersion_Mismatch/BLonD_Files_SC/BLonD_Longitudinal_Distn.npz'
        
parameters['tunex']		= '619'
parameters['tuney']		= '624'

parameters['lattice_start'] 	= 'BWSH65'
parameters['n_macroparticles']	= int(5E5)

# PS Injection 1.4 GeV
parameters['gamma'] 	        = 2.49038064

parameters['beta'] 		= np.sqrt(parameters['gamma']**2-1)/parameters['gamma']
parameters['LongitudinalJohoParameter'] = 1.2
parameters['LongitudinalCut'] 	= 2.4
parameters['TransverseCut']	= 5
parameters['circumference']	= 2*np.pi*100
parameters['phi_s']		= 0
parameters['macrosize']		= parameters['intensity']/float(parameters['n_macroparticles'])
c 				= 299792458
parameters['sig_z'] 	= (parameters['beta'] * c * parameters['blength'])/4.

parameters['turns_max'] = int(2200)
tu1 = np.array(range(-1, parameters['turns_max'], 200))
tu2 = np.array(range(50, 100, 10))
tu3 = np.array(range(1, 50))
tu4 = np.append(tu1, tu2)
tu5 = np.append(tu4, tu3)

parameters['turns_print'] = sorted(tu5)
parameters['turns_update'] = sorted(tu5)

switches = {
        'Space_Charge':         False,
        'Dispersion_Mismatch':  True,
	'CreateDistn':		True,
	'Update_Twiss':		False,  # Needed to save optics turn-by-turn
	'GridSizeX': 128,
	'GridSizeY': 128,
	'GridSizeZ': 64
}


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
