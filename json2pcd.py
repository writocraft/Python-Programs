import json


for count in range(4):

	pathIn = "C:\\Users\\Rohit\\Downloads\\jsontry\\" + str(count) +".json"
	pathOut = "C:\\Users\\Rohit\\Desktop\\Output\\"+ str(count) +".json"

	path_to_input = pathIn
	path_to_output = pathOut

	with open(path_to_input) as json_file:
		data_read =json.loads(json_file.read())

		data_write = []
		points_json = {} 

		for pts in data_read['points']:
			data = {};
			row = str(pts['x']) + " " + str(pts['y']) + " " + str(pts['z']) + " " + str(int(pts['i']))
			data = row

			data_write.append(data)

			
			with open(path_to_output, 'w') as write_json_file:
				json.dump(data_write,write_json_file, indent =4)
		print(len(data_read))
