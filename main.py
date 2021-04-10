import os
import json

DEFAULT_JSONPATH = "D:\\Slideshow Images\\removed_images.json"
DEFAULT_IMAGEPATH = "E:\\Desktop\\Cool & Cute Anime"


def input_case1():
    """
    Functionality: This is the first input use case to simplely get the JSON path for removed_files.json, we will use this file to figure out
                   which images to delete.
    """
    while(True):
        print("\nDefault JSON path (this is the removed_images.json file that contains a list of images to delete): " + DEFAULT_JSONPATH)
        userinput = input("Would you like to use default path? (Y/N): ")

        if userinput.lower() == "n":
            if os.path.isfile(DEFAULT_JSONPATH):
                return DEFAULT_JSONPATH
            else:
                print("Filepath is invalid or file does not exist")

        elif userinput.lower() == "y":
            jsonPath = input("Enter file path to json file that contains list of images to delete: ")
            if os.path.isfile(jsonPath):
                print("Filepath exists")
                return jsonPath
            else:
                print("Filepath is invalid or file does not exist")
        else:
            print("Invalid input")

def input_case2():
    """
    Functionality: This is the second input use case to simplely get the Image Directory which contains all the original images.
    """
    while(True):
        print("\nDefault Image Directory (this is the folder where the images will be deleted from): " + DEFAULT_IMAGEPATH)
        userinput = input("Would you like to use default path? (Y/N): ")

        if userinput.lower() == "n":
            if os.path.isdir(DEFAULT_IMAGEPATH):
                return DEFAULT_IMAGEPATH
            else:
                print("Image directory is invalid or file does not exist")

        elif userinput.lower() == "y":
            imagePath = input("Enter Image directory that contains images that will be run against with out json list: ")
            if os.path.isdir(imagePath):
                print("Image Directory exists")
                return imagePath
            else:
                print("Image directory is invalid or file does not exist")
        else:
            print("Invalid input")

def input_case3(jsonPath, imagePath):
    """
    Functionality: This is the third input use case which is used for finding all the images that are needed to be deleted
                   and removing them.
    """
    try:
        fileInfo = []
        with open(jsonPath) as f:
            for line in f:
                fileInfo.append(json.loads(line))
    except Exception as e:
        print(e)


    for file in fileInfo:
        if os.path.isfile(imagePath + "\\" + file["filename"]):
            print("Found file: " + imagePath + "\\" + file["filename"])
        else:
            print("Could not find file: " + imagePath + "\\" + file["filename"])

    while(True):
        userinput = input("Would you like to delete all these files? (Y/N): ")

        if userinput.lower() == "y":
            for file in fileInfo:
                try:
                    os.remove(imagePath + "\\" + file["filename"])
                    print("File deleted: " + imagePath + "\\" + file["filename"])
                except Exception as e:
                    print("Could not print file due to: " + e)
            return

        elif userinput.lower() == "n":
            print("No Files were deleted")
            return
        else:
            print("Invalid input")


if __name__ == '__main__':
    jsonPath = input_case1()
    imagePath = input_case2()

    input_case3(jsonPath, imagePath)    
    open(jsonPath, 'w').close()
    print(jsonPath + " has been updated with files that have been removed.")

