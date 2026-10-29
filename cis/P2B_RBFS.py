import queue as Q
from RMP import dict_gn
from RMP import dict_hn

start = 'Arad'
goal = 'Bucharest'
result = ''


def get_fn(citystr):
    cities = citystr.split(',')
    hn = gn = 0

    for ctr in range(0, len(cities) - 1):
        gn = gn + dict_gn[cities[ctr]][cities[ctr + 1]]

    hn = dict_hn[cities[-1]]

    return hn + gn


def printout(cityq):
    for i in range(cityq.qsize()):
        print(cityq.queue[i])


def expand(cityq):
    global result

    tot, citystr, thiscity = cityq.get()
    nexttot = 999

    if not cityq.empty():
        nexttot, nextcitystr, nextthiscity = cityq.queue[0]

    if thiscity == goal and tot <= nexttot:
        result = citystr + '::' + str(tot)
        return

    print("Expanded city --------", thiscity)
    print("Second best fn --------", nexttot)
    print("==============================")

    tempq = Q.PriorityQueue()

    for city in dict_gn[thiscity]:
        if city not in citystr.split(','):
            tempq.put((
                get_fn(citystr + ',' + city),
                citystr + ',' + city,
                city
            ))

    while not tempq.empty():
        ctrtot, ctrcitystr, ctrthiscity = tempq.get()

        if ctrtot < nexttot:
            cityq.put((ctrtot, ctrcitystr, ctrthiscity))
        else:
            cityq.put((ctrtot, ctrcitystr, ctrthiscity))
            break

    printout(cityq)

    if not cityq.empty():
        expand(cityq)


def main():
    cityq = Q.PriorityQueue()
    thiscity = start

    cityq.put((999, 'NA', 'NA'))
    cityq.put((get_fn(start), start, thiscity))

    expand(cityq)

    print("The Recursive Best-First path with the total is:")
    print(result.replace(',', ' '))


main()
