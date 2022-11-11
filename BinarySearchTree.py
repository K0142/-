# Binary search tree 클래스 선언
class BinarySearchTree:
	
	# Node 클래스 선언
	class Node:
		def __init__(self, data):
			self.data = data
			self.left = self.right = None

	def __init__(self):
		self.root = None

	# 이진 트리에 데이터를 삽입하는 함수 => 재귀 이용
	def insert(self, data):
		self.root = self._insert_data(self.root, data)
		return self.root is not None

	def _insert_data(self, node, data):
		if node is None:
			node = self.Node(data)
		else:
			if data <= node.data:
				node.left = self._insert_data(node.left, data)
			else:
				node.right = self._insert_data(node.right, data)

		return node
	
	# 이진 트리에 데이터를 탐색하는 함수 => 재귀 이용
	def search(self, key):
		return self._search_data(self.root, key)

	def _search_data(self, root, key):
		if root is None or root.data == key:
			return root is not None
		elif key < root.data:
			return self._search_data(root.left, key)
		else:
			return self._search_data(root.right, key)

	# 이진 트리에 데이터를 삭제하는 함수 => 재귀 이용
	def delete(self, key):
		self.root, deleted = self._delete_data(self.root, key)
		return deleted

	def _delete_data(self, node, key):
		if node is None:
			return node, False

		deleted = False
		if key == node.data:
			deleted = True
			if node.left and node.right:   # 현재 노드에 왼쪽 서브 트리와 오른쪽 서브 트리가 전부 있을 경우
				parent, child = node, node.right
				while child.left is not None:
					parent, child = child, child.left
				child.left = node.left
				if parent != node:
					parent.left = child.right
					child.right = node.right
				node = child
			elif node.left or node.right:   # 현재 노드에 왼쪽 서브 트리와 오른쪽 서브 트리 중 하나만 있을 경우
				node = node.left or node.right
			else: 
				node = None
		elif key < node.data:
			node.left, deleted = self._delete_data(node.left, key)
		else: 
			node.right, deleted = self._delete_data(node.right, key)
	
		return node, deleted

	#깊이 우선 탐색을 이용한 전위 순회
	def dfs_preorder_traversal(self):
		def _dfs_preorder_traversal(root):
			if root is None:
				pass
			else:
				print(root.data, end = ' ')
				_dfs_preorder_traversal(root.left)
				_dfs_preorder_traversal(root.right)
		_dfs_preorder_traversal(self.root)
	
	# 깊이 우선 탐색을 이용한 중위 순회
	def dfs_inorder_traversal(self):
		def _dfs_inorder_traversal(root):
			if root is None:
				pass
			else:
				_dfs_inorder_traversal(root.left)
				print(root.data, end = ' ')
				_dfs_inorder_traversal(root.right)
		_dfs_inorder_traversal(self.root)
	
	# 깊이 우선 탐색을 이용한 후위 순회
	def dfs_postorder_traversal(self):
		def _dfs_postorder_traversal(root):
			if root is None:
				pass
			else:
				_dfs_postorder_traversal(root.left)
				_dfs_postorder_traversal(root.right)
				print(root.data, end = ' ')
		_dfs_postorder_traversal(self.root)

if __name__ == "__main__":
	array = [40, 4, 34, 35, 14, 55, 48, 13, 15, 49, 47]
	num_tree = BinarySearchTree()
	
	for x in array:
		num_tree.insert(x)
	
	# traversal data
	print("<전위 순회>")
	num_tree.dfs_preorder_traversal()
	print("\n<중위 순회>")
	num_tree.dfs_inorder_traversal()
	print("\n<후위 순회>")
	num_tree.dfs_postorder_traversal()
	print("\n")

	# search data
	print("search data")
	print(num_tree.search(14))
	print(num_tree.search(50))
	print()

	# delete data
	print("delete data")
	print(num_tree.delete(48))
	print(num_tree.delete(4))
	print()

