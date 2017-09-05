class Instance(object):
    instance_atts = []

    def __init__(self, attrs, att_list, target_attr):
        self.instance_atts = dict(zip(attrs, att_list))
        self.target_attr = target_attr

    def getAttributeList(self):
        return self.instance_atts

    def getTargetAttr(self):
        return self.target_attr


class DataSet(object):
    def __init__(self, raw_list, attrs, target_attr_list):
        instance_list = self.createInstanceList(raw_list, attrs, target_attr_list)
        self.instance_list = instance_list
        self.attrs = attrs
        self.attr_list = self.buildValidAttrList(instance_list, attrs)

    def createInstanceList(self, raw_list, attrs, target_attr_list):
        instance_list = []
        for i in range(0, len(raw_list) - 1):
            print(i, raw_list[i])
            instance_list.append(Instance(attrs, raw_list[i], target_attr_list[i]))

        return instance_list

    def buildValidAttrList(self, data_list, attrs):
        attr_list = {}
        for attr in attrs:
            attr_list.update({attr: []})
            for instance in data_list:
                attr_list[instance.getAttributeList()[attr]] = []
                if instance.getAttributeList()[attr] > 0:
                    attr_list[attr].append(instance)
        return attr_list

    def getAttrList(self):
        return self.attr_list

    def getAttrs(self):
        return self.attrs

    def getListByAttr(self, attr):
        attr_list = self.getAttrList()

        return [instance for instance in attr_list[attr]]

    def getTargetedByAttr(self, attr):
        filtered_list = []
        attr_list = self.getAttrList()
        for instance in attr_list[attr]:
            if instance.getTargetAttr() == 1:
                filtered_list.append(instance)

        return filtered_list

class DecisionTree(object):
    def __init__(self, data_set, target_attr):
        self.data_set = data_set
        self.target_attr = target_attr
