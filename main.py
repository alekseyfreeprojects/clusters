from math import dist

# Определяет который кластер, номер кластера
def which_cluster1(point):
    x, y = point
    if y - 5 < 0:
        # Принадлежит 1-му кластеру
        return 0
    elif x - 5 < 0:
        # Принадлежит 2-му кластеру
        return 1
    # Принадлежит 3-му кластеру
    return 2

# Определяет который кластер, номер кластера
def which_cluster2(point):
    x, y = point
    if x - 10 > 0:
        if y - 10 < 0:
            # Принадлежит 1-му кластеру
            return 0
        elif (y - 10) / (x - 10) < 1:
            # Принадлежит 2-му кластеру
            return 1
        # Принадлежит 3-му кластеру
        return 2
    else:
        if (y - 10) / (x - 10) < 1:
            # Принадлежит 4-му кластеру
            return 3
        # Принадлежит 5-му кластеру
        return 4

# Получает центр кластера
def get_centroids(clusters):
    centroids = []
    # Цикл по кластерам
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
    # Возвращает центр
    return int(px), int(py)

# Кластеры для 1-й задачи
clusters = [[], [], []]
for line in open('27a.txt'):
    # Точка из файла переводится в массив
    p = [float(d) for d in line.replace(',', '.').split()]
    # Определяет номер кластера куда относится точка-звезда
    cluster_num = which_cluster1(p)
    # Добавляет точку-звезду к кластеру
    clusters[cluster_num].append(p)
print(*get_centroids(clusters))

# Кластеры для 2-й задачи
clusters = [[], [], [], [], []]
for line in open('27b.txt'):
    # Точка из файла переводится в массив
    p = [float(d) for d in line.replace(',', '.').split()]
    # Определяет номер кластера куда относится точка-звезда
    cluster_num = which_cluster2(p)
    # Добавляет точку-звезду к кластеру
    clusters[cluster_num].append(p)
print(*get_centroids(clusters))
