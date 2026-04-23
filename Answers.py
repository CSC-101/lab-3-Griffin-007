more = [x + 1 for x in [1,2,3,4]]     # List, in order, the values that x takes at each step. -> 1+1=2, 2+1=3, 3+1=4, 4+1=5
print(more)                               # What is the value of more at this point? -> [2, 3, 4, 5]

def square(n:int) -> int:
    return n * n                           # Record, in order of the calls, each value of n and the corresponding return value. -> 1, 1*1=2; 2, 2*2=4; 3, 3*3=9; 4, 4*4=16
squares = [square(x) for x in [1,2,3,4]]   # What is the value of squares and how does this relate to the values recorded above? -> the value of squares is [1, 4, 9, 16], being comprised of the functions recorded above
print(squares)

def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and the corresponding return value. -> 0>2, false; 1>2, false; 2>2, false; 3>2, true; 4>2, true
answer = [x for x in range(5) if check(x)]   # What is the value of answer? -> [3, 4]
print(answer)

def inc(m:int) -> int:
    return m + 1                             # Record, in order of the calls, each value of m and the corresponding return value. -> 0+1=1; 1+1=2; 2+1=3; 3+1=4; 4+1=5
def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and the corresponding return value -> 1>2; false; 2>2, false; 3>2, true, 4>2, true, 5>2, true
answer = [inc(x) for x in range(5) if check(x)]   # What is the value of answer? -> [4, 5]
print(answer)

def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           # Record each value of total and num at the end of the loop body. -> 4, 4; 4, 13; 2, 15; 1, 16
    return total
result = tally([4, 9, 2, 1])
print(result)

def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # Record each value of new_list and idx at the end of the loop body. ->idx=0, new_list=[4]; idx=1, new_list= [4,9]; idx=2, new_list=[4,9,2]; idx=1, new_list=[4,9,2,1]
    return new_list                    # How does this loop differ from that above? -> tally was directly pulling values, whereas copy was pulling values from position in the list
result = copy([4, 9, 2, 1])
print(result)

def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # Record each value of new_list and value at the end of the loop body. 4+1, [5]; 9+1, [5, 10]; 2+1, [5, 10, 3]; 1+1, [5, 10, 3, 2]
    return new_list
result = increment_all([4, 9, 2, 1])
print(result)

new