class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
        # 같은 값은 무시 (중복 방지)
    
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()
    
    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()
    
    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)
    
    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True
    
    def find_min(self):
        """가장 작은 값을 가진 노드 찾기 (왼쪽 끝)"""
        current = self
        while current.left:
            current = current.left
        return current
    
    def delete(self, value, parent=None):
        """노드 삭제 - 부모 참조를 포함한 재귀 방식"""
        if value < self.value:
            if self.left:
                return self.left.delete(value, self)
            else:
                return False
        elif value > self.value:
            if self.right:
                return self.right.delete(value, self)
            else:
                return False
        else:
            # 값을 찾음 - 삭제 시작
            # Case 1: 자식이 없는 경우 (leaf node)
            if self.left is None and self.right is None:
                if parent:
                    if parent.left == self:
                        parent.left = None
                    else:
                        parent.right = None
                return True
            
            # Case 2: 자식이 하나만 있는 경우
            elif self.left is None:
                if parent:
                    if parent.left == self:
                        parent.left = self.right
                    else:
                        parent.right = self.right
                else:
                    # 루트 노드인 경우
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                return True
            
            elif self.right is None:
                if parent:
                    if parent.left == self:
                        parent.left = self.left
                    else:
                        parent.right = self.left
                else:
                    # 루트 노드인 경우
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                return True
            
            # Case 3: 자식이 둘 다 있는 경우
            else:
                # 오른쪽 서브트리에서 가장 작은 값 찾기 (successor)
                successor = self.right.find_min()
                self.value = successor.value
                # successor 삭제
                self.right.delete(successor.value, self)
                return True


tree = TreeNode(6)
tree.insert(5)
tree.insert(2)
tree.insert(3)
tree.insert(8)
tree.insert(7)
tree.insert(9)

print("In-order traversal:")
tree.inorder_traversal()

print("\n3을 찾기:", tree.find(3))
print("10을 찾기:", tree.find(10))

print("\n3 삭제")
tree.delete(3)
print("삭제 후 In-order traversal:")
tree.inorder_traversal()

print("\n5 삭제 (한 자식만 있음)")
tree.delete(5)
print("삭제 후 In-order traversal:")
tree.inorder_traversal()

print("\n6 삭제 (두 자식 모두 있음)")
tree.delete(6)
print("삭제 후 In-order traversal:")
tree.inorder_traversal()