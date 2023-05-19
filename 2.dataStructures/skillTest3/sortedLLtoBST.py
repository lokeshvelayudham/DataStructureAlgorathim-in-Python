
import sys
sys.setrecursionlimit(10**7)


#   List Node Class
class Node:
	def __init__(self, data):		
		self.data = data
		self.next = None


#   Binary tree node class for reference
class TreeNode:
	def __init__(self, val):
		self.data = val
		self.left = None
		self.right = None


def findMiddleElement(head):
	# The pointer used to disconnect the left half from the mid node.
	prevPtr = None
	
	slowPtr = head
	fastPtr = head

	while fastPtr != None and fastPtr.next != None:
		prevPtr = slowPtr
		slowPtr = slowPtr.next
		fastPtr = fastPtr.next.next

	# Handling the case when slowPtr was equal to head.
	if prevPtr != None:
		prevPtr.next = None

	return slowPtr


def sortedListToBST(head):

	if head == None:
		return None

	mid = findMiddleElement(head)

	newNode = TreeNode(mid.data)

	# When there is only one element in the Linked List 
	if head == mid:
		return newNode

	# Recursively form balanced BST for left and right subtree
	newNode.left = sortedListToBST(head)
	newNode.right = sortedListToBST(mid.next)

	return newNode


































ind = []
data1 = []

#   taking input via fast input
def takeInput():

	arr = list(map(int, sys.stdin.readline().strip().split(" ")))

	head = None
	if(arr[0] != -1):

		head = Node(arr[0])
		data1.append(arr[0])
		last = head
		for data in arr[1:]:

			if(data == -1):
				break
			data1.append(data)
			last.next = Node(data)
			last = last.next

	return head

def print1(poi):
	if poi == None:
		return
	print1(poi.left)

	ind.append(poi.data)
	
	print1(poi.right)

def isValid(root, height):
	if root == None:
		height[0] = 0
		return 1

	lh, rh, l, r = 0, 0, 0, 0

	l = isValid(root.left, [lh])
	r = isValid(root.right, [rh]);
	height[0] = max(l, r) + 1 

	if abs(l-r) >= 2:
		return 0
	else:
		return l & r

#   main
t = int(input().strip())
for i in range(t):
	ind.clear()
	data1.clear()
	head = takeInput()
	root = sortedListToBST(head)
	poi = root
	print1(poi)
	if data1 != ind:
		print('INCORRECT')
		continue

	h = 0
	if isValid(root, [h]) == 0:
		print('INCORRECT')
		continue
	print('CORRECT')