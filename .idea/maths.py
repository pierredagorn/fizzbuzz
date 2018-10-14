
def somme_cubes(n):
    somme = 0
    for i in range(1,n+1):
        somme = somme + i**3
    return somme


def somme_entiers(n):
    return n*(n+1)/2

x=3
sommecube = somme_cubes(x)
carresommeentier = somme_entiers(x)**2

if sommecube == carresommeentier:
    print("Les deux valeurs", sommecube, "et" , carresommeentier, "sont égales" )
else:
    print("Les deux valeurs", sommecube, "et", carresommeentier, "ne sont pas égales")

n=4
def list(n):
    for i in range(1, n+1):
        print("the numbers are", i)
    for i in range(0, n):
        print("the numbers are", i)
liste1 = [list(n)]

