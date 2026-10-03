my_name = ['D', 'a','n', 'd', 'a', 'r', 'a', ' ', 'M','a','r','i','a','m','a',' ','P','a','i','v','a',' ', 'd','e',' ','S','o','u','s', 'a']
name_in_bin = ""
for item in my_name:
    asc = ord(item)
    convert = bin(asc)
    name_in_bin += convert
    
print(name_in_bin)
    
