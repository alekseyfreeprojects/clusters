from math import dist


def which_cluster1(point):
    x, y = point
    if y - 5 < 0:
        return 0
    elif x - 5 < 0:
        return 1
    return 2


def which_cluster2(point):
    x, y = point
    if x - 10 > 0:
        if y - 10 < 0:
            return 0
        elif (y - 10) / (x - 10) < 1:
            return 1
        return 2
    else:
        if (y - 10) / (x - 10) < 1:
            return 3
        return 4


def get_centroids(clusters):
    centroids = []
    for cl in clusters:
        dmin = 10 ** 10000
        for p in cl:
            d = sum(dist(p, pt) for pt in cl)
            if d < dmin:
                dmin = d
                c = p
        centroids.append(c)
    px = 100_000 * sum(p[0] for p in centroids) / len(centroids)
    py = 100_000 * sum(p[1] for p in centroids) / len(centroids)
    return int(px), int(py)


clusters = [[], [], []]
for line in open('27a.txt'):
    p = [float(d) for d in line.replace(',', '.').split()]
    clusters[which_cluster1(p)].append(p)
print(*get_centroids(clusters))

clusters = [[], [], [], [], []]
for line in open('27b.txt'):
    p = [float(d) for d in line.replace(',', '.').split()]
    clusters[which_cluster2(p)].append(p)
print(*get_centroids(clusters))
