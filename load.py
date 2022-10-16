def load_citeseer():
    x = []
    y = []
    adjmap = dict()
    map = dict()
    f = open("citeseer/citeseer.edges", "r")
    fc = open("citeseer/citeseer.node_labels", "r")
    i = 0
    for line in fc:
        a = line.split(",")[0]
        map[a] = i
        i += 1
    for line in f:
        [a, b, _] = [map[index]
                     for index in line.replace("\n", "").split(",")]
        if a not in adjmap:
            adjmap[a] = [b]
        else:
            adjmap[a].append(b)

        if b not in adjmap:
            adjmap[b] = [a]
        else:
            adjmap[b].append(a)
        x.append(a)
        x.append(b)
        y.append(b)
        y.append(a)
    return x, y, map, adjmap


def load_cora():
    x = []
    y = []
    adjmap = dict()
    map = dict()
    f = open("cora/cora.cites", "r")
    fc = open("cora/cora.content", "r")
    i = 0
    for line in fc:
        a = line.split("\t")[0]
        map[a] = i
        i += 1
    for line in f:
        [a, b] = [map[index] for index in line.replace("\n", "").split("\t")]
        if a not in adjmap:
            adjmap[a] = [b]
        else:
            adjmap[a].append(b)

        if b not in adjmap:
            adjmap[b] = [a]
        else:
            adjmap[b].append(a)
        x.append(a)
        x.append(b)
        y.append(b)
        y.append(a)
    return x, y, map, adjmap


def load_pubmed():
    x = []
    y = []
    adjmap = dict()
    map = dict()
    f = open("pubmed/data/Pubmed-Diabetes.DIRECTED.cites.tab", "r")
    fc = open("pubmed/data/Pubmed-Diabetes.NODE.paper.tab", "r")
    i = -2
    for line in fc:
        if i < 0:
            i += 1
            continue
        a = line.split("\t")[0]
        map[a] = i
        i += 1
    linecnt = 0
    for line in f:
        linecnt += 1
        if linecnt <= 2:
            continue
        [a, b] = [map[index] for index in line.replace(
            "\n", "").replace("paper:", "").split("\t")[1:4:2]]
        if a not in adjmap:
            adjmap[a] = [b]
        else:
            adjmap[a].append(b)

        if b not in adjmap:
            adjmap[b] = [a]
        else:
            adjmap[b].append(a)
        x.append(a)
        x.append(b)
        y.append(b)
        y.append(a)
    return x, y, map, adjmap
