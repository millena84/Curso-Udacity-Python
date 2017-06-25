#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    ================================================================
    Exercise Udacity course "Programming Foundations with Python"
    Lesson 2: Use functions - P2: rename files
    -------------------------------------------------------------

    In this exercise, we need to rename a bunch of files that are
    recorded in some folder in the computer. The objective is
    rename the files by removing the numbers (all files have number
    in their names). The instructor says that we have to:
    (1) get the file names from a folder
    (2) for each file, rename

    We can describe more steps, like:
    1) get the file names from a folder
    2) show all the file names
    3) show the file names after they are renamed
    4) open a window with the folder after all the names are
        renamed [in a new version]

    -----------------------------------------------------------------

    Modules that we use in this program:
    - os: module with functions related with operational system.
        You can manipulate paths, open and write files, file names
        and other things.
    - xx?

    Functions used in this program:
    - os.listdir = given a path, return the file names contained in
        the folder.
        syntax: os.listdir("path")
    - xxx.xxx = makes the program sleep for a number off seconds
        syntax: xxx

    ================================================================|																#
"""

## só funciona rodando no Python3
import os

# to create a function:
def rename_files():
    # step 1: choose the folder where are the files

    # os.listdir = list all the names of files in a folder
    file_list = os.listdir("/home/millena/Desktop/Cursos/Udacity-Python/rename-files")
    saved_path = os.getcwd()
    table = str.maketrans(dict.fromkeys('0123456789'))

    print(file_list)

    # step 2: while there is some file with a number on the name:
    # step 2.1: edit the name of the file
    os.chdir("/home/millena/Desktop/Cursos/Udacity-Python/rename-files")

    for file_name in file_list:
        # step 2.2: remove the number
        # step 2.3: rename the files
        print("Old Name - " + file_name)
        print("New Name - " + file_name.translate(table))
        os.rename(file_name, file_name.translate(table))
    os.chdir(saved_path)

rename_files()