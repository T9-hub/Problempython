def is_prime(n: int) -> bool:
    # 1. แก้ไขเป็น <= 1 เพราะ 1 ไม่ใช่จำนวนเฉพาะ
    if n <= 1:
        return False

    # ตรวจสอบตัวหารตั้งแต่ 2 ถึง sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def prime_number_in_range(start: int, end: int) -> dict:
    prime_number = []

    for i in range(start, end + 1):
        if is_prime(i):
            prime_number.append(i)

    # ส่งค่า start, end, รายการจำนวนเฉพาะ และจำนวนกลับออกไปเป็น Dictionary
    return {
        "start": start,
        "end": end,
        "prime": prime_number,
        "count": len(prime_number),
        "sum": sum(prime_number),  # แถมผลรวมตามโจทย์ให้ด้วย
    }


# --- ส่วนการเรียกใช้งาน ---
s = 60
e = 120
result = prime_number_in_range(s, e)

# ดึงค่า start และ end จาก Dictionary ที่คืนค่ากลับมา
print(
    f"prime_number ในช่วง {result['start']} ถึง {result['end']} ได้แก่: "
    f"{' '.join(map(str, result['prime']))}"
)
print(f"จำนวนทั้งหมด: {result['count']} ตัว")
print(f"ผลรวม: {result['sum']}")