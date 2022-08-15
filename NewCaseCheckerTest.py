import os.path
import sys
from NewCaseChecker import main

def NewCaseCheckerTest():
    try:
        exists = os.path.exists("NewCaseChecker.py")
        assert exists == True
    except:
        sys.exit()

    assert main() == "hello world"
