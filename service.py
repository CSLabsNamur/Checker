import json
from jsonschema import validate

def checkFileIntegrity(file):
    # Schema files must follow
    schema = {
        "type" : "object",
        "properties" :{
            "concerned" : {"type" : "array"},
            "description" : {"type" : "string"},
            "message" : {"type" : "string"}
        },
        "required" : [
            "concerned",
            "description"
        ]
    }
    # Try to read file content
    try:
        fh = open(file, "r")
        fileContent = fh.read()
        fh.close()
    except:
        return (False, "Could not open %s" % file)
    try:
        # Validate schema
        fileInJSON = json.loads(fileContent)
        validate(instance=fileInJSON, schema=schema)
    except:
        return (False, "%s couln't pass the integrity test" % file)
    return (True, "")

def retreiveFileDetails(filePath):
    """
    Get usual informations about a file

    Parameter
    ---------
    filePath (string) : Path to file

    Return
    ------
    dictionary following this structure :
    ```json
    {
        "parentPath" : (string) path to the parent folder
        "fileName" : (string) name of the file, without the rest of the path
        "metadataPath" : (string) path to the metadata folder
        "metadataFilePath" : (string) path to the metadata file
    }
    ```
    """
    # Parse folder path
    pathItems = filePath.split("/")
    parentPath = ""
    fileName = ""
    for i in range(len(pathItems)):
        # If it's not the last element of the list
        # Used to remove filename and get parent path
        if i != len(pathItems) - 1:
            parentPath += "%s/" % pathItems[i]
        else:
            fileName = pathItems[i]
    # Remove last /
    parentPath = parentPath[:-1]
    # Get metadata folder path
    metadataPath = "%s/.metadata" % parentPath
    metadataFilePath = "%s/%s.json" % (metadataPath, fileName)
    # Make dict and return
    return {
        "parentPath" : parentPath,
        "fileName" : fileName,
        "metadataPath" : metadataPath,
        "metadataFilePath" : metadataFilePath
    }

def getMetadata(metadataFilePath):
    """
    Return a JSON containing `metadataFilePath`
    """
    # Try to read file content
    try:
        # Handle file
        fh = open(metadataFilePath, "r")
        fileContent = fh.read()
        fh.close()
        # Retreive JSON
        fileInJSON = json.loads(fileContent)
        return fileInJSON
    except:
        raise ValueError("Could not get %s content" % metadataFilePath)