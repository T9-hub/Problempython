while True:
    try:
        rows = int(input("กรอกจำนวนแถวของดาว (หรือพิมพ์ 0 เพื่อเลิก): "))
        
        if rows == 0:
            print("จบการทำงาน")
            break
            
        if rows < 0:
            print("กรุณากรอกตัวเลขที่มากกว่า 0\n")
            continue
            
        print("\n--- รูปสามเหลี่ยมซ้าย ---")
        for i in range(1, rows + 1):
            print("*" * i)
            
        print("\n--- รูปสามเหลี่ยมขวา ---")
        for i in range(1, rows + 1):
            # ช่องว่างลดลง (rows - i) + ดาวเพิ่มขึ้น (i)
            print(" " * (rows - i) + "*" * i)
            
        print("\n--- รูปพีระมิด ---")
        for i in range(1, rows + 1):
            # ช่องว่างตรงกลาง + ดาวเลขคี่ (2 * i - 1)
            print(" " * (rows - i) + "*" * (2 * i - 1))
            
        print("-" * 30 + "\n")
        print()
    except ValueError:
        print("ข้อผิดพลาด: กรุณากรอกเฉพาะตัวเลขจำนวนเต็มเท่านั้น!\n")