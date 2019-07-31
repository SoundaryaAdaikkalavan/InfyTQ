def prefixsuffix(s):
    n=len(s)
    for i in range(n//2,0,-1):
        prefix=s[0:i]
        suffix=s[n-i:n]
        if prefix==suffix:
            return i
    return 0
s=input()
print(prefixsuffix(s))
