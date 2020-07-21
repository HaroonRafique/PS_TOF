import os

NoSC_Scan = True
SC_Scan = True

master_dir = os.getcwd()

NoSC_locations = []
NoSC_locations.append('/0_70_0')
NoSC_locations.append('/0_85_0')

SC_locations = []
SC_locations.append('/1_70_0')
SC_locations.append('/1_70_1')
SC_locations.append('/1_70_2')
SC_locations.append('/1_85_0')
SC_locations.append('/1_85_1')
SC_locations.append('/1_85_2')

if NoSC_Scan:
	for loc in NoSC_locations:
		print '--------------------------------------------------------------------------------------------'
		print '\t Submitting HPC-Batch simulation:', loc
		print '--------------------------------------------------------------------------------------------'
		dir_ = master_dir + loc 
		make_command = 'python Make_SLURM_submission_script.py'
		submit_command = 'sbatch SLURM_submission_script.sh'
		os.chdir(dir_)
		os.system(make_command)
		os.system(submit_command)

if SC_Scan:
	for loc in SC_locations:
		print '--------------------------------------------------------------------------------------------'
		print '\t Submitting HPC-Batch simulation:', loc
		print '--------------------------------------------------------------------------------------------'
		dir_ = master_dir + loc 
		make_command = 'python Make_SLURM_submission_script.py'
		submit_command = 'sbatch SLURM_submission_script.sh'
		os.chdir(dir_)
		os.system(make_command)
		os.system(submit_command)

