import os
for root, dirs, files in os.walk("."):
    print("Directory:", root)
    for file in files:
        print("  File:", file)
