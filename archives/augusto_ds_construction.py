import collections
import json
import os
from threading import Thread
import pandas


def read_json(filename: str) -> dict:

    """Loads the JSON file"""

    try:
        with open(filename, "r") as f:
            data = json.loads(f.read())
    except:
        raise Exception(f"Reading {filename} file encountered an error")
    return data


def file_list(path) -> list:

    """Lists the contents of a given folder"""

    files = os.listdir(path)

    return files


def flatten(d, sep="."):

    """
    Transforms the nested JSON into a dictionary with the tree nodes concatenated 
    at a single level, using a dot as the separator for the original dictionary keys.
    """

    obj = {}

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


def filter_dict(json_file): # This is the filter that passes what is not listed

    """
    Filters the JSON file to concatenate the unfiltered information to compose the dataset. Since the files can be very different, it is better to discard unwanted entries instead of selecting the desired entries.
    """

    # The info entry will be partially used
    [json_file["info"].pop(key, "key: not found") for key in ['added', 'started', 'duration', 'ended', 'owner', 'category', 'git', 'route', 'custom', 'machine', 'platform', 'version', 'options', "monitor", "package"]]

    # Since procmemory is a list, to pop it you have to iterate to perform the operations
    # In procmemory only regions will remain
    json_file.pop("procmemory", "key: not found")

    # Will delete the entire target entry
    json_file.pop("target", "key: not found")

    # The extracted entry will be discarded
    json_file.pop("extracted", "key: not found")

    # Will delete the entire virustotal entry
    json_file.pop("virustotal", "key: not found")

    # The network entry can be used, but maybe not directly
    json_file.pop("network", "key: not found")

    # The signatures entry will be discarded
    json_file.pop("signatures", "key: not found")

    # The static entry will be partially used (since I am interested in dynamic analysis, static will be left out)
    json_file.pop("static", "key: not found")

    # The dropped entry will be discarded
    json_file.pop("dropped", "key: not found")

    # The behavior entry will be partially used
    json_file['behavior'].pop("generic", "key: not found")

    for i in range(len(json_file["behavior"]["processes"])):
        [json_file["behavior"]["processes"][i].pop(key, "key: not found") for key in ['track', 'pid', 'command_line', 'time', 'tid', 'first_seen', 'ppid', 'type', 'process_path', 'process_name']]
        for j in range(len(json_file["behavior"]["processes"][i]['modules'])):
            [json_file["behavior"]["processes"][i]['modules'][j].pop(key, "key: not found") for key in ['imgsize', 'baseaddr', 'filepath', 'basename']]
        for j in range(len(json_file["behavior"]["processes"][i]['calls'])):
            [json_file["behavior"]["processes"][i]['calls'][j].pop(key, "key: not found") for key in ['time', 'tid', 'status', 'return_value', 'last_error', 'nt_status', 'buffer', 'arguments', 'category', "api"]]
            if len(json_file["behavior"]["processes"][i]['calls'][j]['flags']) == 0:
                json_file["behavior"]["processes"][i]['calls'][j].pop('flags', "key: not found")
            else:
                [json_file["behavior"]["processes"][i]['calls'][j]['flags'].pop(key, "key: not found") for key in ['stack_pivoted', 'module_address', 'process_identifier', 'region_size', 'stack_dep_bypass', 'heap_dep_bypass', 'protection', 'process_handle', 'allocation_type', 'base_address', 'module_handle', 'handle', 'section_handle', 'object_handle', 'file_handle', 'file_path', 'filepath', 'flags', 'create_disposition', 'filepath_r', 'status_info', 'mode', 'file_attributes', 'application_name', 'resource_name', 'basename', 'buffer', 'length', 'offset', 'move_method', 'create_options', 'desired_access', 'shared_access', 'share_access', 'create_disposition', 'section_name', 'commit_size', 'section_handle', 'win32_protect', 'section_offset', 'view_size', 'allocation_type', 'key_handle', 'key_name', 'information_class', 'reg_type', 'id', 'string', 'window_handle', 'text', 'caption', 'language_identifier', 'iid', 'clsid', 'creation_flags', 'index', 'open_options', 'control_code', 'cmd', 'folder', 'hook_identifier', 'std_handle', 'modifiers','option', 'algorithm_identifier', 'command_line', 'prcess_name', 'algorythm_identifier']]

    for i in range(len(json_file["behavior"]["processtree"])):
        [json_file["behavior"]["processtree"][i].pop(key, "key: not found") for key in ['track', 'pid', 'first_seen', 'ppid', 'process_name', 'command_line', 'children']]

    if "summary" in json_file["behavior"]:
        [json_file["behavior"]["summary"].pop(key, "key: not found") for key in ['file_opened', 'regkey_opened', 'tls_master', 'guid', 'connects_ip', 'regkey_writen', 'command_line', 'regkey_deleted', 'mutex', 'file_read', 'regkey_read', 'file_created', 'file_moved', 'file_written', 'file_recreated', 'directory_created', 'file_failed', 'resolves_host', 'file_deleted', 'directory_removed', 'file_exists', 'directory_enumerated', 'file_opened', 'wmi_query', 'connects_host', 'dll_loaded', 'regkey_written', 'file_copied']]

    # The memory entry will be used
    json_file.pop("memory", "key: not found")

    # The debug entry will be discarded
    json_file.pop("debug", "key: not found")

    # The screenshots entry will be discarded
    json_file.pop("screenshots", "key: not found")

    # The strings entry will be used (but need to check what can be used)
    json_file.pop("strings", "key: not found")

    # The metadata entry will be discarded
    json_file.pop("metadata", "key: not found")

    # The buffer entry will be discarded
    json_file.pop("buffer", "key: not found")

    return json_file


