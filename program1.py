# # #Problem-01: 
# # # Find Multiples of Three
# # # รับ start และ end แล้วหาเลขทุกตัวในช่วงนี้ที่หารด้วย 3 ลงตัว
# def find_number(start,end):
    
#     result = []
    
#     for i in range(start,end+1):
#         if i%3==0:
#             result.append(i)
#     return result

# while True:    
#     try:
#         start = int(input(" กรอกตัวเลข ระหว่าง 1-100 : "))
#         end = int(input(" กรอกตัวเลข ระหว่าง 1-100 : "))
        
#         if start<1 or end>100:
#             print("กรุณากรอกตัวเลขระหว่าง 1-100")
#             continue
        
#         if start > end:
#             print("ตัวเลข start มากกว่า end ไม่สมารถคำนวณได้ ")
#             continue
#         break

#     except ValueError:
#         print("กรุณากรอกตัวเลขเท่านั้น")


# result = find_number(start,end)

# if result:
    
#     print(f"List ของตัวเลขทั้งหมดที่หารด้วย 3 ได้ลงตัว = {result} ")
#     print(f"พบทั้งหมด: {len(result)} ตัว ")
    
# else:
#     print(" ไม่พบตัวเลขที่หารด้วย 3 ลงตัว ")
    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# def find_multiples_of_three(start: int, end: int) -> list:
#     # 1. ตรวจสอบเงื่อนไข: ถ้า start มากกว่า end ให้คืนค่า list ว่างทันที
#     if start > end:
#         return []
    
#     # สร้าง list ว่างไว้สำหรับเก็บผลลัพธ์
#     result = []
    
#     # 2. วนลูปตั้งแต่ start จนถึง end (ต้องใช้ end + 1 เพื่อให้ครอบคลุมตัวปลายทาง)
#     for num in range(start, end + 1):
        
#         # เช็กว่าตัวเลขในรอบนั้น หารด้วย 3 ลงตัวหรือไม่ (เศษเท่ากับ 0)
#         if num % 3 == 0:
#             result.append(num)  # ถ้าหารลงตัว ให้นำตัวเลขนั้นใส่เข้าไปใน result
            
#     # 3. ส่งคืน list ผลลัพธ์
#     return result

# # --- ตัวอย่างการรันใช้งาน ---
# output = find_multiples_of_three(10, 25)
# print(output)
# # Output: [12, 15, 18, 21, 24]





def find_number(start:int,end:int):
    
    if start>end:
        return []
    result = []
    
    for i in range(start,end+1):
        
        if i % 3==0:
            result.append(i)
            
    return result