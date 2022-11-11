# 리스트 생성
def add_data(animal):
	animal_list.append(None)             # 빈칸 추가
	list_len = len(animal_list)          # 배열의 현재 크기
	animal_list[list_len - 1] = animal

# 데이터 삽입
def insert_data(position, animal):
	if position <0 or position > len(animal_list):
		print("데이터 삽입 범위를 벗어났습니다.")
		return
	animal_list.append(None) 
	list_len = len(animal_list)
	for i in range(list_len - 1, position, -1):
		animal_list[i] = animal_list[i-1]
		animal_list[i-1] = None
	animal_list[position] = animal

# 데이터 삭제
def delete_data(position):
	if position <0 or position > len(animal_list):
		print("데이터 삭제 범위를 벗어났습니다.")
		return
	list_len = len(animal_list)
	animal_list[position] = None
	for i in range(position+1, list_len):
		animal_list[i-1] = animal_list[i]
		animal_list[i] = None
	del(animal_list[list_len-1])

# 변수 선언
animal_list = []
select = -1      # 1: 추가 2: 삽입 3: 삭제 4: 종료
if __name__ == "__main__":
	while(select !=4):
		select = int(input("선택하세요(1: 추가 2: 삽입 3: 삭제 4: 종료) ==>"))
		if(select==1):
			data = input("추가할 데이터 ==>")
			add_data(data)
			print(animal_list)
		elif(select==2):
			pos = int(input("삽입할 위치 ==>"))
			data = input("추가할 데이터 ==>")
			insert_data(pos, data)
			print(animal_list)
		elif(select==3):                        
			pos = int(input("삭제할 데이터 ==>"))
			delete_data(pos)
			print(animal_list)
		elif(select==4):        
			print(animal_list)
			exit
		else:
			print("1-4중 하나를 입력하세요.")
			continue
