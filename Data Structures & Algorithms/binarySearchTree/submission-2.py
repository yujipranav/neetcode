class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if self.root == None:
            self.root = newNode
            return

        curr = self.root
        while True:
            if key < curr.key:
                if curr.left == None:
                    curr.left = newNode
                    return
                curr = curr.left
            elif key > curr.key:
                if curr.right == None:
                    curr.right = newNode
                    return 
                curr = curr.right
            else:
                curr.val = val
                return


    def get(self, key: int) -> int:
        curr = self.root
        while curr != None:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return -1

    def getMin(self) -> int:
        curr = self.root
        while curr and curr.left:
            curr = curr.left

        return curr.val if curr else -1

    def findMin(self, node: TreeNode) -> TreeNode:
        while node and node.left:
             node = node.left

        return node

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1


    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, current: TreeNode, key: int) -> TreeNode:
        if current == None:
            return None
        
        if key > current.key:
            current.right = self.removeHelper(current.right, key)
        elif key < current.key:
            current.left = self.removeHelper(current.left, key)
        else:
            if current.left == None:
                return current.right
            elif current.right == None:
                return current.left
            else:
                minNode = self.findMin(current.right)
                current.key = minNode.key
                current.val = minNode.val
                current.right = self.removeHelper(current.right, minNode.key)

        return current

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result

    def inorderTraversal(self, root: TreeNode, result: List[int]) -> None:
        if root != None:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)

