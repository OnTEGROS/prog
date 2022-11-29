def reading(file, encoding):
    list = []
    try:
        open(file, encoding = encoding)
    except FileNotFoundError:
        print(f"Soubor '{file}' nebyl nalezen!")
        return list
    file = open(file, encoding = encoding)
    for line in file:
        data = line.rstrip()
        list.append(data)
    return list

print(reading('text.txt', 'utf-8'))
print(reading('text2.txt', 'utf-8'))

print("")
print("/// úkol 2 ///")
print("")

def search(key, value, dic):
    if dic.get(key) == value:
        return True
    elif dic.get(key) == None:
        print("Klíč nenalezen!")
        return False
    else:
        return False


print(search(1, "jedna", {1:"jedna",2:"dva",3:"tři"}))
print(search(2, "jedna", {1:"jedna",2:"dva",3:"tři"}))
print(search(4, "jedna", {1:"jedna",2:"dva",3:"tři"}))
print(search(1, "čryři", {1:"jedna",2:"dva",3:"tři"}))