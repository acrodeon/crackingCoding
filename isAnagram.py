

def isAnagram (u,v):
    return sorted(u) == sorted(v)

if __name__ == '__main__':
    w1 = "abcdaa"
    w2 = "aaadbc"
    w3 = "vvvdev"
    print(w1, w2, isAnagram(w1,w2))
    print(w3, w2, isAnagram(w3,w2))
          
