import numpy as np
from sklearn.cluster import KMeans
import helper_functions as hf
import helper_classes as hc
#column is attr (for example height is an attr)
#row is an instance(for example a person is an instance)



predefined_props = ['height', 'age', 'weight', 'strength', 'speed']
instance_num = 1000

random_list = hf.randomMatrixGenerator(instance_num, len(predefined_props))

data_set = hc.DataSet(random_list, predefined_props)

print(hf.calculateInfoGain('height', data_set))
