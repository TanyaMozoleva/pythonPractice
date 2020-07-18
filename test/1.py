def array(string):
    index = string.find(',')
    if index == -1:
        return
    string = string[index + 1:]
    
    index = string.rfind(',')
    if index == -1:
        return
    string = string[: index]
    
    index = 0
    while index < len(string):
        if string[index] == ',':
            string = string[: index] + ' ' + string[index + 1:]
        index = index + 1

    return string.strip()


print(array(''))
print(array('1'))
print(array('1, 3'))
print(array('1,2,3'))  # 2
print(array('1,2,3,4'))
print(array('6c2,f2c,3d1,b,e1'))
