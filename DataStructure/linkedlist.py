class Node:  #http://python.jobbole.com/83953/

    __slots__ = ['_item','_next']    #限定Node实例的属性

    def __init__(self, item):
        self._item=item
        self._next=None     #Node的指针部分默认指向None

    def getItem(self):
        return self._item

    def getNext(self):
        return self._next

    def setItem(self, newitem):
        self._item=newitem

    def setNext(self, newnext):
        self._next  = newnext


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

    def append(self, item):
        temp = Node(item)
        if self.isEmpty():
            self._head = temp  # 若为空表，将添加的元素设为第一个元素
        else:
            current = self._head
            while current.getNext() != None:
                current = current.getNext()  # 遍历链表
            current.setNext(temp)  # 此时current为链表最后的元素

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

    def insert(self, pos, item):
        if pos == self._size:
            self.append(item)
        else:
            temp = Node(item)
        count = 1
        pre = None
        current = self._head
        while count <= pos and current != None:
            if count == pos:
                pre = current.get_next()
                current.set_next(temp)
                temp.set_next(pre)
            else:
                current = current.get_next()
                count += 1
                self._size += 1









