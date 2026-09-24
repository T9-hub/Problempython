# Problem-03: "โปรแกรมหาตัวหาร (Divisors/Factors) ของจำนวนเต็ม

# รับจำนวนเต็ม n แล้วหาตัวเลขทั้งหมดที่สามารถหาร n ลงตัว
def find_divisor_number(n:int):
        
    result = []
    
    for i in range(1,n+1):
        
        # i หาร n ลงตัวไหม?
        # เรากำลังหารตัวหารที่หารด้วยเลขของมันอยู่
        if n%i == 0:
            result.append(i)
    return result

while True:
    
    try:
        user_input = int(input("กรุณากรอกตัวเลข 1 ตัว : "))
        n = user_input
        
        if user_input < 0:
            print("ตัวเลขน้อยกว่า 0 ไม่ได้กรุณากรอกใหม่")
            continue
        if user_input >1000:
            print("ตัวเลขมากกว่า 1,000 ไม่ได้กรุณากรอกใหม่")
            continue
        
        break
        
    except ValueError:
        print("ให้กรอกตัวเลขเท่านั้น!!")
    

result = find_divisor_number(n)

if result:
    # print(f"ตัวเลขที่หาร {n} ได้ลงตัวได้แก่ {result} ")
    # if you want to see output int not list use joint map
    print(f"ตัวเลขที่หาร {n} ได้ลงตัวได้แก่ {",".join(map(str,result))} ")
    print(f"ตัวเลขที่หาร {n} ได้ลงตัวได้แก่",*result)
    
    # หรือจะใช้
    #     print(f"ตัวเลขที่หาร {n} ได้ลงตัวได้แก่:")
    # for num in result:
    #     print(num)  # num จะมีประเภทข้อมูลเป็น int นำไปใช้งานต่อได้ทันที
    print(f"พบจำนวนที่หารลงตัวทั้ง {len(result)} ตัว")
    

else:
    print(f" ไม่เจอตัวเลขที่หาร {n} ลงตัวเลย ")