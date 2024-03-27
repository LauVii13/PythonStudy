for _ in range(int(input())):
    n = int(input())
    lista = [""] * n
    dicionario = {}
    out = ""

    for i in range(n):
        lista[i] = input()
        dicionario[lista[i]] = 1

    for i in range(n):
        palavra = lista[i]

        if len(palavra) <= 1:
            out += "0"
            continue

        encontrou = False
        for j in range(1, len(palavra)):
            if (
                dicionario.get(palavra[:j]) != None
                and dicionario.get(palavra[j:]) != None
            ):
                encontrou = True
                continue

        if encontrou:
            out += "1"
        else:
            out += "0"

        encontrou = False

    print(out)
