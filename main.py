import csv
# id,filepaths,labels,data set
img_ids = []
img_paths = []
labels = []
dataset = []

with open('D:\\pythonProject\\moco-main\\BIRD\\birds.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        img_ids.append(row['class id'])
        img_paths.append(row['filepaths'])
        labels.append(row['labels'])

print(img_ids[0:5])
print(labels[0:5])
