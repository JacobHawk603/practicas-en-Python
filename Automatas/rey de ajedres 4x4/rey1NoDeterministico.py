from multiprocessing import Pool

def cubo(valor):
    valor+=1
    return valor**3

def main():
    print(Pool().map(cubo, [2,3,5]))

if __name__ == "__main__":
    main()