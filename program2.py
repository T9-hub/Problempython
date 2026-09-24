# Problem-02: รับตัวเลขเข้ามา 5 จำนวน LOOP เอามาดูว่าจำนวน  คำนวณ ผลรวม เเละ ค่าเฉลี่ย

# def calculate_sum_and_avg() -> None: 
#     numbers = []
#     for i in range(1,6):
#         num = int(input(f"กรุณากรอกตัวเลขตัวที่ {i} : "))
#         numbers.append(num)
#         # ทีนี้เราก็จะได้ num เเต่ละตัวออกมาดูได้ ไม่ใช่ list 
        
#         # ผลรวม
#         sum_num = sum(numbers)
#         #  ค่าเฉลี่ย
#         avg = sum_num / len(numbers)
        
        
#     print(f"ตัวเลขใน list ทั้งหมดมี : {numbers}")
#     print(f" ผลรวมตัวเลขใน list ทั้งหมด = : {sum_num}")
#     print(f" ค่าเฉลี่ยนตัวเลขใน list ทั้งหมด = : {avg}")
# print(calculate_sum_and_avg())

# ADVANCE มาหน่อย
def calculate_advanced_stats() -> None:
    numbers = []
    
    # 1. ปรับเปลี่ยนเป็น Dynamic Loop (รับกี่จำนวนก็ได้)
    print("--- Program Started (Type 'done' to finish input) ---")
    
    while True:
        user_input = input(f"Enter number {len(numbers) + 1}: ").strip()
        
        # เงื่อนไขการหยุดรับข้อมูล (Sentinel Value)
        if user_input.lower() == 'done':
            if len(numbers) == 0:
                print("Error: Please enter at least one number before finishing.")
                continue
            break
            
        # 2. Input Validation ป้องกันโปรแกรมค้างจากตัวอักษร
        try:
            num = float(user_input)
            numbers.append(num)
        except ValueError:
            print("Invalid input! Please enter a valid real number or 'done'.")

        
    # 3. คำนวณสถิติเบื้องต้นและขั้นสูง
    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count
    max_val = max(numbers)
    min_val = min(numbers)

    # แสดงผลลัพธ์การประมวลผล
    print("\n" + "="*30)
    print(f"Total numbers entered : {count}")
    print(f"Sum                  : {total_sum:.2f}")
    print(f"Average              : {average:.2f}")
    print(f"Max Value            : {max_val:.2f}")
    print(f"Min Value            : {min_val:.2f}")
    print("="*30)

calculate_advanced_stats()