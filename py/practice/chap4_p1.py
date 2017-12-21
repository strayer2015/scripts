#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6



def appendList(lista):
    string=''
    for ii in range(len(lista)-1):
        string=string+lista[ii]+', '

    string = string + lista[-1]
    return string

spam = ['apples', 'bananas', 'tofu', 'cats']
print(appendList(spam))
