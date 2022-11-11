# Queue 클래스 선언
class Queue:
	def __init__(self):
		self.queue = []

	def enqueue(self, data):
		self.queue.append(data)

	def dequeue(self):
		dequeue_data = None
		if self.isEmpty():
			print("데이터가 없습니다.")
		else:
			dequeue_data = self.queue[0]
			self.queue = self.queue[1:]
		return dequeue_data

	# 데이터를 꺼내지 않고 어떤 값인지 return
	def peek(self):
		peek_data = None
		if self.isEmpty():
			print("데이터가 없습니다.")
		else:
			peek_data = self.queue[0]
		return peek_data

	def isEmpty(self):
		is_empty = False
		if len(self.queue) == 0:
			is_empty = True
		return is_empty

if __name__ == "__main__":
	num_queue = Queue()

	# enqueue data
	num_queue.enqueue(1)
	num_queue.enqueue(2)
	num_queue.enqueue(3)
	print("Queue: ", num_queue.queue)

	#peek data
	print("peek data: ", num_queue.peek())

	# dequeue data
	dequeue_data = num_queue.dequeue()
	print("dequeue data: ", dequeue_data)
	num_queue.dequeue()
	num_queue.dequeue()

	# isEmpty
	print("T/F: ", num_queue.isEmpty())
