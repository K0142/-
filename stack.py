# stack 클래스 선언
class Stack:
	def __init__(self):
		self.stack = []

	def push(self, data):
		self.stack.append(data)
	
	def pop(self):
		pop_data = None
		if self.isEmpty():
			print("데이터가 없습니다.")
		else:
			 pop_data = self.stack.pop()
		
		return pop_data

	# 마지막에 삽입한 데이터를 삭제하지 않고 return
	def top(self): 
		top_data = None
		if self.isEmpty():
			print("데이터가 없습니다.")
		else:	
			top_data = self.stack[-1]
		
		return top_data

	# 스택이 비어있는지 확인하는 메소드
	def isEmpty(self):
		is_empty = False
		if len(self.stack) == 0:
			is_empty = True
		
		return is_empty

if __name__ == "__main__":
	num_stack = Stack()

	# push data
	num_stack.push(1)
	num_stack.push(2)
	num_stack.push(3)
	print("stack: ", num_stack.stack)

	# top data
	top_data = num_stack.top()
	print("top data: ", top_data)

	# pop data
	pop_data = num_stack.pop()
	print("pop data: ", pop_data)
	num_stack.pop()
	num_stack.pop()

	# isEmpty stack
	print("T / F: ", num_stack.isEmpty())
	
	
