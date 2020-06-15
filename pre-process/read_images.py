import glob
import json

path = "./images/galleria/*/"
result = []

folders = glob.glob(path)

for path_folder in folders:
    files = glob.glob(path_folder + "/*.jpg")
    files += glob.glob(path_folder + "/*.JPG")
    folderName = path_folder.split('/')
    for path_file in files:
        path_file = path_file.split('/')[len(path_file.split('/')) - 1]
        isThunbmail = path_file.split('_t')
        if len(isThunbmail) > 1:
            continue
        fileName = path_file.split('.')
        result.append(
            {
                "src": path_folder + path_file,
                "srct": path_folder + fileName[0] + "_t." + fileName[1],
                "tags": folderName[len(folderName) - 2]})

print(json.dumps(result))
