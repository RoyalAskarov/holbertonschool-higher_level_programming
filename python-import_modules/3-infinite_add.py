#!/usr/bin/python3
import sys
if __name__ == "__main__":
    total = 0
    # Loop through arguments starting from index 1
    # (Index 0 is the script name, so we skip it)
    for arg in sys.argv[1:]:
        total += int(arg)
    print(total)
