# Module: dictform. Data to Python dictionary converter. Works with strings, iterables, txt and csv (use encoding='utf-8-sig') files.
# Developed by D. Jenkins, Inpyosis LLC March 20, 2024

def dictform(data):
    '''Converts a string of back-to-back paired terms or a group of iterable pairs into a Python dictionary.'''
    converter = {}

    if isinstance(data, str):
        if "\n" in data:
            transform = data.split("\n") #    
            for item in transform:
                pair = [p.strip('"') for p in item.split(",", 1)]
                if len(pair) >= 2:
                    key = pair[0].split()
                    base_word = " ".join(key)
                    companion_word = pair[1]
                    converter[base_word] = companion_word
        else:
            transform = data.split(",")
            for t in range(0, len(transform), 2):
                key = transform[t].strip('"').split()
                base_word = " ".join(key)
                if t + 1 < len(transform):
                    companion_word = transform[t + 1].strip('"')
                    converter[base_word] = companion_word    
    else:
        for item in data:
            if len(item) == 2:
                item1, item2 = item
                converter[str(item1).strip('"')] = str(item2).strip('"')
            else:
                transform = list(data)
                for item1, item2 in zip(transform[0::2], transform[1::2]):
                    base_word = item1.strip('"')
                    companion_word = item2.strip('"')
                    converter[base_word] = companion_word

    return converter


if __name__ == "__main__":
    print(dictform(['shirt', '45', 'car', '29000']))
    print(dictform(('jean', '65', 'couch', '1800')))

    data1 = 'thin, fat, short, tall, smooth, coarse,'
    data2 = ['shirt', 'camesa', 'car', 'coche', 'beach', 'playa']
    data3 = ('shirt', '45', 'car', '29000')
    data4 = (('shirt', 'camesa'), ('car', 'coche'), ('beach', 'playa'))
    data5 = 'hotdog, cheap, soda, cheaper'
    data6 = 'hotdog, 6, cream soda, 2, maple covered peanuts, 9'
    data7 = 'hotdog special, 6, soda, 2'
    data8 = ['italian sausage', 'cheese pizza', 'orange soda', 'french fries']

    print(dictform(data1))
    print(dictform(data2))
    print(dictform(data3))
    print(dictform(data4))
    print(dictform(data5))
    print(dictform(data6))
    print(dictform(data7))
    print(dictform(data8))
    
    taste = "Burbon Hot Chocolate, 8, Rasberries & Cream, Sweet Tea, 4, Maple Pancakes (GF), 12, Bacon Delight, 5.50, Lamb & Eggs, 9.75, Basil Veggies, 8.75, Eggs, 5"

    mytaste = dictform(taste)
    print(mytaste)

    assert (dictform('thin, fat, short, tall, smooth, coarse,'))
    assert (dictform(['shirt', 'camesa', 'car', 'coche', 'beach', 'playa']))
    assert (dictform(('shirt', 'camesa', 'car', 'coche', 'beach', 'playa')))
    assert (dictform((('shirt', 'camesa'), ('car', 'coche'), ('beach', 'playa'))))
    assert (dictform('hotdog, cheap, soda, cheaper' ))
    assert (dictform('hotdog, 6, soda, 2' ))
    assert (dictform('hotdog special, 6, soda, 2' ))
    assert (dictform(['italian sausage', 'cheese pizza', 'orange soda', 'french fries']))


    # Demonstration that this works with txt files containing a pair of words on each line
    with open('progressives.txt', mode='r') as file:
        prunes = file.read()
        print(dictform(prunes))

    with open('garden.txt', mode='r') as file1:
        seed = file1.read()
        print(dictform(seed))

    with open('fruit.txt', mode='r') as file2:
        skillet = file2.read()
        print(dictform(skillet))

    with open('menutest.txt', mode='r') as file:
        skill = file.read()
        print(dictform(skill))

    with open('menu.txt', mode='r') as file:
        skill = file.read()
        print(dictform(skill))

    # Also works with csv files
    with open('word pairs.csv', mode='r', encoding='utf-8-sig') as file3:
        leaves = file3.read()
        print(dictform(leaves))
        
