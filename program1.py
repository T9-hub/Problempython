#Problem-01:
# # Find Multiples of Three
# # รับ start และ end แล้วหาเลขทุกตัวในช่วงนี้ที่หารด้วย 3 ลงตัว
def find_number(start,end):
    
    result = []
    
    for i in range(start,end+1):
        if i%3==0:
            result.append(i)
    return result

while True:    
    try:
        start = int(input(" กรอกตัวเลข ระหว่าง 1-100 : "))
        end = int(input(" กรอกตัวเลข ระหว่าง 1-100 : "))
        
        if start<1 or end>100:
            print("กรุณากรอกตัวเลขระหว่าง 1-100")
            continue
        
        if start > end:
            print("ตัวเลข start มากกว่า end ไม่สมารถคำนวณได้ ")
            continue
        break

    except ValueError:
        print("กรุณากรอกตัวเลขเท่านั้น")


result = find_number(start,end)

if result:
    
    print(f"List ของตัวเลขทั้งหมดที่หารด้วย 3 ได้ลงตัว = {result} ")
    print(f"พบทั้งหมด: {len(result)} ตัว ")
    
else:
    print(" ไม่พบตัวเลขที่หารด้วย 3 ลงตัว ")
    





