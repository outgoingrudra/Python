import os
print("Before:", os.getcwd())
os.chdir("..")
print("After:", os.getcwd())
