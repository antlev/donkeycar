import os
import runpy
datasets=os.listdir("data/dataset/")
datasets.remove("auto.py")
print(datasets)
for dataset in datasets:
	print("Running command : ")
	print("python manage.py train --tub data/dataset/" + str(dataset) + " --model models/" + str(dataset) + " --logs " + str(dataset))
	os.system("python manage.py train --tub data/dataset/" + str(dataset) + " --model models/" + str(dataset) + " --logs " + str(dataset))
