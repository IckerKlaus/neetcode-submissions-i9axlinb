class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        self.root = self.insertBST(self.root, key, val)
    
    def insertBST(self, root, key, val):
        if not root:
            return TreeNode(key, val)
        
        if key < root.key:
            root.left = self.insertBST(root.left, key, val)
        elif key > root.key:
            root.right = self.insertBST(root.right, key, val)
        else:
            root.val = val
        return root

    def get(self, key: int) -> int:
        node = self.searchBST(self.root, key)
        return node.val if node else -1
    
    def searchBST(self, root, key):
        if not root:
            return None
        
        if key < root.key:
            return self.searchBST(root.left, key)
        elif key > root.key:
            return self.searchBST(root.right, key)
        else:
            return root

    def getMin(self) -> int:
        node = self.findMin(self.root)
        return node.val if node else -1

    def findMin(self, root):
        while root and root.left:
            root = root.left
        return root

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1

    def remove(self, key: int) -> None:
        self.root = self.removeBST(self.root, key)

    def removeBST(self, root, key):
        if not root:
            return
        
        if key < root.key:
            root.left = self.removeBST(root.left, key)
        elif key > root.key:
            root.right = self.removeBST(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.findMin(root.right)
                root.key = minNode.key
                root.val = minNode.val
                root.right = self.removeBST(root.right, minNode.key)
        return root

    def getInorderKeys(self) -> List[int]:
        values = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            values.append(root.key)
            inorder(root.right)
        
        inorder(self.root)
        return values
        


