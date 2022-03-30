import pymeshlab
ms = pymeshlab.MeshSet()

ms.load_new_mesh('Simplified Mupani South Workshop - Cloud.ply')


#https://pymeshlab.readthedocs.io/en/latest/filter_list.html?highlight=compute%20normals%20for%20point%20sets#compute_normal_for_point_clouds
ms.compute_normal_for_point_clouds()

#https://pymeshlab.readthedocs.io/en/latest/filter_list.html?highlight=poisson#generate_surface_reconstruction_screened_poisson
ms.generate_surface_reconstruction_screened_poisson()


ms.save_current_mesh('generated_mesh.obj')