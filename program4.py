# Problem-06: Prime Numbers
def prime_number(n:int):
    
    if n<=1:
        return False
    
    for i in range(2,n):
        if n%i==0:
            return False
    return True


print(prime_number(9))



# Problem-06-1: Prime number in range
def find_prime_in_range(start:int,end:int):
    
    primes = []
    
    for num in range(start,end+1):
        if prime_number(num):
            primes.append(num)
            
    return primes

print(find_prime_in_range(1,50))





# Problem-06-2: ตรวจสอบจำนวนสมบูรณ์ is_perfect_number ผลรวมของตัวหารทั้งหมด ที่ไม่รวมตัวมันเอง เช่น 

def is_perfect_number(n:int) ->bool:
    
    if n<=1:
        return False
    
    
    sum_divisor = 0
    
    for i in range(1,n):
        if n % i ==0:
            sum_divisor +=i
            
            
            # เมื่อวนลูปครบแล้ว จะเปรียบเทียบว่า ผลรวมตัวหาร (sum_divisor) เท่ากับตัวเลขเดิม (n) หรือไม่
            # ถ้าเท่ากัน จะ คืนค่า True  ไม่เท่าคืน False
    return sum_divisor == n


print(is_perfect_number(6))



# Problem-06-3: โปรแกรมหาตัวหารร่วมมาก
def find_gcd(a: int, b: int) -> int:
    gcd = 1
    min_num = min(a, b)
    
    for i in range(1, min_num + 1):
        if a % i == 0 and b % i == 0:
            gcd = i  # อัปเดตตัวหารร่วมที่มากที่สุด
            
    return gcd

print(find_gcd(12, 18))  # ได้ 6 (เพราะ 6 หารทั้ง 12 และ 18 ลงตัว)