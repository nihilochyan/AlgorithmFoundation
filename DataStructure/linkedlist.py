class Node:  #  http://python.jobbole.com/83953/

    __slots__ = ['_item', '_next']    #限定Node实例的属性

    def __init__(self, item):
        self._item = item
        self._next = None     #Node的指针部分默认指向None

    def getItem(self):
        return self._item

    def getNext(self):
        return self._next

    def setItem(self, newitem):
        self._item = newitem

    def setNext(self, newnext):
        self._next = newnext


class SingleLinkedList:
    def __init__(self):
        self._head=None    #初始化链表为空表
        self._size=0

    def isEmpty(self):
        return self._head == None

    def add(self, item):
        temp = Node(item)    #add在链表前端添加元素
        temp.setNext(self._head)
        self._head = temp
        self._size += 1

    def append(self, item):
        temp = Node(item)
        if self.isEmpty():
            self._head = temp  # 若为空表，将添加的元素设为第一个元素
        else:
            current = self._head
            while current.getNext() != None:
                current = current.getNext()  # 遍历链表
            current.setNext(temp)  # 此时current为链表最后的元素
        self._size += 1

    def search(self, item):
        current = self._head   #search检索元素是否在链表中
        founditem = False
        while current != None and not founditem:
            if current.getItem() == item:
                founditem = True
            else:
                current = current.getNext()
        return founditem

    def index(self, item):
        current = self._head   #index索引元素在链表中的位置
        count = 0
        found = None
        while current != None and not found:
            count += 1
            if current.getItem() == item:
                found = True
            else:
                current = current.getNext()
        if found:
            return count
        else:
            raise ValueError('%s is not in linkedlist' % item)

    def remove(self, item):
        current = self._head
        pre = None
        while current != None:
            if current.getItem() == item:
                if not pre:
                    self._head = current.getNext()
                else:
                    pre.setNext(current.getNext())
                break
            else:
                pre = current
                current = current.getNext()
        self._size -= 1

    def insert(self, pos, item):
        if pos == self._size:
            self.append(item)
        elif pos == 0:
            self.add(item)
        else:
            temp = Node(item)
            current = self._head
            prefix = None
            while pos != 0:
                prefix = current
                current = current.getNext()
                pos -= 1
            prefix.setNext(temp)
            temp.setNext(current)
        self._size += 1

    def list(self):
        current = self._head
        print(current.getItem(), ',', end='')
        while current.getNext() != None:
            current = current.getNext()  # 遍历链表
            print(current.getItem(), ',', end='')
        print()

if __name__ == '__main__':
    singlelinkedlist = SingleLinkedList()
    print('list size is 0: ', singlelinkedlist.isEmpty())
    singlelinkedlist.add(5)
    singlelinkedlist.add(7)
    singlelinkedlist.add(8)
    print('list size is : ', singlelinkedlist._size)
    singlelinkedlist.append(10)
    print('list size is : ', singlelinkedlist._size)
    singlelinkedlist.list()
    singlelinkedlist.remove(10)
    singlelinkedlist.list()
    singlelinkedlist.insert(2, 111)
    singlelinkedlist.list()
    print('list size is : ', singlelinkedlist._size)
    print('Index of 7: ', singlelinkedlist.index(7))
    print('search 111:', singlelinkedlist.search(111))






