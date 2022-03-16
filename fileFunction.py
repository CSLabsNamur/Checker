import os
import os.path
from service import *

##### File functions #####
# This file contains functions that are applied on every files
# They must be compliant whit the following resctrictions :
# - Use two parameters :
#   - filePath (string) : path to the file
#   - data (dict) : contains global informations
# - Returns a tuple ((boolean) Operation succeed, (string) Message)
# If you don't follow these rules, script will raise an exception


def checkFile(filePath, data):
    """
    Check if a file possesses metadata
    """
    infos = retreiveFileDetails(filePath)
    # Check if there is a .metadata folder
    if not os.path.isdir(infos["metadataPath"]):
        return (False, "%s has files but does not have a .metadata folder !" % infos["parentPath"])
    # Check if there is a metadata file
    if not os.path.isfile(infos["metadataFilePath"]):
        return (False, "%s does not have a corresponding metadata file" % filePath)
    # Check file integrity
    return checkFileIntegrity(infos["metadataFilePath"])

def search(filePath, data):
    """
    search a particular word in metadata "concerned" field in `filePath` metadata
    """
    # If the integrity test passes
    if checkFile(filePath, "")[0]:
        infos = retreiveFileDetails(filePath)
        metadata = getMetadata(infos["metadataFilePath"])
        for item in metadata["concerned"]:
            if data["args"][2].upper() == item.upper():
                print("%s contains references" % filePath)
                return (True, "%s contains references" % filePath)
        return (True, "%s does not contains references" % filePath)
    return(False, "Could not get metadata for %s" % filePath)
            
            

