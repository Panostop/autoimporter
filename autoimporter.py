import pip
from os import system

def autoimporter(*func):
    try:
        func

    except ImportError as e:
        print("\nCould not find '{}' module, installing it...".format(e.name))
        try:
            system('python -m pip install {}'.format(e.name))

        except:
            print("Could not install the'{}' module. exiting...\n".format(e.name))
            exit()

        else:
            print("Module installed, importing it...")
            func


    else:
        print("Modules importés\n")
