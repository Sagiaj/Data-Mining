import numpy as np
import generate as g
from sklearn.cluster import KMeans

class Coordinate:
    def __init__(self, vector):
        self.vector = vector

    def getData(self):
        return self.vector

    def calcDistance(self, p):
        return np.sqrt(sum([(val1 - val2)**2 for val1,val2 in zip(self.vector, p.vector)]))

class CoordinateRepo:
    def __init__(self, coor_list):
        self.setCoordinates(coor_list)
    
    def randomPointGenerator(self, range_num = 2):
        import random
        return [random.randint(0,10) for i in range(range_num)]
    
    def setCoordinates(self, p_list):
        self.point_list = p_list
        coor_list = []
        for point in p_list:
            coor_list.append(Coordinate([val for val in point]))
        self.coor_list = coor_list
        self.setDistMatrix()

    def getCoordinates(self):
        return self.coor_list

    def addCoordinate(self, point):
        self.coor_list.append(Coordinate([val for val in point]))
    
    def getPoints(self):
        return self.point_list
        
    def setDistMatrix(self):
        coor_list_len = len(self.coor_list)
        self.distance_matrix = [[0 for x in range(coor_list_len+1)] for y in range(coor_list_len+1)]
        for i in range(coor_list_len):
            for j in range(i+1, coor_list_len):
                self.distance_matrix[i][j] = self.coor_list[i].calcDistance(self.coor_list[j])
        
    def getDistMatrix(self):
        return self.distance_matrix

class Cluster:
    def __init__(self, dataset):
        self.point_list = list()
        self.setDataset(dataset)
    
    def setDataset(self, data_list):
        self.point_list = data_list
        cRepo = CoordinateRepo(data_list)
        self.coor_list = cRepo

    def getDataSet(self):
        return self.coor_list.getCoordinates()
    
    def addPoint(self, point):
        self.coor_list.addCoordinate([point])


def buildValidClusters(clusters, point_list, labels):
    flattened_clusters = []
    for i in range(len(point_list)):
        if len(clusters[labels[i]]) == 0:
            clusters[labels[i]].append(Cluster([[point_list[i]]]))
        else:
            for c in clusters[labels[i]]:
                c.addPoint(point_list[i])

    for cluster in clusters:
        for c in cluster:
            flattened_clusters.append(c)

    return flattened_clusters


def run(point_list = [[]], num_clusters = 2):
    kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(point_list)
    labels = kmeans.labels_
    clusters = [[] for j in range(num_clusters)]

    return buildValidClusters(clusters, point_list, labels)


# An exemplary
# clusters = run(g.gen(2, 5), 3)
#
# for cluster in clusters:
#     print("data set for cluster: ", cluster)
#     for coordinate in cluster.getDataSet():
#         for point in coordinate.getData():
#             print(point)
