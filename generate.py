def gen(dim, numberOfPoints):
    import random
    return [[random.randint(1,100) for i in range(dim)] for j in range(numberOfPoints)]