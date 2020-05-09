from pathlib import Path

nums1 = [1, 2, 3, 4, 5]
nums2 = [3, 4, 5, 6, 7]
str1 = ['a','b','c']
str2 = ['a','b']
str3 = ['test']

print(list(set(nums1) | set(nums2)))
print(list(set(nums1) - set(nums2)))

#print(list(set(str1) | set(str(str2))))
print(list(set(str1) - set(str(str2))))

str2.append('c')

print(list(set(str1) - set(str(str2))))

path4= '/home/harumiki/python/a/'

p_tmp = Path(path4).glob("*")
file_list=[]

for p in p_tmp:
    file_list.append(p.name)
    print(p.name)

print(file_list)

print(list(set(file_list) - set(str3)))

