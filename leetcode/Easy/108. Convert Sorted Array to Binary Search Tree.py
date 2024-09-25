# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # Base case: If the list is empty, return None
        if not nums:
            return None

        # Find the middle index of the list
        mid = len(nums) // 2

        # The middle element becomes the root of the BST
        root = TreeNode(nums[mid])

        # Recursively construct the left and right subtrees
        root.left = self.sortedArrayToBST(nums[:mid])  # Left subtree from the left half
        root.right = self.sortedArrayToBST(nums[mid + 1:])  # Right subtree from the right half

        return root