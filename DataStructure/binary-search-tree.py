#  http://blog.csdn.net/hjj414/article/details/37700843


class tree_node:

    def __init__(self, key=None, value=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.value = value


class binary_search_tree:

    def __init__(self):
        self.root = None

    def preorder(self):
        print('preoder: ')
        self.__preorder(self.root)
        print()

    def __preorder(self, root):
        if not root:
            return
        print(str(root.key)+':'+str(root.value))
        self.__preorder(root.left)
        self.__preorder(root.right)

    def inorder(self):
        print('inorder: ')
        self.__inorder(self.root)
        print()

    def __inorder(self, root):
        if not root:
            return
        self.__inorder(root.left)
        print(str(root.key)+':'+str(root.value))
        self.__inorder(root.right)

    def postorder(self):
        print('postorder: ')
        self.__postorder(self.root)
        print()

    def __postorder(self, root):
        if not root:
            return
        self.__postorder(root.left)
        self.__postorder(root.right)
        print(str(root.key)+':'+str(root.value))

    def insert(self, key, value):
        self.root = self.__insert(self.root, key, value)

    def __insert(self, root, key, value):
        if not root:
            root = tree_node(key, value)
        else:
            if key < root.key:
                root.left = self.__insert(root.left, key, value)
            elif key > root.key:
                root.right = self.__insert(root.right, key, value)
            else:
                print(key, 'already exists')
        return root

    def insert_non_recursion(self ,key, value):
        if not self.root:
            self.root = tree_node(key, value)
        else:
            cur = self.root
            while True:
                if key < cur.left:
                    if not cur.left:
                        cur.left = tree_node(key, value)
                        break
                    cur = cur.left
                elif key > cur.key:
                    if not cur.right:
                        cur.right = tree_node(key, value)
                        break
                    cur = cur.right
                else:
                    print(key, ':', 'already exists')

    def height(self):
        return self.__height(self.root)

    def __height(self, root):
        if not root:
            return -1
        left_height = self.__height(root.left)
        right_height = self.__height(root.right)
        return 1 + [left_height, right_height][left_height < right_height]
        #return 1+(left_height>right_height and [left_height] or [right_height])[0]

    def count(self):
        '''elements in tree'''
        return self.__count(self.root)

    def __count(self, root):
        if not root:
            return 0
        return 1+self.__count(root.left) + self.__count(root.right)

    def delete(self, key):
        self.root = self.__delete(self.root, key)

    ##
    ## 删除操作：
    ##   首先找到删除的节点，
    ##1. 如果左右子树都不为空，则找到右子树中最小的节点min，用min.key代替删除节点的key，然后再到右子
    ##   树中删除min节点,因为min没有左节点，所以删除它的话只需要用它的右节点代替它(如果有右节点)；
    ##2. 如果左子树或者右子树不为空，则直接代替掉
    ##3. 如果左右均空即叶子节点，直接删掉
    def __delete(self, root, key):
        if not root:
            print('not find key: ', key)
        elif key < root.key:
            root.left = self.__delete(root.left, key)
        elif key > root.key:
            root.right = self.__delete(root.right, key)
        elif root.left and root.right:
            right_min = self.__find_min(self.root.right)
            root.key = right_min.key
            root.value = right_min.value
            root.right = self.__delete(root.right, right_min.key)
        elif root.left:
            root = root.left
        elif root.right:
            root = root.right
        else:
            root = None  # destroy Object by pointing it to no pointer

        return root

    def find(self, key):
        node = self.__find(self.root, key)
        if not node:
            print('not found')
        return node

    def __find(self, root, key):
        if not root:
            return None
        if key < root.key:
            return self.__find(root.left, key)
        elif key > root.key:
            return self.__find(root.right, key)
        else:
            return root

    def find_min(self):
        return self.__find_min(self.root)

    def __find_min(self, root):
        if not root.left:
            return root
        return self.__find_min(root.left)

    def find_max(self):
        return self.__find_max(self.root)

    def __find_max(self, root):
        if not root.right:
            return root
        return self.__find_max(root.right)


def main():
    import random
    root = binary_search_tree()
    for i in random.sample([j for j in range(1, 100)], 5):
        root.insert(i, i*10)
    'insert: '
    root.insert(78, 780)
    root.insert(101, 1010)
    root.insert(14, 140)

    root.preorder()
    root.inorder()
    root.postorder()

    print('height: ', root.height())
    print('count: ', root.count())
    print('min: ', root.find_min().key)
    print('max: ', root.find_max().key)
    print('delete: ')
    root.delete(101)
    root.delete(12)
    root.preorder()
    root.inorder()
    root.postorder()
    root.find(78)
    print('height: ', root.height())
    print('count: ', root.count())
    print('min: ', root.find_min().key)
    print('max: ', root.find_max().key)

if __name__ == '__main__':
    main()








