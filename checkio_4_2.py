def group_equal(els):
    from itertools import groupby
    from operator import itemgetter
    return list(map(list,map(itemgetter(1),groupby(els))))
