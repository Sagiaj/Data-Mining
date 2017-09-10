import numpy as np
import helper_classes as hc

def randomMatrixGenerator(list_size = 2, range_num = 2):
    import random
    return [[random.randint(0, 1) for j in range(range_num)] for i in range(list_size)]

def calculateEntropy(data_set):
    attrs = data_set.getAttrs()
    set_len = len(data_set.getUnfilteredList())
    attr_list = data_set.getAttrList()
    entropy = 0
    for x in attrs:
        x_len = len((data_set.getTargetedByAttr(x)))
        p_x = float(x_len/set_len)
        n_x = float((set_len - x_len)/set_len)
        if p_x > 0 and n_x > 0:
            entropy += -p_x*np.log2(p_x) -n_x*np.log2(n_x)
    return entropy

def calculateInfoGain(attr, data_set):
    original_entropy = calculateEntropy(data_set)
    attrs = data_set.getAttrs()
    subset_entropy = 0.0

    for possibility in [0, 1]:  # all possibilities of 'attr' instead of range
        possibility_subset = data_set.getListByAttrVal(attr, value=possibility)
        p_t = len(possibility_subset) / len(data_set.getUnfilteredList())

        data_subset = [list(instance.getAttributeList().values()) for instance in possibility_subset if instance.getAttributeList()[attr] == possibility]
        subset_entropy += p_t * calculateEntropy(
            hc.DataSet(data_subset, attrs, data_set.getTargetedListByAttr(attr, value=possibility))
        )

    return (original_entropy - subset_entropy)


def recurseDecisionTree(data_set):
    recurseDecisionTree(hc.DataSet())