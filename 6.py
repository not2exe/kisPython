subtree_r_r_r = {"APL": 0, "HAML": 1}
subtree_r_r = {"MASK": subtree_r_r_r, "CSON": 2}
subtree_r = {2014: 3, 1972: 4, 1994: subtree_r_r}
subtree_l_r_l = {1994: 6, 2014: 7, 1972: 8}
subtree_l_r = {1979: 5, 1988: subtree_l_r_l}
subtree_l_l = {"APL": 9, "HAML": 10}
subtree_l = {"MASK": subtree_l_r, "CSON": subtree_l_l}
root_tree = {"LSL": subtree_r, "EAGLE": subtree_l}


def main(array, tree=None):
    if tree is None:
        tree = root_tree
    if type(tree) is int:
        return tree
    keys = tree.keys()
    key = None
    for i in array:
        if i in keys:
            key = i
            break
    return main(array, tree[key])


print(main([1972, 'APL', 'CSON', 'LSL', 1979]))
print(main([1994, 'APL', 'CSON', 'LSL', 1979]))
print(main([1994, 'HAML', 'CSON', 'EAGLE', 1988]))
print(main([2014, 'HAML', 'MASK', 'LSL', 1988]))
print(main([2014, 'HAML', 'MASK', 'EAGLE', 1979]))
