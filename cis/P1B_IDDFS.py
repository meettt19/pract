from RMP import dict_gn

start = 'Arad'
goal = 'Bucharest'
result = ''

def DLS(city, visitedstack, startlimit, endlimit):
    global result
    result = result + city + ' '

    visitedstack.append(city)

    if city == goal:
        return 1

    if startlimit == endlimit:
        return 0

    for eachcity in dict_gn[city].keys():
        if eachcity not in visitedstack:
            found = DLS(
                eachcity,
                visitedstack,
                startlimit + 1,
                endlimit
            )

            if found:
                return found

    return 0


def IDDFS(city, visitedstack, endlimit):
    global result

    for i in range(0, endlimit):
        print("Searching at limit:", i)

        result = ''
        visitedstack.clear()

        found = DLS(city, visitedstack, 0, i)

        if found:
            print("Found!")
            print(result)
            break
    else:
        print("Not Found!")


def main():
    visitedstack = []

    IDDFS(start, visitedstack, 9)

    print("IDDFS Traversal from", start, "to", goal, "is:")
    print(result)


main()
