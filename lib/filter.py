import re
from collections import OrderedDict


class Filter:
    """
    Could be used to register filter chain
    and parse data line through them.
    """

    def __init__(self):
        self.table = {"head": OrderedDict(), "data": []}
        self.head_nb = 0
        self.filter_nb = 0
        self.chain = None
        self.curr_row = None

        # row deliminator validate
        self.start = False
        self.end = False

    def head_set(self, header: dict):
        for k, v in header.items():
            self.table["head"][k] = v
        self.head_nb = len(self.table["head"])

    def table_get(self):
        ret = []
        ret.append(list(self.table["head"].keys()))
        for dat in self.table["data"]:
            ret.append(dat.copy())
        return ret

    def filter_set(self, filters: list):
        """
        Set chain of pattern text to filter.
        """
        self.chain = filters
        self.filter_nb = len(filters)

    def delim_set(self, start: bool = None, end: bool = None):
        if start is not None:
            self.start = start
        if end is not None:
            self.end = end

    def __update(self, info: dict):
        if self.curr_row is None:
            return
        for idx, (name, type) in enumerate(self.table["head"].items()):
            if name in info:
                self.curr_row[idx] = type(info[name])

    def parse(self, data: str):
        for idx, filter in enumerate(self.chain):
            res = re.match(filter, data)

            # start of row object
            if self.curr_row is None:
                if not self.start or (self.start and idx == 0 and res is not None):
                    self.curr_row = [None for i in range(self.head_nb)]
                    self.table["data"].append(self.curr_row)
                else:
                    raise Exception("No row available to receive information.")

            info = res.groupdict() if res is not None else {}
            self.__update(info)

            # end of row object
            if (
                self.curr_row is not None
                and self.end
                and idx == (self.filter_nb - 1)
                and res is not None
            ):
                self.curr_row = None
