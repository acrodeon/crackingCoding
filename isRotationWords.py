##Assume you have a method isSubstring which checks if one word is a substring of another.
##Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring
##(i.e., “waterbottle” is a rotation of “erbottlewat”).


def isRotationWords(s1, s2):
    if len(s1) != len(s2):
        return False
    t = s1 + s1
    return s2 in t




if __name__ == "__main__":
    s1 = "apple"
    s2 = "ppale"
    print("{} and {} are {} rotated words".format(s1,s2,isRotationWords(s1,s2)))
    
