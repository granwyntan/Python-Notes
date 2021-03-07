def findDigit(equation):
    exp, result = str(equation).split("=")
    numb1, numb2 = str(exp).split("*")
    resultlist = list(result)
    diffOccur = 0
##    ## print(numb1)
##    ## print(numb2)
##    ## print(result)
    if "?" in result:
        actualresult = list(str(float(numb1)*float(numb2)))
        if float(numb1)*float(numb2) > 9999:
            return -1
        for i in range(len(result)):
            if resultlist[i] != actualresult[i]:
                finalnumber = actualresult[i]
    elif "?" in numb1:
        ## print(numb1)
        ## print(numb2)
        ## print(result)
        n1thing = float(result)/float(numb2)
        ## print(float(result) % float(numb2))
        if (float(result) % float(numb2) != 0) == True:
            return -1
        elif (n1thing % 1 != 0) == True:
            return -1
        else:
            actualn1 = str(int(n1thing))
            for i in range(len(actualn1)):
                if actualn1[i] != numb1[i]:
                    diffOccur += 1
            if diffOccur > 1:
                return -1
            else:
                return actualn1[numb1.index("?")]
##            for i in range(len(numb1)):
##                if n1list[i] != actualn1[i]:
##                    finalnumber = actualn1[i]
    elif "?" in numb2:
        n2thing = float(result)/float(numb1)
        if (float(result) % float(numb1) != 0) == True:
            return -1
        elif (n2thing % 1 != 0) == True:
            return -1
        else:
            actualn2 = str(int(n2thing))
            for i in range(len(actualn1)):
                if actualn2[i] != numb2[i]:
                    diffOccur += 1
            if diffOccur > 1:
                return -1
            else:
                return actualn2[numb2.index("?")]
##            for i in range(len(numb2)):
##                print(n2list[i])
##                print(actualn2[i])
##                if n2list[i] != actualn2[i]:
##                    finalnumber = actualn2[i]
#### print(findDigit("?5*41=2665"))
#### print(findDigit("9?54*1=9254"))
#### print(findDigit("7?*1=72"))
#### print(findDigit("6*?=42"))
print(findDigit("94?4*1=9254"))
#### print(findDigit("6480*1=648?"))
