def hp(n):
    if n==1:
        return 1
    return 1/n+hp(n-1)
n=int(input())
print(hp(n))
