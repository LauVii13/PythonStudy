p1 = input()
p2 = input()
p3 = input()

result = ""

if p1 == "vertebrado":
    if p2 == "ave":
        if p3 == "carnivoro":
            result = "aguia"
        else:
            result = "pomba"
    else:
        if p3 == "onivoro":
            result = "homem"
        else:
            result = "vaca"
else:
    if p2 == "inseto":
        if p3 == "hematofago":
            result = "pulga"
        else:
            result = "lagarta"
    else:
        if p3 == "hematofago":
            result = "sanguessuga"
        else:
            result = "minhoca"
            
print(result)