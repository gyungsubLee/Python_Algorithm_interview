​
# ✍️ 풀이1(재귀-파이썬 다운 방식)

```python
# Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None
```

<br/>



### input: TreeNode
<img src="./이미지/1.png" width="40%">

<br/>

### 재귀2
<img src="./이미지/2.png" width="40%">

<br/>

### 재귀1
<img src="./이미지/3.png" width="40%">