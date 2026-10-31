def DFS(tree,root):
    visited = set()
    stack = [root]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            print(vertex)

            for i in tree[vertex]:
                if i not in visited:
                    stack.append(i)

if __name__ == '__main__':
    tree = {1:[2,3],2:[4,5],3:[6],4:[],5:[],6:[]}
    DFS(tree,1)