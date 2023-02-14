import random

curso = [0, 0]
curso[0] = ["Ciencias Biologicas"]
curso[1] = ["Farmacia"]
counter = [0, 0]
with open("CIÊNCIAS_BIOLÓGICAS.txt") as data:
    for row in data:
        curso[0].append(row)
with open("FARMÁCIA.txt") as data:
    for row in data:
        curso[1].append(row)
order = [0] * (len(curso[0]) - 1) + [1] * (len(curso[1]) - 1)
random.shuffle(order)
print(f"1: {order.count(1)} 0:{order.count(0)}")
print(len(order))
results = [None] * 2
results[0] = list(range(1, len(curso[0])))
results[1] = list(range(1, len(curso[1])))
random.shuffle(results[0])
random.shuffle(results[1])
par = 0
impar = 0
for i in range(0, len(order)):
    if order[i] == 0:

        print(curso[order[i]][results[order[i]][par]])
        print(end="\n\n\n\n")
        par += 1
    else:
        print(curso[order[i]][results[order[i]][impar]])
        print(end="\n\n\n\n")
        impar += 1
    answer = "inicialized"
    while answer != "S" and answer != "N":
        answer = input("S para Sim e N para Não: ",)
    if answer == "S":
        counter[order[i]] += 1
    print(end="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(f"{curso[0][0]}: {(counter[0])} Total: {order.count(0)} Afinidade:{round(float(counter[0])/order.count(0)*100 , 2)}%")
print(f"{curso[1][0]}: {(counter[1])} Total: {order.count(1)} Afinidade:{round(float(counter[1])/order.count(1)*100 , 2)}%")
