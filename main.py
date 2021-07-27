print('Loading applications...')
# Import modules and application files
import sys, subprocess, os, time, shutil
import importlib

projectFolders = []
for _, dirnames, _ in os.walk(os.getcwd()):
    for dirname in dirnames:
        if dirname == '__pycache__':
            continue
        elif dirname == '.git':
            continue
        projectFolders.append(dirname)
    break

projectModules = []
for folder in projectFolders:
    sys.path.insert(1, os.path.join(os.getcwd(), folder))
    try:
        module = importlib.import_module(folder[0].lower() + folder[1::], package=None)
        projectModules.append(module)
    except:
        print('LOAD ERROR: Could not load application \'{}\'. Please ensure that this application meets load requirements of AM.'.format(folder))
    
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
            
    elif int(choice) > (len(options) - 1):
        print('Invalid Choice!')
        print('Program failed. Bye!')
        exit()
    
    # Load selected module
    def appLaunch():
        try:
            print('LAUNCH: {}'.format(options[int(choice)]).upper())
            print(' ')
            projectModules[int(choice)].amMainRun()
        except AttributeError:
            print('Launch Error: Failed to launch application. Please check that the application meets the amMainRun() function requirement.')
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