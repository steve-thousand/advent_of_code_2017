valid = 0

def getAllCombosOfArray(array):
    if len(array) <= 1:
        return [array]
    combos = []
    for index, i in enumerate(array):
        array_copy = []
        array_copy.extend(array)
        array_copy.pop(index)
        all_sub_combos = getAllCombosOfArray(array_copy)
        for j in all_sub_combos:
            j.insert(1,i)
            combos.append(j)
    return combos

def buildAnagrams(string):
    combos = getAllCombosOfArray(list(string))
    anagrams = []
    for i in combos:
        anagrams.append("".join(i))
    return anagrams

with open("/Users/conrad/Desktop/adventofcode2017/4/input.txt", "r") as f:
    for line in f:
        columns = line.split();
        dictionary = set()
        for column in columns:
            anagrams = buildAnagrams(column)
            if len(dictionary.intersection(anagrams)) > 0:
                valid -= 1
                break
            else:
                dictionary.add(column)
        
        #if we get here, every thing in the passphrase is unique
        valid += 1

#223
print(valid)
