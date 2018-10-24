def _recursion_merge_sort2(l1, l2, tmp):
    if len(l1) == 0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
        return _recursion_merge_sort2(l1, l2, tmp), tmp


def recursion_merge_sort2(l1, l2):
    return _recursion_merge_sort2(l1, l2, [])


def loop_merge_sort(l1, l2):
    tmp = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
    tmp.extend(l1)
    tmp.extend(l2)
    return tmp


if __name__ == '__main__':
    l1 = [1, 2, 3]
    l2 = [2, 3, 5]
    a, b = recursion_merge_sort2(l1, l2)  # 尾递归方法
    print(b)
    c = loop_merge_sort(l1, l2)
    print(c)




