import inspect

import example


class C(example.B):
    pass


class D(C, example.A):
    pass


def print_class_tree(tree, indent=-1):
    if isinstance(tree, list):
        for node in tree:
            print_class_tree(node, indent+1)
    else:  # tuple
        print(' ' * indent, tree[0].__name__)
    return


if __name__ == '__main__':
    print('A,B,C,D:')
    print_class_tree(inspect.getclasstree([example.A, example.B, C, D]))

    print('If we call getclasstree() with `unique=True`, \
            the output is different.')
    print_class_tree(inspect.getclasstree(
        [example.A, example.B, C, D], unique=True))
