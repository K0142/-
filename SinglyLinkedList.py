# Singly linked list 클래스 선언
class SinglyLinkedList:
	
	# Node 클래스 선언
	class Node:
		def __init__ (self, data, next = None):
			self.data = data   # 저장된 데이터
			self.next = next   # 다음 노드를 가리키는 변수
	def __init__ (self):
		self.head = None
	
	def print_node(self):
		if self.head == None:
			print("저장된 데이터가 없습니다.")
			return
		else:
			print("<현재 리스트 구조>")
			link = self.head
			while link:       # link가 가리키는 노드가 없을 때까지 반복
				print(link.data, end = ' ')
				link = link.next
			print("\n")

	def insert_node(self, data):
		if self.head == None:   # 첫 번째 노드일 경우
			self.head = self.Node(data)
		else:
			# head에 새 노드 저장 / 기존 노드는 새로 생성할 노드의 next로 설정
			self.head = self.Node(data, self.head) 

	def delete_node(self):
		if self.head == None:
			print("저장된 데이터가 없습니다.")
			return
		else:
			self.head = self.head.next

	def search_node(self, data):   # 몇 번째 노드인지 검색
		if self.head == None:
			print("저장된 데이터가 없습니다.")
			return
		else:
			link = self.head
			index = 0
			while link:
				if data == link.data:
					return index
				else:
					link = link.next
					index += 1

if __name__ == "__main__":
	num_list = SinglyLinkedList()
	num_list.insert_node(1)
	num_list.insert_node(2)
	num_list.insert_node(3)
	num_list.insert_node(4)
	num_list.insert_node(5)
	num_list.print_node()

	# 탐색
	result = num_list.search_node(3)
	print("3의 위치: {}".format(result), "\n")
	
	num_list.delete_node()
	num_list.delete_node()
	num_list.print_node()
