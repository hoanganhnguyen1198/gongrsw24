import collections
import json
import os

"""
    Transforms JSON reports into TXT files in API call order
"""


def read_json(filename: str) -> dict:
    """Loads the JSON file"""
    
    try:
        with open(filename, "r") as f:
            data = json.loads(f.read())
    except:
        raise Exception(f"Reading {filename} file encountered an error")
    return data


def file_list(path):
    """Lists the contents of a given folder"""
    
    files = os.listdir(path)
    
    return files


def flatten(d, sep="."):
    """Transforms the nested JSON into a dictionary with the tree nodes concatenated at a single level, with a dot as the separator for the original dictionary keys"""
    
    obj = collections.OrderedDict()
    
    def recurse(t, parent_key=""):
        if isinstance(t, list):
            for i in range(len(t)):
                recurse(t[i], parent_key + sep + str(i) if parent_key else str(i))
        elif isinstance(t, dict):
            for k, v in t.items():
                recurse(v, parent_key + sep + k if parent_key else k)
        else:
            obj[parent_key] = t
    
    recurse(d)
    return obj


def filter_dict2(json_file):
    """
    Filters the JSON file to concatenate only the chosen information to compose the dataset. As the files can be very different, it is better to discard unwanted entries instead of selecting the desired entries.
    """
    
    filtered_json_file = {}
    
    if (
            "behavior" in json_file):  # including only behavior leaves several txt files without content and the overall size of the files remains at 1.1GB, too large to be processed in a dataset
        
        filtered_json_file["behavior_summary"] = json_file["behavior"]["summary"] if (
                "summary" in json_file["behavior"]) else None
        
    return filtered_json_file


def save_file(path, filename, content):  # execute this in a thread
    
    with open(path + filename + ".txt", "a") as f:
        
        buffer = list(content.values())
        
        for item in buffer:
            try:
                f.write(str(item) + '\n')
                # there is an encoding problem here that I don't know what it is (and this problem had already occurred before in the other approach)
            except:
                pass


def main():
    path = "..//5 - Cuckoo Reports//"  # This path is just to load the JSON files
    
    print("Getting list of files in the folder", end='')
    json_file_list = file_list(path)
    print("............complete")
    
    cont = 0
    
    for item in sorted(json_file_list):  # [start_file:finish_file]
        
        file_path = path + item
        
        print("Loading file nº: " + str(cont) + " Name: " + item, end="")
        json_file = read_json(file_path)  # this is where the JSON processing should happen
        print("..............loaded")
        
        print("Applying filters ", end='')
        filtered_json_file = filter_dict2(json_file)
        json_file = None
        print("........finished")
        
        print("Transforming nested JSON into dictionary", end='')
        flat_json = flatten(filtered_json_file)
        filtered_json_file = None
        print("......finished")
        
        print("File size: {:.2f}MB".format(os.path.getsize(file_path) / 1000000))
        print("Dictionary with " + str(len(flat_json)) + " lines")
        
        print("Saving file to disk", end='')
        save_file("..//7 - TF-IDF//", item[:-5], flat_json)
        print(" ...........finished")
        print(">>>>>Restarting<<<<<<")
        
        cont += 1


if __name__ == '__main__':
    main()
