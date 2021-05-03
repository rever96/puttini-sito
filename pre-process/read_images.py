import glob
import json

path = "./images/galleria/*/"
result = []

folders = glob.glob(path)

for path_folder in folders:
    files = glob.glob(path_folder + "/*.jpg")
    files += glob.glob(path_folder + "/*.JPG")
    folderName = path_folder.split('/')[2].split("\\")[1]
    for path_file in files:
        path_file = path_file.split('/')[len(path_file.split('/')) - 1]
        isThunbmail = path_file.split('_t')
        if len(isThunbmail) > 1:
            continue
        fileName = path_file.split('.')
        result.append(
            {
                "src": "./images/" + path_file,
                "srct": "./images/" + fileName[0] + "_t." + fileName[1],
                "tags": folderName})

print(json.dumps(result))
