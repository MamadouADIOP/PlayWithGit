import pathlib

# path of the given file modified in  frontend branch
print(pathlib.Path("my_file.txt").parent.absolute())

# current working directory modified in frontend branch
print(pathlib.Path().absolute())
