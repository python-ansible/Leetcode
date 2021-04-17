# _*_ coding: utf-8 _*_
# 我们可以为二叉树 T 定义一个翻转操作，如下所示：选择任意节点，然后交换它的左子树和右子树。
# 只要经过一定次数的翻转操作后，能使 X 等于 Y，我们就称二叉树 X 翻转等价于二叉树 Y。
# 编写一个判断两个二叉树是否是翻转等价的函数。
# 这些树由根节点root1 和 root2给出。
# 输入：root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
# 输出：true
# 解释：我们翻转值为 1，3 以及 5 的三个节点。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/flip-equivalent-binary-trees
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1. 层序遍历
# 2. 递归操作
#      退出条件：
#         if not root1 and not root2: return True
#         if not root1 and root2：return False
#         if not root2 and root1: return False
#         if root1.val != root2.val: return False
#     子递归 and 返回值：
#         return flipEquiv(root1.left, root2.left) and flipEquiv(root1.right, root2.right)
#         or flipEquiv(root1.left, root2.right) and flipEquiv(root1.right, root2.left)

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2: return True
        if not root1 and root2: return False
        if not root2 and root1: return False
        if root1.val != root2.val: return False
        return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right) \
        or self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)