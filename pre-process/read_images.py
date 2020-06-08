import glob

path = "./images/galleria/*/"


folders = glob.glob(path)

print(folders)

print(glob.glob(folders[0] + "/*.jpg"))
