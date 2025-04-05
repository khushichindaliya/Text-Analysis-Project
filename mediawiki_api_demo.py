import tarfile

f = open("data/yelp_dataset.tar")

# open file
file = tarfile.open(f)
# extracting file
file.extractall()

file.close()
