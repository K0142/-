# Doubly Linked List 클래스 선언
class DoublyLinkedList:

	# Node 클래스 선언
	class Node:
		def __init__ (self, data, next = None, prev = None):
			self.data = data
			self.next = next
			self.prev = prev

	def __init__(self):
		self.head = None
		self.tail = None

	def print_node_before(self):
		if self.head == None:
			print("저장된 데이터가 없습니다.")
			return
		else:
			print("<현재 리스트 구조: head>")
			link = self.head
			while link:
				print(link.data, '<->', end = ' ')
				link = link.next
			print("\n")
	def print_node_after(self):
		if self.tail == None:
			print("저장된 데이터가 없습니다.")
			return
		else:
			print("<현재 구조 리스트: tail>")
			link = self.tail
			while link:
				print(link.data, '<->', end = ' ')
				link = link.prev
			print("\n")

	def insert_node_before(self, data):
		if self.head == None:
			self.head = self.Node(data)
			self.tail = self.head  # 같은 노드를 가리킨다
		else:
			# head가 가리키는 기존 노드의 prev를 새 노드로 지정, 새로 생성한 노드의 next를 기존 노드로 지정
			self.head.prev = self.Node(data, next = self.head)
			# head를 새로 생성한 노드로 변경
			self.head = self.head.prev

	def insert_node_after(self, data):
		if self.head == None:
			self.tail = self.Node(data)
			self.head = self.tail  # 같은 노드를 가리킨다

		else:
			# tail이 가리키는 기존 노드의 next를 새 노드로 지정, 새로 생성한 노드의 prev를 기존 노드로 지정
			self.tail.next = self.Node(data, prev = self.tail)
			# tail을 새로 생성한 노드로 변경
			self.tail = self.tail.next

	def delete_node_before(self):
		if self.head == None:
			print("삭제할 노드가 없습니다.")
			return
		else:
			# 현재 head가 가리키는 노드의 next를 새로운 head로 지정
			self.head = self.head.next
			self.head.prev = None

	def delete_node_after(self):
		if self.tail == None:
			print("삭제할 노드가 없습니다.")
			return
		else:
			# 현재 tail이 가리키는 노드의 prev를 새로운 tail로 지정
			self.tail = self.tail.prev
			self.tail.next = None

if __name__ == "__main__":
	num_list = DoublyLinkedList()
	num_list.insert_node_before(1)
	num_list.insert_node_before(2)
	num_list.insert_node_before(3)
	num_list.insert_node_after('A')
	num_list.insert_node_after('B')
	num_list.insert_node_after('C')
	
	num_list.print_node_before()
	num_list.print_node_after()
	
	num_list.delete_node_before()
	num_list.print_node_before()
	num_list.delete_node_after()
	num_list.print_node_after()
