from pathlib import Path

# Absolute path
# Relative path

Path() # current dir
path = Path("../ecommerce") # current dir
print(path.exists())

path = Path("emails")
path.mkdir()
path.rmdir()

path = Path("../")
for file in path.glob('*'):
    print(file)
