def is_prime(num):
    # 1은 소수가 아님
    if num < 2:
        return False
    # 2부터 num-1까지의 수로 나누어 떨어지는지 확인
    for i in range(2, num):
        if num % i == 0:
            return False # 나누어 떨어지면 소수가 아님
    return True # 위 반복문을 통과하면 소수임

def sosu(numbers):
    count = 0
    for number in numbers:
        if is_prime(number):
            count += 1
    return count

# 입력 처리
N = int(input())
numbers = list(map(int, input().split()))

# 함수 호출 및 결과 출력
prime_count = sosu(numbers)
print(prime_count)