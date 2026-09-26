def divid(a,b):
    
    try:
        result = a/b
        
    except ZeroDivisionError as e:
        print(f"Exception is : {e} " )
        return None
    
    else:
        return result
    

round_count = 1

while True:
    
    print(f"--- การทำงานรอบที่ {round_count} ------")
    
    try:
        a = float(input("กรอกตัวเลขตัวตั้ง : "))
        b = float(input("กรอกตัวเลขตัวหาร : "))
        
        
        res = divid(a,b)
        
        if res is not None:
            print(f" The result {a} divided by {b} is {res}")
            
    
    except ValueError:
        print("กรุณากรอกตัวเลขเท่านั้น")
    
    # ถามผู้ใช้ว่าต้องการทำต่อมั้ย
    
    user_choice = input("คุณต้องการสร้างการหารต่อมั้ย : ( y/n ) ").strip().lower()
    
    
    if user_choice.lower() == "y":
        round_count +=1
        break
    elif user_choice.lower() == "n":
        print("ขอบคุณที่ใช้บริการ")
        break
    else:
        print("กรุณากรอกเฉพาะ  Y AND N เท่านั้น")
        
    
    if user_choice.lower() == "exit":
        print("จบการทำงาน")
        break