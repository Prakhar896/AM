import os, sys, importlib

def amMainRun(folderName, fileName):
    sys.path.insert(1, os.path.join(os.getcwd(), folderName))
    try:
        # Execute file
        importlib.import_module(folderName[0].lower() + folderName[1::], package=None)
    except FileNotFoundError:
        print('LOAD ERROR: Could not load application \'{}\'. Please ensure that this application meets load requirements of AM.'.format(folderName))