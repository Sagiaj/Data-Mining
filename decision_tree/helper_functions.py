import numpy as np

def randomMatrixGenerator(list_size = 2, range_num = 2):
    import random
    return [[random.randint(0, 1) for j in range(range_num)] for i in range(list_size)]

def calculateEntropy(data_set):
    attrs = data_set.getAttrs()
    attr_list = data_set.getAttrList()
    entropy = 0
    for x in attrs:
        x_len = len((data_set.getListByAttr(x)))
        p_x = float(x_len/len(attr_list))
        if p_x > 0:
            entropy += -p_x*np.log2(1/p_x)
    return entropy

def calculateInfoGain(attr, data_set):
    original_entropy = calculateEntropy(data_set)
    filtered_by_attr = data_set.getListByAttr(attr)
    val_freq = {}
    subset_entropy = 0.0
    attr_list = data_set.getAttrList()
    for attribute in attr_list:
        for instance in attr_list[attribute]:
            if attribute in instance.getAttributeList().keys() and instance.getAttributeList()[attribute] == 1:
                if attribute in val_freq:
                    val_freq[attribute] += 1.0
                else:
                    val_freq[attribute] = 1.0

    for val in val_freq.keys():
        p_t = val_freq[val] / sum(val_freq.values())
        data_subset = [subset for subset in data_set if subset[attr] == val]
        subset_entropy += p_t * calculateEntropy(data_subset)

    return (original_entropy - subset_entropy)