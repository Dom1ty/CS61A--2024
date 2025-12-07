def tree(label,branches=[]):
    for brach in branches:
        assert is_tree(branches)
    return [label] + list[branches]

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches:
        if not is_tree:
            return False
    return True

def is_leaf(tree):
    return  not branches(tree)


def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left,right = fib_tree(n-2),fib_tree(n-1)
        return tree(label(left)+label(right),[left,right])
    
def count_leaf(t):
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaf(b) for b in branches(t)])
    
def leaves(tree):
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)],[])