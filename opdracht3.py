class BSTNode:
    def __init__(self,element,left,right):
        self.element = element
        self.left = left
        self.right = right

    def __repr__(self,nspaces=0):
        s1 = ''
        s2 = ''
        s3 = ''
        if self.right != None:
            s1 = self.right.__repr__(nspaces + 3)
        s2 = s2 + ' '*nspaces + str(self.element) + '\n'
        if self.left != None:
            s3 = self.left.__repr__(nspaces + 3)
        return s1 + s2 + s3

    def max(self):
        current = self
        while current.right:
            current = current.right
        return current.element
    
    def rsearch(self,e):
        if e == self.element:
            return True

        if e > self.element and self.right:
            return self.right.rsearch(e)
        if e < self.element and self.left:
            return self.left.rsearch(e)
        
        return False

    def rinsert(self,e):
        if e > self.element:
            if self.right:
                self.right.rinsert(e)
            else:
                self.right = BSTNode(e,None,None)
        if e < self.element:
            if self.left:
                self.left.rinsert(e)
            else:
                self.left = BSTNode(e,None,None)

    def insert(self,e):
        parent = self
        current = None
        found = False

        if parent.element < e:
            current = parent.right
        elif parent.element > e:
            current = parent.left
        else:
            found = True;

        while not found and current:
            parent = current
            if parent.element < e:
                current = parent.right
            elif parent.element > e:
                current = parent.left
            else:
                found = True

        if not found:
            if parent.element < e:
                parent.right = BSTNode(e,None,None)
            else:
                parent.left = BSTNode(e,None,None)
        return not found

    def insertArray(self,a, low=0, high=-1):
        if len(a) == 0:
            return
        if high == -1:
            high = len(a)-1
        mid = (low+high+1)//2
        self.insert(a[mid])
        if mid > low:
            self.insertArray(a,low,mid-1)
        if high > mid:
            self.insertArray(a,mid + 1,high)

    def search(self,e):
        current = self
        found = False
        while not found and current:
            if current.element < e:
                current = current.right
            elif current.element > e:
                current = current.left
            else:
                found = True
        if found:
            return current
        else:
            return None

    def search2(self,e):
        if self.element == e:
            return self
        parent = self.getParent(e)
        if parent == None:
            return None
        if parent.element < e:
            return parent.right
        return parent.left

    def getParent(self,e):
        parent = self
        current = None
        found = False

        if parent.element < e:
            current = parent.right
        elif parent.element > e:
            current = parent.left;
        else:
            return None

        while not found and current:
            if current.element == e:
                found = True
            else:
                parent = current
                if current.element < e:
                    current = current.right
                else:
                    current = current.left
        if found:
            return parent
        else:
            return None
        
    def parentMinRightTree(self):
        parent = self.right
        current = parent.left
        while current.left:
            parent = current
            current = current.left
        return parent

    def delete(self,e):
        parent = self.getParent(e);

        if parent == None:
            return False
        if parent.element < e:
            current = parent.right
            if current.left == None:
                parent.right = parent.right.right
                return True
            else:
                if current.right == None:
                    parent.right = parent.right.left
                    return True
        else:
            current = parent.left
            if current.left == None:
                parent.left = parent.left.right
                return True
            else:
                if current.right == None:
                    parent.left = parent.left.left
                    return True
        if current.right.left == None:
            current.element = current.right.element
            current.right = current.right.right
            return True
        node = current.parentMinRightTree()
        current.element = node.left.element
        node.left = node.left.right
        return True
#----------------------------------------------------------------------------------------------------------------------------------------

class BST:
    def __init__(self,a=None):
        if a:
            mid = len(a)//2
            self.root = BSTNode(a[mid],None,None)
            self.root.insertArray(a[:mid])
            self.root.insertArray(a[mid+1:])
        else:
            self.root = None

    def __repr__(self):
        if self.root:
            return str(self.root)
        else:
            return 'null-tree'

    def rsearch(self, e):
        if self.root and e:
            return self.root.rsearch(e)
        return False

    def rinsert(self,e):
        if self.root:
            if e:
                self.root.rinsert(e)
        else:
            self.root = BSTNode(e,None,None)

    def search(self,e):
        if self.root and e:
            return self.root.search(e)
        else:
            return None


    def insert(self,e):
        if e:
            if self.root:
                return self.root.insert(e)
            else:
                self.root = BSTNode(e,None,None)
                return True
        else:
            return False

    def max(self):
        if self.root:
            return self.root.max()
        else:
            return None

    def delete(self,e):
        if self.root and e:
            if self.root.element == e:
                if self.root.left == None:
                    self.root = self.root.right
                elif self.root.right == None:
                    self.root = self.root.left
                elif self.root.right.left == None:
                    self.root.element = self.root.right.element
                    self.root.right = self.root.right.right
                else:
                    node = self.root.parentMinRightTree();
                    self.root.element = node.left.element
                    node.left = node.left.right
                return True
            else:
                return self.root.delete(e)
        else:
            return False

if __name__ == '__main__':
    b = BST([1,2,3])
    print(b)
    print('----------------')

    b = BST([1,2,3,4])
    print(b)
    print('----------------')
    b = BST([1,2,3,4,5,6,7,8,9,10])
    print(b)
    print('----------------')

    print(b.max())

    print(b.rsearch(11))

    #b = BST([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    #print(b)
    #node = b.search(3)
    #if node != None:
    #    print(node.element)
    #node = b.search(4)
    #if node != None:
    #    print(node.element)
    #node = b.search(8)
    #if node != None:
    #    print(node.element)
    #node = b.search(11)
    #if node != None:
    #    print(node.element)
    #node = b.search(16)
    #if node != None:
    #    print(node.element)
    #b.insert(17);
    #print(b)
    #print('----------------')
    #b.delete(14)
    #print(b)
    #print('----------------')

    #print(b.insert(10))

    #b = BST()
    #for i in range(1,11):
    #    b.insert(i)
    #print(b)
    #print('----------------')

    #b = BST(None)
    #print(b)
    #print('----------------')
    #b = BST([])
    #print(b)
    #print('----------------')
    #b = BST([0])
    #print(b)
    #print('----------------')

    b = BST()
    b.insert(3)
    b.insert(2)
    b.insert(10)
    b.insert(11)
    b.insert(9)
    b.insert(6)
    b.insert(7)
    b.insert(8)
    print(b)
    print('----------------')
    #b.delete(3)
    #print(b)
    #print('----------------')

    b = BST()
    b.rinsert(3)
    b.rinsert(2)
    b.rinsert(10)
    b.rinsert(11)
    b.rinsert(9)
    b.rinsert(6)
    b.rinsert(7)
    b.rinsert(8)
    print(b)
    print('----------------')
    #b.delete(3)
    #print(b)
    #print('----------------')

