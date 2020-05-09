import filecmp 
import glob
from pathlib import Path

path1= '/home/harumiki/python/a'
path2= '/home/harumiki/python/b'


path3= '/home/harumiki/python/a/*'
path4= '/home/harumiki/python/a/'

filecmp.dircmp(path1,path2).report()

f=glob.glob(path3)
print(f)

p_tmp = Path(path4).glob("*")
print(p_tmp)

file_list=[]

for p in p_tmp:
    file_list.append(p.name)
    print(p.name)

print(file_list)

p_temp = list(Path(path4).glob('*'))
print(p_temp)
