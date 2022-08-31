# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root:TreeNode) -> str:
        q = collections.deque([root])
        result = []
        # TreeNode -> list
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result) # list -> str

    def deserialize(self, data:str)->TreeNode:
        if data == '#':
            return None
        # str -> list
        nodes = data.split()
        
        root = TreeNode(int(nodes[0]))
        q = collections.deque([root])
        index = 1
        while q:
            node = q.popleft()
            if nodes[index] != '#':
                node.left = TreeNode(int(nodes[index]))
                q.append(node.left)
            index += 1
            
            if nodes[index]is not '#':
                node.right = TreeNode(int(nodes[index]))
                q.append(node.right)
            index += 1
        return root
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))