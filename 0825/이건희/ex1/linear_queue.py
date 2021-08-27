# Queue의 사이즈 지정 - createQueue
# 고정 크기의 배열로 Queue를 생성하는 것이 상대적으로 가변 배열(리스트)보다 빠르다.
SIZE = 4
Q = [0] * SIZE

# 초기 상태의 표현
front, rear = -1, -1

# isFull
def is_full():
    """
    Queue가 포화상태인지 확인
    - 리스트에서는 큰 문제가 되지 않지만 고정 배열의 경우 확인 필요
    """
    global rear
    if rear == SIZE-1:
        return True
    else:
        return False

# isEmpty
def is_empty():
    """
    Queue가 공백상태인지 확인
    """
    global front, rear
    if front == rear:
        return True
    else:
        return False

# enQueue
def enqueue(item):
    """
    Queue의 뒤쪽(rear 다음)에 원소를 삽입
    - rear를 뒤쪽으로 옮기고 (rear + 1)그 자리에 원소를 삽입
    - Stack의 top을 옮겨놓고 그 자리에 요소를 넣었던 것을 떠올리자
    """
    global rear
    if is_full():
        print("Q is full")
    else:
        rear += 1
        Q[rear] = item

# deQueue
def dequeue():
    """
    Queue의 앞쪽(front)에서 원소를 삭제하고 반환
    - front를 뒤쪽으로 옮기고(front + 1) 그 자리에 있는 원소를 반환하며 삭제
    """
    global front
    if is_empty():
        return "Q is empty"
    else:
        front += 1
        return Q[front]
# Qpeek
def Qpeek():
    """
    Queue의 앞쪽(front)의 한 자리뒤(front+1)에서 원소를 삭제없이 반환
    - front의 값을 단순하게 증가시켜 가져온다. (큐의 첫 번째 원소 반환)
    - 이때 중요한 것은 dequeue와 다르게 front의 값 자체를 '변경'하지 않는다는 점
     - front += 1은  front + 1과 다르다.
     - dequeue와 비교하며 생각
    """
    global front, rear
    if is_empty():
        return "Can't use it"
    else:
        return Q[front//4+1]

#1. Queue 초기화 상태 확인
print(Q)

#2. Queue가 비었는지 확인
print(is_empty()) # True

#3. enQueue 작업 & 확인
enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
enqueue(5) # Queue is full!

print(Q)

#4. Qpeek
print(Qpeek())

#5. deQueue 작업 & 확인
print(dequeue()) # 1
print(dequeue()) # 2
print(dequeue()) # 3
print(dequeue()) # 4
print(dequeue()) # Queue is empty!