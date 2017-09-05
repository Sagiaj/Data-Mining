class Instance(object):
    instance_atts = []

    def __init__(self, attrs, att_list):
        self.instance_atts = dict(zip(attrs, att_list))

    def getAttributeList(self):
        return self.instance_atts


class DataSet(object):
    def __init__(self, raw_list, attrs):
        instance_list = self.createInstanceList(raw_list, attrs)
        self.instance_list = instance_list
        self.attrs = attrs
        self.attr_list = self.buildValidAttrList(instance_list, attrs)

    def createInstanceList(self, raw_list, attrs):
        instance_list = []
        for attr_combination in raw_list:
            instance_list.append(Instance(attrs, attr_combination))

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
        filtered_list = []
        attr_list = self.getAttrList()
        for property in attr_list:
            instance_list = attr_list[property]
            for instance in instance_list:
                if instance.getAttributeList()[attr] == 1:
                    filtered_list.append(instance)

        return filtered_list