#!/usr/bin/env python3

# standard library imports
import shutil       # shell utilities will be used to move files
import os           # proves access to low level os operations (agnostic to flavor of OS)


def main():
    """called at runtime"""
    os.chdir("/home/student/mycode/")
    shutil.move("raynor.obj", "ceph_storage/")
    
    # program will pause while we accept input
    xname = input("What is the new name for kerrigan.obj? ")            # collect string input from the user
    shutil.move("ceph_storage/kerrigan.obj", "ceph_storage/" + xname)   # moving kerrigan.obj into 
                                                                        # ceph_storage/ with new name


main() # this calls our main function
