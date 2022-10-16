from typing import List
import matplotlib.pyplot as plt

from load import load_citeseer, load_cora, load_pubmed

map = dict()
adjmap = dict()
routers = []
reordermap = []
checked = []
mapsizethreshold = 5
x = []
y = []


def printPlot(filename=""):
    s = set(reordermap)
    i = 0
    maparr = dict()
    for node in reordermap:
        maparr[node] = i
        i += 1
    for node in range(len(map)):
        if node in s:
            continue
        maparr[node] = i
        i += 1
    plt.scatter([maparr[newx] for newx in x],
                [maparr[newy] for newy in y], s=1)
    if not filename:
        plt.show()
    else:
        plt.savefig(fname="img/{0}".format(filename))
    plt.cla()


def reduce(threshlod=15, round=1):
    localrouter = []
    routerneighbor = set()
    print("round {0}".format(round))
    for key in adjmap:
        if checked[key] or len(adjmap[key]) < threshlod:
            continue

        print("find {0} as a router".format(key))
        localrouter.append(key)
        reordermap.append(key)
        for item in adjmap[key]:
            routerneighbor.add(item)
        checked[key] = True
    islandization(list(routerneighbor))
    printPlot(str(round))
    if False in checked:
        reduce(threshlod-1, round+1)


def islandization(neighbor: List[int]):
    threshold = 25
    for node in neighbor:
        localchecked = []
        done = True
        curarr: List = list(adjmap[node])
        cnt = 0
        while len(curarr) > 0:
            curnode = curarr[0]
            curarr.remove(curnode)
            if cnt > threshold:
                done = False
                break
            if curnode in localchecked or checked[curnode]:
                continue
            cnt += 1
            localchecked.append(curnode)
            for node in adjmap[curnode]:
                if node in localchecked or checked[curnode]:
                    continue
                curarr.append(node)
        if done and len(localchecked) > 0:
            for node in localchecked:
                reordermap.append(node)
                checked[node] = True


x, y, map, adjmap = load_pubmed()
# x, y, map, adjmap = load_citeseer()
# x, y, map, adjmap = load_cora()
checked = [False for _ in range(len(map))]
printPlot("0")
reduce()
