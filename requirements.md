# Requirements for running AM

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Custom Project Loading and Setup](#project-loading-and-setup)


## System Requirements
AM is written in Python 3.8.8.

The following are the Software Requirements for running AM:

- Windows 10 (Build 10240, 2015 release) or later
- macOS Version 10.13 or later

**All other operating systems are not supported.**

All Software versions require Python version 3.8.8 or later. [Download the latest Python version here.](https://www.python.org/downloads/)

AM can either be run via the command line (Terminal/Command Prompt) or in the Python's IDLE (Integrated Development and Learning Environment).

## Project Loading and Setup
The AM Loader makes the following assumptions when loading a project:
1) The project is in the same directory as the `main.py` file of AM.
2) The projects main runtime file follows the naming requirement of the name of the project folder but the first character to be in lower case. For example, a project folder called `MyCoffeeMaker` project would have the main runtime file of `myCoffeeMaker.py`. The main runtime file must also be in the root of the project folder.
3) The main runtime file has all its code wrapped in a function called `amMainRun()`. the AM will call this function when the project is chosen to be launched. (If you do not wish to do this, check [below for an alternative method](#alternative-to-wrapping-the-main-runtime-file-in-a-function) to have the AM call the main runtime file.)

Failure to meet any of these requirements will result in AM skipping the project and not loading it. If it still loads it, there's a good chance it will throw an error when the project is launched.

Here is a complete example of a project that will load correctly:

A project called `MyCoffeeMaker`:
```
AM
├── main.py
├── MyCoffeeMaker
    ├── myCoffeeMaker.py
    ├── other project files...
``` 

Inside the `myCoffeeMaker.py` file:
```python
import time
def amMainRun():
    # Your code here
    print('Making Coffeeeee for ya!')
    time.sleep(5)
    print('Coffee is ready!')
```

### Alternative to wrapping the main runtime file in a function
If you do not wish to wrap your project code in a `amMainRun()` function, you can create what's called a router file instead.

A router file is a file that contains a function called `amMainRun()` that is called when the project is chosen to be launched. It then redirects the python thread to the main runtime file.
It does this by importing and executing the main runtime file.

The router file must also be in the root of the project folder and follow the naming requirements of the project folder name but the first character to be in lower case.
For example, the router file for the project above would be `myCoffeeMaker.py`. 

**IMPORTANT: The main runtime file that the router file redirects to must NOT be named `main.py`. It can be named anything except for `main.py`.**
(This is due to the way the AM Loader has to load the project.)

Here is a complete example of a project with a router file that will load correctly:

A project called `MySandwichMaker`:
```
AM
├── main.py
├── MySandwichMaker
    ├── mySandwichMaker.py
    ├── sandwichMain.py
    ├── other project files...
```

Inside the `mySandwichMaker.py` file:
```python
# THIS IS THE ROUTER FILE #
import sys, os
def amMainRun():
    sys.path.insert(1, os.path.join(os.getcwd(), 'MySandwichMaker')) # Change the path to the project folder
    import sandwichMain # Executes the sandwichMain.py main runtime file
```

Inside the `sandwichMain.py` file:
```python
# Your code here
import time
print('Making a sandwich for ya!')
time.sleep(5)
print('Sandwich is ready!')
```

For a more complete example, check out the in-built project `StickyMeet` at the root of the repository whose router file is `stickyMeet.py` and main file is `sMain.py`.
