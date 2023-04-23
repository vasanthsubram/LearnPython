import os
from pathlib import Path

print()
filename = os.getcwd()
print(os.getcwd())

newPath = Path('/Users').joinpath('vsubramanian').joinpath('Documents')

os.chdir(newPath)
print(os.getcwd())

#list dir
print("contents of dir = " , os.getcwd())
print(os.listdir(os.getcwd()))

total_size = 0
for sub_path in Path(os.getcwd()).iterdir():
  total_size += sub_path.stat().st_size
print(total_size)

#go back in the path
print(Path('..').resolve())