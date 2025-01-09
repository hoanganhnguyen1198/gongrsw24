"""
Tasks:
    1 - Create a dictionary for each file with the strings and their quantities
    2 - Concatenate this dictionary into a dataframe (use the compute TF function) - use .lower
        pd.DataFrame([wordDictA, wordDictB]) I have to use a for loop for each file,
        master the original dataframe in wdA and alternate in WDB, just like I did in the other approach
    3 - Compute the IDF (use the compute IDF function)
    4 - Compute the TF-IDF (use the compute TF-IDF function)
"""

import os
from threading import Thread
import pandas
import pandas as pd


def read_file(filename: str) -> dict:
    """Loads the TXT file"""
    try:
        with open(filename, "r") as f:
            data = f.readlines()
    except:
        raise Exception(f"Reading {filename} file encountered an error")
    return data


def file_list(path):
    """Lists the contents of a given folder"""
    
    files = os.listdir(path)
    
    return files


def convert_to_dict(list, filename):
    """
    Converts a list of strings received as a parameter into a dictionary with the number of times each string appears in that list
    """
    
    dict = {}
    dict["name"] = filename[0:5]
    for item in list:
        item = item.lower()
        if item[0:-1] in dict.keys():
            dict[item[0:-1]] += 1
        elif item not in dict.keys():
            dict[item[0:-1]] = 1
    return dict


def save_dataframe(dataframe):
    """
    Saves the dataframe in CSV format
    """
    dataframe.to_csv("..//6 - Dataset//TF-IDF.csv", index=False)


def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bowCount)
    return tfDict


def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)
    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log10(N / float(val))
    return idfDict


def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val * idfs[word]
    return tfidf


def main():
    path = "..//7 - TF-IDF//"
    
    print("Getting list of files in the folder", end='')
    txt_file_list = file_list(path)
    txt_file_list.sort()  # it might be interesting to use
    print("............complete")
    
    df1 = pandas.DataFrame
    
    table = None  # List of words existing in all documents, without repetition
    
    cont = 0
    
    for item in txt_file_list:  # THE LIMITATION OF THE NUMBER OF LOADED FILES CAN BE DONE HERE
        
        file_path = path + item  # full file path
        
        print("Loading file nº: " + str(cont) + " Name: " + item, end="")
        txt_file = read_file(file_path)  # Todo: check if txt_file is a list
        print("..............loaded")
        
        print("Transforming the text file into a dictionary", end='')
        file_dict = convert_to_dict(txt_file, item)
        print("......finished")
        
        if cont == 0:
            print("Transforming the dictionary into a dataframe", end='')
            df1 = pd.DataFrame([file_dict])  # returns the normalized dataframe
            file_dict = None
            print("......finished")
        else:
            print("Transforming the dictionary into a dataframe", end='')
            df2 = pd.DataFrame([file_dict])
            file_dict = None
            print("......finished")
            print("Concatenating the dataframes", end='')
            table = pandas.concat([df1, df2], ignore_index=True)
            print("......finished")
            print("Clearing memory", end='')
            df2 = None
            df1 = table
            table = None
            print("......finished")
        
        print(df1.shape)
        
        cont += 1
    print("Saving dataframe to disk")
    save_dataframe(df1)
    print("......finished")


if __name__ == '__main__':
    main()
