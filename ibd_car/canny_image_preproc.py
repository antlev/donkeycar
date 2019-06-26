import os, cv2
from shutil import copyfile


dataset_folder="data/dataset/"
datasets=os.listdir(dataset_folder)
datasets_to_remove=[]
for dataset in datasets:
	# Keep the datset if it is not already transformed or if the transformed datset already exist
	if 'cv' in dataset or os.path.exists(dataset_folder + dataset + "_cv_canny"):
		print("erase " + dataset)
		datasets_to_remove.append(dataset)

datasets = [x for x in datasets if x not in datasets_to_remove]
print(datasets)

for dataset in datasets:
	dataset_name=dataset_folder + dataset
	new_dataset_name=dataset_name + "_cv_canny/"
	dataset_name=dataset_name + "/"
	print("Apply Canny transformation : <" + dataset_name + "> => <" + new_dataset_name + ">")

	if not os.path.exists(new_dataset_name):
		os.mkdir(new_dataset_name)
	images=os.listdir(dataset_name)
	json_to_remove=[]

	for image in images:
		if 'json' in image:
			copyfile(dataset_name+image, new_dataset_name+image)
			json_to_remove.append(image)

	images = [x for x in images if x not in json_to_remove]


	for image_name in images:
		image = cv2.imread(dataset_name + image_name, 0)
		new_image = cv2.Canny(image,100,200)
		cv2.imwrite(new_dataset_name + image_name , image) 
