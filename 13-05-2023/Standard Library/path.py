from pathlib import Path    

# Windows
Path("C:\\Users\\Al\\Downloads")
Path(r"C:\Users\Al\Downloads")

# Linux
Path("/usr/local/bin")

# Relative
Path("ecommerce/__init__.py")
Path() / "ecommerce" / "__init__.py"
Path.home()

# Path: Standard Library/pathlib.py
# exists()
# is_dir()
# is_file()
# mkdir()
# rmdir()
# glob()
# iterdir()
# name
# suffix
# stem
# parent
# stat()
# touch()
# unlink()
# rename()
# replace()
# absolute()