from collections import OrderedDict


class Filter:
    """
    Could be used to register filter chain
    and parse data line through them.
    """

    def __init__(self):
        self.table = {"head": OrderedDict(), "data": []}

    def head_set(self, name, type):
        self.table["head"][name] = type

    def table_get(self):
        ret = []
        ret.append(list(self.table["head"].keys()))
        for dat in self.table["data"]:
            ret.append(dat.copy())
        return ret
