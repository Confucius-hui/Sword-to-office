n = input()
lists = []
for i in range(int(n)):
    row = input().split(' ')
    row = list(map(lambda x:int(x),row))
    lists.append(row)

