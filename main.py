print('Loading applications...')
# Import modules and application files
import sys, subprocess, os, time, shutil
import importlib
try:
    from am_ignore import *
except:
    print('WARNING: Failed to import am_ignore file. This might be because the file was deleted. This can result in AM loading folders that should not be loaded.')
    print(' ')

projectFolders = []
for _, dirnames, _ in os.walk(os.getcwd()):
    for dirname in dirnames:
        try:
            if dirname.startswith('.') or (dirname in ignored_projects):
                continue
        except:
            pass
        projectFolders.append(dirname)
    break

projectModules = []
count = 0
for folder in projectFolders:
    sys.path.insert(1, os.path.join(os.getcwd(), folder))
    try:
        module = importlib.import_module(folder[0].lower() + folder[1::], package=None)
        projectModules.append(module)
    except:
        print('LOAD ERROR: Could not load application \'{}\'. Please ensure that this application meets load requirements of AM.'.format(folder))
        projectFolders.pop(count)
    count += 1
    
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

print('Loading complete!')
print(' ')

def mainLoop():
    # Launch options
    options = projectFolders
    print('Options:')
    
    count = 0
    for option in options:
        print("\t{} - {}".format(count, option))
        count += 1
    print(' ')
    choice = input('Enter your choice: ')

    # String commands
    if choice == 'exit':
        print('Bye!')
        exit()
    elif choice.startswith('import'):
        if choice[7::] == '':
            print('Please enter a the path to the folder to import.')
            print('Restarting AM...')
            print(' ')
            mainLoop()
            exit()
            
        if not os.path.isdir(choice[7::]):
            print('Given path is not directory. Please give the path of a directory to import.')
            print('Restarting AM...')
            print(' ')
            mainLoop()
            exit()
        # Import project at a differnt folder location
        ## Get name of folder
        print(' ')
        print('Preparing to import folder...')
        folderName = ''
        for char in choice[::-1]:
            if char == '/':
                break
            folderName = char + folderName
        
        time.sleep(1)
        print('Importing folder...')
        os.mkdir(os.path.join(os.getcwd(), folderName))
        copytree(choice[7:], os.path.join(os.getcwd(), folderName))
        
        time.sleep(1)
        print('Folder \'{}\' imported successfully!'.format(folderName))
        print(' ')
        print('Please ensure that the project folder meets the requirements for being loaded by AM.')
        print('Failure for the project folder to meet the requirements can cause AM to skip loading the folder.')
        print('Refer to requirements.md for more information.')
        
        time.sleep(3)
        print(' ')
        print('Restarting AM to attempt to load new imported directory...')
        print(' ')
        
        # Restart AM with shell command...
        if not ("idlelib" in sys.modules):
            print(' ')
            if sys.platform == 'win32':
                cmd = 'python main.py'
                subprocess.check_call(cmd, shell=True)
                exit()
            else:
                cmd = 'python3 main.py'
                subprocess.check_call(cmd, shell=True)
                exit()
        else:
            print(' ')
            print('Sorry, AM seems to be running on IDLE and cannot restart itself.')
            print(' ')
            print('You will have to manually start AM.\nOpen up the \'main.py\' file inside the AM folder in IDLE and click Run > Run Module to launch AM.')
            time.sleep(4)
            print('Terminating app for manual restart...')
            exit()
    
    # Int choices
    if not choice.isdigit():
        print('Please enter a number!')
        print('Restarting AM...')
        print(' ')
        mainLoop()
        exit()
    elif int(choice) > (len(options) - 1):
        print('Invalid Choice!')
        print('Program failed. Bye!')
        exit()
    
    # Load selected module
    def appLaunch():
<<<<<<< HEAD
        # try:
        print('LAUNCH: {}'.format(options[int(choice)]).upper())
        print(' ')
        router.amMainRun(projectFolders[int(choice)], projectFolders[int(choice)][0].lower() + projectFolders[int(choice)][1::])
        # except AttributeError:
        #     print('LAUNCH ERROR: Failed to launch application. This is likely because there was an error in running the AM BootLoader router file.')
=======
        try:
            print('LAUNCH: {}'.format(options[int(choice)]).upper())
            print(' ')
            projectModules[int(choice)].amMainRun()
        except AttributeError:
            print('LAUNCH ERROR: Failed to launch application. Please check that the application meets the amMainRun() function requirement.')
            
>>>>>>> parent of b142a32... Transforming to new loader system...
    while True:
        appLaunch()
        print(' ')
        print('APPLICATION ENDED.')
        rerunOption = input('Would you like to rerun? (y/n) ').lower()
        if rerunOption == 'y':
            print(' ')
            continue
        elif rerunOption == 'n':
            exit()
        else:
            print('Invalid input. Terminating program...')
            time.sleep(2)
            exit()
mainLoop()