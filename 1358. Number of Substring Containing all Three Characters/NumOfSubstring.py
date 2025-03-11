def numberOfSubstrings(s: str) -> int:

    count = 0

    left = 0
    right = -1

    a = 0
    b = 0
    c = 0

    while right < len(s):
        while not (a & b & c): 
            right += 1
            if right == len(s):
                break
            if s[right] == 'a':
                a += 1
            elif s[right] == 'b':
                b += 1
            elif s[right] == 'c':
                c += 1
        
        count += len(s) - right


        while a & b & c: 
            if s[left] == 'a':
                a -= 1
            elif s[left] == 'b':
                b -= 1
            elif s[left] == 'c':
                c -= 1                                        
            left += 1
            if a & b & c:
                count += 1
        

    return count

print(numberOfSubstrings("aaabc"))
