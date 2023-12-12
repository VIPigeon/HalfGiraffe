
def inputAnswers():
    res = {}
    average = 0
    for p in sorted(players.keys()):
        answer = float(input(f"{p}\n>"))
        res[p] = answer
        average += answer
    return res


def calculate(answers):
    global players
    average = 0
    for name, answer in answers.items():
        average += answer
    average /= len(players)
    print("Average:", average)
    res = []
    for name, answer in answers.items():
        res.append((abs(answer - average), name))
    res.sort()
    players[res[0][1]].append(1)
    place = 1
    for i in range(1, len(players)):
        if res[i][0] != res[i - 1][0]:
            place += 1
        players[res[i][1]].append(place)


def printPlayers():
    for p in sorted(players.keys()):
        print(f"{p}: {sum(players[p])} = {' + '.join(map(str, players[p]))}")


tasks = ["There is no task"]
with open("HalfGiraffe.txt", 'r') as f:
    for line in f.readlines():
        tasks.append(line)


names = input("Enter player names (separated by spaces)\n>").split()

players = {}
for name in names:
    players[name] = []

while True:
    taskNumber = int(input(f"Enter task number (integer from 1 to {len(tasks) - 1})\n>"))
    if taskNumber >= len(tasks) or taskNumber < 0:
        print(tasks[0])
        continue
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(tasks[taskNumber], end='')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    calculate(inputAnswers())
    printPlayers()
