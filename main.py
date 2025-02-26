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
        #Находит минимальный диаметр
        dmin = 10 ** 10000
        # Цикл по кластерам
        for p in cl:
            # Сумма всех диаметров одного кластера
            d = sum(dist(p, pt) for pt in cl)
            if d < dmin:
                # Находит минимальный диаметр. Но он нужен только для определения центра
                dmin = d
                # Фиксирует звезду-точку минимального даметра
                c = p
        # Центр минимального даметра добавляет
        centroids.append(c)
    # Находит центр с учетом центров минимального диаметра. Это результат
    px = 100_000 * sum(p[0] for p in centroids) / len(centroids)  # Суммирует центры и делит на количество точек
    py = 100_000 * sum(p[1] for p in centroids) / len(centroids)  # Суммирует центры и делит на количество точек
    # Возвращает центр. Это результат
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
