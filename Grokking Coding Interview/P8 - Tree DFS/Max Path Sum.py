import math


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_maximum_path_sum(root):

  if root is None:
    return -1

  maxSum = [0]
  heightSum(root, maxSum)

  return maxSum[0]

def heightSum(root, maxSum):

  if root is None:
    return 0

  else:

    leftSum = heightSum(root.left, maxSum)
    rightSum = heightSum(root.right, maxSum)

    if leftSum != 0 and rightSum != 0:
       currSum = leftSum + rightSum + root.val
       maxSum[0] = max(maxSum[0], currSum)

    retVal = (max(leftSum, rightSum) + root.val)
    return retVal










def main():
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)

  print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(3)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))

  root = TreeNode(-1)
  root.left = TreeNode(-3)
  print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))


main()
