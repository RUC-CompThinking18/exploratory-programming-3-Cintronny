import re

hammon = open("Scarletletter.txt", "r")
sendo = hammon.read()
def finder(word):

    if type(word) != str:
        raise TypeError("this is not a string")
#this catches if the argument is a string and raises a TypeError if it is not
    matches = re.findall(r"\w*at\b", sendo)

    findings = []

    for word in matches:

        if len(word) > 3:
            #this searches through the list and removes the words that are 3 letters or less
            findings.append(word)
    print findings
finder(sendo) 
