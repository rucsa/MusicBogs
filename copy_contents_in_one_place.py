#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:28:49 2020

@author: rucsa
"""

import shutil
import os
from os import path

def list_files(dir, copy_to_folder):                                                                                                  
    r = []   
    out = []                                                                                                         
    subdirs = [x[0] for x in os.walk(dir)]                                                                  
    for subdir in subdirs: 
        files = os.walk(subdir).__next__()[2]  
        if (len(files) > 0):      
            for file in files: 
                if ("DS_Store" not in file):                                                                                       
                    r.append(subdir + "/" + file)  
                    out.append(copy_to_folder + file)                                                                       
    return (r, out)  

def copy_files_from_lists (src, dest):
    if (len(src) == len(dest)): 
        for j in range (0, len(dest)):
            if path.exists(dest[j]):
                print("WARNING: File EXISTS " + dest[j] + " and will be replaced")
            else:
                print("File moved to" + dest[j] + "\n")
            shutil.copy(src[j], dest[j]) 
            
        print("Finished successfully! Copied " + str(len(dest)) + " files..")
    else:
        print ('ERROR: number of input files does not match number of output files')
        raise SystemExit
        
def main(copy_from_folder, copy_to_folder):
    i, o = list_files(copy_from_folder, copy_to_folder)
    
    if (len(i)==0):
        print('ERROR: 0 files in source')
        raise SystemExit
    elif (len(o)==0):
        print('ERROR: 0 files in destination folder')
        raise SystemExit
    else:
        copy_files_from_lists(i, o)      
    
if __name__ == "__main__":
    copy_from_folder = "./Contents/"
    copy_to_folder = "./results/"  
    
    if not os.path.exists(copy_to_folder):
        os.makedirs(copy_to_folder)
    
    
    print("\nThe script will copy all files from all subdirectories in:\n" + copy_from_folder + "-- into -> " + copy_to_folder)
    a = input("Hit Enter to continue ... || ... Press 0 to exit\n")
    
    if (a == ""):
        main(copy_from_folder, copy_to_folder)
    elif (a == "0"):
        print("Exit called by user...")
        

    




