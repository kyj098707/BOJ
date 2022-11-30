class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def array_to_bst(nums):
    if not nums:
        return None  
    
    # 중앙 인덱스
    mid_idx = len(nums)//2
    
    # 중앙값으로 노드 생성
    node = TreeNode(nums[mid_idx])
    
    # left subtree 구성
    # values < nums[mid_idx]
    node.left = array_to_bst(nums[:mid_idx])
    
    # right subtree 구성
    # values > nums[mid_idx]
    node.right = array_to_bst(nums[mid_idx+1:])
    
    return node

def inorder(node): 
    if not node: 
        return      
    
    inorder(node.left) 
    print(node.val)
    inorder(node.right)   

    
nums = [1,2,3,4,5,6,7]
print("Original array:", nums)

root = array_to_bst(nums)
print("A height balanced BST:")
print(inorder(root))