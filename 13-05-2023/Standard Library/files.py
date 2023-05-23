from pathlib import Path

path = Path("Standard Library\path.py")

print(path.exists())
print(path.stat())

# file creation time
from time import ctime
print(ctime(path.stat().st_ctime))
print(path.read_text())

# path.read_bytes()
# path.write_text('#Hello World')

# copy file from one location to another
source = Path("Standard Library\path.py")
target = Path() / "__init__.py"
target.write_text(source.read_text())

# copy file from one location to another using shutil
from shutil import copy
copy(source, target)
