def DLS(tree, root, limit):
    visited = set()
    stack =[(root,0)]

    while stack:
        vertex, depth = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            print(vertex)

            if depth < limit:
                for i in tree[vertex]:
                    if i not in visited:
                        stack.append((i, depth + 1))
if __name__ == '__main__':
    tree = {1:[2,3],2:[4,5],3:[6],4:[],5:[],6:[]}

    DLS(tree, 1, 1)