def filter_dict2(json_file):

    """
    Filters the JSON file to concatenate only the chosen information to compose the dataset. 
    Since the files can be very different, it is better to discard unwanted entries instead of selecting the desired entries.
    """

    filtered_json_file = {}

    filtered_json_file["id"] = int(json_file["info"]["id"])

    filtered_json_file["score"] = json_file["info"]["score"]

    filtered_json_file["added_files"] = 0

    for strings in json_file["debug"]["log"]:

        if "DECRYPT FILE" in strings:   # If there is a decrypt button in the log, it is a decrypter and will be discarded

            break

        elif "Added new file to list with pid" in strings:

            filtered_json_file["added_files"] += 1

    if ("behavior" in json_file):

        if ("apistats" in json_file["behavior"]): # Some are returning zero in the ID because they do not have API STATS -> I think I will clean it directly in the dataset after it is ready

            filtered_json_file["apistats"] = json_file["behavior"]["apistats"]

        if ("summary" in json_file["behavior"]):

            filtered_json_file["file_created"] = len(json_file["behavior"]['summary']["file_created"]) if ("file_created" in json_file["behavior"]['summary']) else 0

            filtered_json_file["file_recreated"] = len(json_file["behavior"]['summary']["file_recreated"]) if ("file_recreated" in json_file["behavior"]['summary']) else 0

            filtered_json_file["directory_created"] = len(json_file["behavior"]['summary']["directory_created"]) if ("directory_created" in json_file["behavior"]['summary']) else 0

            filtered_json_file["dll_loaded"] = len(json_file["behavior"]['summary']["dll_loaded"]) if ("dll_loaded" in json_file["behavior"]['summary']) else 0

            filtered_json_file["file_opened"] = len(json_file["behavior"]['summary']["file_opened"]) if ("file_opened" in json_file["behavior"]['summary']) else 0

            filtered_json_file["command_line"] = len(json_file["behavior"]['summary']["command_line"]) if ("command_line" in json_file["behavior"]['summary']) else 0

            filtered_json_file["regkey_opened"] = len(json_file["behavior"]['summary']["regkey_opened"]) if ("regkey_opened" in json_file["behavior"]['summary']) else 0

            filtered_json_file["resolve_host"] = len(json_file["behavior"]['summary']["resolve_host"]) if ("resolve_host" in json_file["behavior"]['summary']) else 0

            filtered_json_file["file_written"] = len(json_file["behavior"]['summary']["file_written"]) if ("file_written" in json_file["behavior"]['summary']) else 0

            filtered_json_file["file_deleted"] = len(json_file["behavior"]['summary']["file_deleted"]) if ("file_deleted" in json_file["behavior"]['summary']) else 0

            filtered_json_file["file_exists"] = len(json_file["behavior"]['summary']["file_exists"]) if ("file_exists" in json_file["behavior"]['summary']) else 0

            filtered_json_file["file_moved"] = len(json_file["behavior"]['summary']["file_moved"]) if ("file_moved" in json_file["behavior"]['summary']) else 0

            filtered_json_file["mutex"] = len(json_file["behavior"]['summary']["mutex"]) if ("mutex" in json_file["behavior"]['summary']) else 0

            filtered_json_file["file_failed"] = len(json_file["behavior"]['summary']["file_failed"]) if ("file_failed" in json_file["behavior"]['summary']) else 0

            filtered_json_file["wmi_query"] = len(json_file["behavior"]['summary']["wmi_query"]) if ("wmi_query" in json_file["behavior"]['summary']) else 0

            filtered_json_file["guid"] = len(json_file["behavior"]['summary']["guid"]) if ("guid" in json_file["behavior"]['summary']) else 0

            filtered_json_file["file_read"] = len(json_file["behavior"]['summary']["file_read"]) if ("file_read" in json_file["behavior"]['summary']) else 0

            filtered_json_file["regkey_read"] = len(json_file["behavior"]['summary']["regkey_read"]) if ("regkey_read" in json_file["behavior"]['summary']) else 0

            filtered_json_file["directory_enumerated"] = len(json_file["behavior"]['summary']["directory_enumerated"]) if ("directory_enumerated" in json_file["behavior"]['summary']) else 0

            filtered_json_file["regkey_written"] = len(json_file["behavior"]['summary']["regkey_written"]) if ("regkey_written" in json_file["behavior"]['summary']) else 0

    if "memory" in json_file:

        for dlllist in json_file["memory"]["dlllist"]["data"]:

            if dlllist["process_name"] in filtered_json_file.keys():

                filtered_json_file[dlllist["process_name"]] += 1

            else:

                filtered_json_file[dlllist["process_name"]] = 1

        for privs in json_file["memory"]["privs"]["data"]:

            if privs["privilege"] in filtered_json_file.keys():

                filtered_json_file[privs["privilege"]] += 1

            else:

                filtered_json_file[privs["privilege"]] = 1


    if "network" in json_file:

        filtered_json_file["udp"] = len(json_file["network"]['udp'])
        filtered_json_file["dns"] = len(json_file["network"]['dns'])
        filtered_json_file["domains"] = len(json_file["network"]['domains'])
        filtered_json_file["http"] = len(json_file["network"]['http'])
        filtered_json_file["tcp"] = len(json_file["network"]['tcp'])
        filtered_json_file["http_ex"] = len(json_file["network"]['http_ex'])

    if "strings" in json_file:

        filtered_json_file["strings_count"] = len(json_file["strings"])

    return filtered_json_file


