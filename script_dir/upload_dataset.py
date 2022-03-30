import alteia



def upload_dataset(file_path, project_id, mission_id, script_dir):

	sdk = alteia.SDK(config_path=script_dir+'config-connections.json')

	new_dataset = sdk.datasets.create_mesh_dataset(	name='output_mesh',
													project=project_id,
													mission=mission_id,
													dataset_format='obj',
													texture_count=0, material_count=0)

	sdk.datasets.upload_file(dataset=new_dataset.id,
							 component='mesh',
							 file_path=file_path)


if __name__ == "__main__":

	script_dir='.'
	# sdk = alteia.SDK(config_path=script_dir+'/alteia_cred.json')
	# help(sdk.datasets.create_mesh_dataset)

	upload_dataset('../work_dir/output.glb', '62403f06e7fe320008dd2883', script_dir)