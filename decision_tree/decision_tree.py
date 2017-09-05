import numpy as np
from sklearn.cluster import KMeans
import helper_functions as hf
import helper_classes as hc
import random
#column is attr (for example height is an attr)
#row is an instance(for example a person is an instance)



# calculate information gain recursively
# export the results to an external file in any format
# create a decision tree class to support the gain


predefined_props = ['height', 'age', 'weight', 'strength', 'speed']
instance_num = 1000

target_attr_list = [random.randint(0,1) for i in range(1, instance_num)]
random_list = hf.randomMatrixGenerator(instance_num, len(predefined_props))

# let the appended last column denote the target attribute availability
# for i in range(0, len(random_list) - 1):
#     random_list[i].append(target_attr_list[i])
data_set = hc.DataSet(random_list, predefined_props, target_attr_list)

print(hf.calculateInfoGain('height', data_set))
