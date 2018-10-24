import re

hammon = open("Scarletletter.txt", "r")
sendo = hammon.read()
def finder(word):

    if type(word) != str:
        raise TypeError("this is not a string")

    matches = re.findall(r"\w*at\b", sendo)

    findings = []

    for word in matches:

        if len(word) > 3:
            findings.append(word)
    print findings
finder(sendo) 
