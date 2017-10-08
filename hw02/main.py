def bsearch(data, target):
    min = 0
    max = len(data) - 1

    if target in data:
        while True:
            center = int((min + max) / 2)
            if data[center] > target:
                max = center - 1
            elif data[center] < target:
                min = center + 1
            elif data[center] == target:
                return(center)
    else:
        return("None")
