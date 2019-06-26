import os, cv2
from shutil import copyfile

dataset_name="data/dataset/chambre_ant_l1"
new_dataset_name=dataset_name + "_cv/"
dataset_name=dataset_name + "/"

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
