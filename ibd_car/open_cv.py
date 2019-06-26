import os, cv2
from shutil import copyfile

test_data_folder="data/dataset/test"
images=os.listdir(test_data_folder)
new_dataset_folder=test_data_folder + "_cv_laplacian/"
test_data_folder="data/dataset/test/"

if not os.path.exists(new_dataset_folder):
	os.mkdir(new_dataset_folder)

json_to_remove=[]
# Remove json
for image in images:
	if 'json' in image:
		copyfile(test_data_folder+image, new_dataset_folder+image)
		json_to_remove.append(image)
images = [x for x in images if x not in json_to_remove]

for image_name in images:
	image = cv2.imread(test_data_folder + image_name, 0)
	laplacian = cv2.Laplacian(image,cv2.CV_64F)
	sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
	sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
	cv2.imwrite(new_dataset_folder + image_name , laplacian) 
	# cv2.imwrite(new_dataset_folder + image_name , sobelx) 
	# cv2.imwrite(new_dataset_folder + image_name , sobely) 
