import alteia



sdk = alteia.SDK(config_path='./config-connections.json')


analytic = sdk.analytics.search(name="agnicoeagledevelopment/pc2mesh")
if len(analytic)>0:
	analytic=analytic[0]
	sdk.analytics.delete(analytic=analytic.id)

sdk.analytics.create(name="agnicoeagledevelopment/pc2mesh",
	version="1.0.0",
	display_name="pc2mesh",
	description="Generates a Mesh from a .las file - - - ",
	docker_image="registry-1.docker.io/michaeldelagarde/pc2mesh:latest",
	company="627cfd46193a2300078b53b1",
	instance_type='small',
	volume_size=20,
	inputs=[{
		"name": "input_las",
		"display_name": "input_las",
		"description": ".las file",
		"scheme": {
			"type": "string", "pattern": "^[0-9a-f]{24}$"
		},
		"source": {
			"service": "data-manager",
			"resource": "dataset",
			"scheme": {
				"type": "object",
				"properties": {"type": {"const": "pcl"}}, ####
				"required": ["type"]
			},
		},
		"required": True
	},
	],
	parameters=[
		# {
		# "name": "x_offset",
		# "display_name": "X offset",
		# "description": "X offset to apply to ifc coordinates",
		# "required": False,
		# "scheme": {
		# 	"type": "string"#, "pattern": "^[0-9]$"
		# }
	 # 	},
	 # 	{
		# "name": "y_offset",
		# "display_name": "Y offset",
		# "description": "Y offset to apply to ifc coordinates",
		# "required": False,
		# "scheme": {
		# 	"type": "string"#, "pattern": "^[0-9]$"
		# }
	 # 	},
		# {
		# "name": "z_offset",
		# "display_name": "Z offset",
		# "description": "Z offset to apply to ifc coordinates",
		# "required": False,
		# "scheme": {
		# 	"type": "string"#, "pattern": "^[0-9]$"
		# }
	 # 	},

	],
	deliverables=[
	# {
	# 	"name": "output_mesh",
	# 	"display_name": "output_mesh",
	# 	"description": "output_mesh",
	# 	"scheme": {
	# 		"type": "string", "pattern": "^[0-9a-f]{24}$"
	# 	},
	# 	"source": {
	# 		"service": "data-manager",
	# 		"resource": "dataset",
	# 		"scheme": {
	# 			"type": "object",
	# 			"properties": {"type": {"const": "mesh"}},
	# 			"required": ["type"]
	# 		},
	# 	},
	# 	"required": False
	# }
	],
	groups=["UTILS"])