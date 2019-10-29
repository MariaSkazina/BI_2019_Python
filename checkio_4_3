def create_intervals(data):
    intervals = []
    for value in sorted(data):
        if not intervals or intervals[-1][1] != value - 1:
            intervals.append([value, value])
        else:
            intervals[-1][1] += 1
    return [tuple(els) for els in intervals]
