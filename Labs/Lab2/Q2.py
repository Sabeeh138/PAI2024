# function to check whther last letter is vowel
def lastletter(intstring):
    intstring.lower()
    # vowels list in lowercase
    vowels = ['a', 'e', 'i', 'o', 'u']
    lastletter = intstring[-1]
    
    if lastletter in vowels:
        return "Last letter is indeed a vowel sire"
    else:
        return "Last letter is actually a consonant"
    
    
userint = input("Please enter a string: ")
result = lastletter(userint)
print(result)
