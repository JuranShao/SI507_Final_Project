import json
from prettytable import PrettyTable

class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class BST:
    def __init__(self, node_list, key_loc):
        self.root = Node(node_list[0])
        for data in node_list[1:]:
            self.insert(data, key_loc)

    def search(self, node, parent, data_index, key_loc):
        if node is None:
            return False, node, parent
        if node.data[key_loc] == data_index:
            return True, node, parent
        if node.data[key_loc] > data_index:
            return self.search(node.lchild, node, data_index, key_loc)
        else:
            return self.search(node.rchild, node, data_index, key_loc)

    def insert(self, data_all, key_loc):
        flag, n, p = self.search(self.root, self.root, data_all[key_loc], key_loc)
        if not flag:
            new_node = Node(data_all)
            if data_all[key_loc] > p.data[key_loc]:
                p.rchild = new_node
            else:
                p.lchild = new_node

    def delete(self, root, data, key_loc):
        flag, n, p = self.search(root, root, data, key_loc)
        if flag is False:
            print("invalid delete")
        else:
            if n.lchild is None:
                if n == p.lchild:
                    p.lchild = n.rchild
                else:
                    p.rchild = n.rchild
                del p
            elif n.rchild is None:
                if n == p.lchild:
                    p.lchild = n.lchild
                else:
                    p.rchild = n.lchild
                del p
            else:  # left and right tree are not empty
                pre = n.rchild
                if pre.lchild is None:
                    n.data = pre.data
                    n.rchild = pre.rchild
                    del pre
                else:
                    next = pre.lchild
                    while next.lchild is not None:
                        pre = next
                        next = next.lchild
                    n.data = next.data
                    pre.lchild = next.rchild
                    del p

    def preOrderTraverse(self, node):
        if node is not None:
            print(node.data,)
            self.preOrderTraverse(node.lchild)
            self.preOrderTraverse(node.rchild)

    def inOrderTraverse(self, node):
        if node is not None:
            self.inOrderTraverse(node.lchild)
            print(node.data)
            self.inOrderTraverse(node.rchild)

    def postOrderTraverse(self, node):
        if node is not None:
            self.postOrderTraverse(node.lchild)
            self.postOrderTraverse(node.rchild)
            print(node.data,)

    def trans_Dict(self):
        dic = self.__Dict(self.root)
        # dic={self.root.data:dic}
        return dic

    def __Dict(self, Node):
        dic = {}
        dic['value'] = Node.data
        if Node.lchild is not None and Node.rchild is not None:
            dic['left'] = self.__Dict(Node.lchild)
            dic['right'] = self.__Dict(Node.rchild)
        elif Node.lchild is not None and Node.rchild is None:
            dic['left'] = self.__Dict(Node.lchild)
        elif Node.lchild is None and Node.rchild is not None:
            dic['right'] = self.__Dict(Node.rchild)
        else:
            dic = {}
            dic['value'] = Node.data
        return dic


def select_counties_of_state(state):
    list_back = []
    with open('list_counties_cases_now.json') as file:
        list_counties = json.load(file)
    for item in list_counties:
        if item['state'] == state:
            list_back.append(item)
    return list_back


if __name__ == '__main__':
    with open('list_states_cases_now.json') as file:
        list_states = json.load(file)
    bst = BST(list_states, 'state')
    dict_ = bst.trans_Dict()
    with open('Tree_state.json', 'w') as outfile:
        json.dump(dict_, outfile, indent=4)

    with open('list_counties_cases_now.json') as file:
        list_counties = json.load(file)
    bst = BST(list_counties, 'county')
    dict_c = bst.trans_Dict()
    with open('Tree_county.json', 'w') as outfile:
        json.dump(dict_c, outfile, indent=4)