def normalize(flat_json):

    """This function will receive the flat JSON and transform it into a dataframe"""

    keys_list = list(flat_json.keys())

    unique_cols = {}

    for items in keys_list:
        api = items.split(sep='.')[-1]
        if api not in unique_cols:
            unique_cols[api] = 0

    for k, v in flat_json.items():
        k_split = k.split(sep='.')[-1]
        if k_split in unique_cols:
            unique_cols[k_split] = unique_cols[k_split] + v

    df1 = pandas.json_normalize(unique_cols)

    return df1


def main():

    path = "..//5 - Cuckoo Reports//"

    print("Getting list of files in the folder", end='')
    json_file_list = file_list(path)
    print("............complete")

    df1 = pandas.DataFrame()

    cont = 0

    for item in sorted(json_file_list):

        file_path = path + item

        print("Loading file nº: " + str(cont) + " Name: " + item, end="")
        json_file = read_json(file_path)
        print("..............loaded")

        print("Applying filters ", end='')
        filtered_json_file = filter_dict2(json_file)

        json_file = None
        print("........finished")

        print("Transforming nested JSON into dictionary", end='')
        flat_json = flatten(filtered_json_file)
        filtered_json_file = None
        print("......finished")

        print("File size: {:.2f}MB".format(os.path.getsize(file_path)/1000000))
        print("Dictionary with " + str(len(flat_json)) + " lines")

        if cont == 0:

            print("Normalizing file", end="")
            df1 = normalize(flat_json)
            flat_json = None
            print(" ...........finished")

        else:

            print("Normalizing file", end="")
            df2 = normalize(flat_json)
            flat_json = None
            print(" ...........finished")

            print("Concatenating file", end="")
            table = pandas.concat([df1, df2], ignore_index=True)
            print(" ...........finished")

            print("Copying Dataframe", end="")
            df1 = table
            print(" ...........copied")

            print("Cleaning unnecessary dataframes", end="")
            table = None
            df2 = None
            print(" ...........finished")

            print("Final table: ", df1.shape)

            print(">>>>>Restarting<<<<<<")

        if (cont != 0) and (int(cont % 5)) == 0:

            print("Saving file to disk")
            to_pickle_args = "..//6 - Dataset//" + str(cont) + ".pkl"
            write_thread = Thread(target=df1.to_pickle, args=[to_pickle_args])
            write_thread.start()
            print("File saved to disk")

            if cont >= 10:

                remove_file_args = "..//6 - Dataset//" + (str(cont-5)) + ".pkl"
                remove_thread = Thread(target=os.remove, args=[remove_file_args])
                remove_thread.start()

        elif item == json_file_list[-1]:

            remove_file_args = "..//6 - Dataset//" + (str(int(cont % 5)) * 5) + ".pkl"
            remove_thread = Thread(target=os.remove, args=[remove_file_args])
            remove_thread.start()

        cont += 1


if __name__ == '__main__':
    main()
