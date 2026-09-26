while True:
    
    try:
        # บล็อก try ใส่เฉพาะคำสั่งที่เสี่ยงเกิด FileNotFoundError เท่านั้น
        file_name = input("Enter a file name (or type 'exit' to quit): ")
        
        if file_name.lower() == "exit":
                print("Exiting program.")
                break
            
        infile = open(file_name, "r", encoding="utf-8")

    except FileNotFoundError:
        # ทำงานเมื่อหาไฟล์ไม่พบ
        print(f"ไม่พบไฟล์ชื่อ '{file_name}' กรุณาลองใหม่อีกครั้ง\n")

    except IOError as e:
        # ทำงานเมื่อเกิดข้อผิดพลาดในการเปิดไฟล์อื่นๆ
        print(f"เกิดข้อผิดพลาดในการเปิดไฟล์: {e}\n")

    else:
        # ทำงานเมื่อเปิดไฟล์สำเร็จ (ไม่มี Exception เกิดขึ้นใน try)
        content = infile.read()
        print("\n--- File Content ---")
        print(content)
        print("--------------------\n")
        infile.close()  # อย่าลืมปิดไฟล์เมื่อทำงานเสร็จ

        break  # ออกจากลูปเพราะอ่านไฟล์เรียบร้อยแล้ว