n , m = map(int, input().split())

dic_votos = {}
vote = list(map(int, input().split()))

max_index = vote[0]

for i in range(m):
    dic_votos[vote[i]] = dic_votos.get(vote[i], 0) + 1
    
    if dic_votos[vote[i]] > dic_votos[max_index]:
        max_index = vote[i]
    elif dic_votos[vote[i]] == dic_votos[max_index] and vote[i] < max_index:
        max_index = vote[i]
             

    print(max_index)