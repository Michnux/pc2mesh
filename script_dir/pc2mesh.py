import subprocess
import os

import pymeshlab



def pc2mesh(input_path, work_dir, offsets, hsrs, vsrs):

	#convert the .las file to .ply with cloudcompare
	cmd = "xvfb-run CloudCompare -SILENT -O "+input_path+" -C_EXPORT_FMT PLY -SAVE_CLOUDS"
	subprocess.run(cmd, shell=True)

	#get the CC dir
	cc_dir=input_path
	c=cc_dir[-1]
	while c!='/':
		c = cc_dir[-1]
		cc_dir = cc_dir[:-1]
	cc_dir+='/'
	
	#get the output file
	file_names = os.listdir(cc_dir)
	print(file_names)
	converted_file = [x for x in file_names if '.ply' in x][0]


	#generate mesh file from converted file using pymeshlab
	ms = pymeshlab.MeshSet()
	ms.load_new_mesh(cc_dir+converted_file)

	#https://pymeshlab.readthedocs.io/en/latest/filter_list.html?highlight=compute%20normals%20for%20point%20sets#compute_normal_for_point_clouds
	ms.compute_normal_for_point_clouds()

	#https://pymeshlab.readthedocs.io/en/latest/filter_list.html?highlight=poisson#generate_surface_reconstruction_screened_poisson
	ms.generate_surface_reconstruction_screened_poisson()

	ms.save_current_mesh(work_dir+'output.obj')



if __name__ == "__main__":

	pass