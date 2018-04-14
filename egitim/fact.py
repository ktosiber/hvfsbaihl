def iterative_fact(n):
    x = 1
    liste = list(range(2,n+1))
    for listedeki_sayi in liste:
        x = x * listedeki_sayi    
    return x

def recursive_fact(n):
    if n == 0:
        return 1
    else:
        return n * recursive_fact(n-1) 