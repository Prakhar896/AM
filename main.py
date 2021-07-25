print('Loading applications...')
# Import modules and application files
import sys, subprocess, os, time
import importlib

projectFolders = []
for _, dirnames, _ in os.walk(os.getcwd()):
    for dirname in dirnames:
        if dirname == '__pycache__':
            continue
        projectFolders.append(dirname)
    break

projectModules = []
for folder in projectFolders:
    sys.path.insert(1, os.path.join(os.getcwd(), folder))
    module = importlib.import_module(folder[0].lower() + folder[1::], package=None)
    projectModules.append(module)

print('Loading complete!')
print(' ')

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
elif int(choice) > (len(options) - 1):
    print('Invalid Choice!')
    print('Program failed. Bye!')
    exit()
    
# Load selected module
try:
    print('LAUNCH: {}'.format(options[int(choice)]).upper())
    print(' ')
    projectModules[int(choice)].amMainRun()
except AttributeError:
    print('Launch Error: Failed to launch application. Please check that the application meets the amMainRun() function requirement.')
