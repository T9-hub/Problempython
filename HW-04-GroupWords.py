
# ฟังก์ชันจะต้อง "ข้าม" หรือ "ไม่สนใจ" สตริงว่าง ("")
def find_group(words:list) -> list:
    # สร้างDicสำหรับจัดกลุ่ม 
    groups = {}
    # วนลูปเช็กทีละคำ
    for word in words:
        cleaned_word = word.strip().lower()        
        if not cleaned_word: 
            # ถ้าwordเป็นสตริงว่าง("")ให้ข้ามไป
            # ไม่นำมารวมในกลุ่ม
            continue
        # สร้างตัว Signature
        # เรียง A-Z เพื่อให้คำเป็น Anagram 
        signature = "".join(sorted(cleaned_word))
        if signature not in groups:
            groups[signature] = []
            
        groups[signature].append(cleaned_word)
    
    return list(groups.values())




# เรียกใช้ 

def main():
    
    all_words = []
    print("="*50)
    print("โปรแกรมจัดกล่มคำ (Anagram Grouping Tool)")
    print("="*50)
    print("คำแนะนำ:")
    print(" - พิมพ์คำที่ต้องการจัดกลุ่มคำ (ใส่หลายคำได้โดยใช้วรรค หรือ , แยก)")
    print(" - พิมพ์ 'clear' เพื่อเริ่มใส่ข้อมูลใหม่")
    print(" - พิมพ์ 'exit' or 'quit' เพื่อออกจากโปรแกรม")
    print("="*50)


    while True:
        # .strip() ใช้สำหรับลบช่องว่างส่วนเกินที่อยู่ด้านหน้าและด้านหลังของข้อความ
        user_input = input("\nป้อนคำศัพท์ (หรือคำสั่ง) : ").strip() # ("text ") = "text"
        
        
        # เช็คเงื่อนไขการออกจากโปรแกรม
        if user_input.lower() in ["exit","quit"]:
            print("\nขอบคุณที่ใช้โปรแกรม! ปิดการทำงานเรียบร้อย.")
            break
        
        if user_input.lower() == "clear":
            all_words.clear()
            print(">> ล้างข้อมูลเรียบร้อยเเล้ว ! ")
            continue
        
        # สร้างตัวเเยกคำด้วย เว้นวรรค หรือ เครื่องหมายจุลาค
        raw_word = user_input.replace(","," ").split()
        
        if not raw_word:
            print(">> [เตือน คุณไม่ได้กรอกคำศัพท์ใด หรือ กรอกเพียงช่องว่าง]")
            continue # ให้โปรแกรมทำงานต่อ
        
        
        # สะสมคำศัพท์เพิ่มเข้าไปใน list
        all_words.extend(raw_word)
        
        
        # ประมวลผลและแสดงผลลัพธ์ทันที
        result_gruop = find_group(all_words)
        
        print("\n--- ผลลัพธ์การจัดกลุ่มล่าสุด ---")
        print(f"จำนวนกลุ่มทั้งหมด: {len(result_gruop)} กลุ่ม")
    
        
        for i, group in enumerate(result_gruop, 1):
            print(f"  กลุ่มที่ {i}: {group}")
        print("-" * 32)
    
# เรียกใช้งานโปรแกรม
if __name__ == "__main__":
    main()

# # หรือจะเรียกใช้แบบ
# # --- ทดสอบการใช้งาน ---
# data = [" listen ", "Silent", "   ", "rat", "Tar"]
# print(find_group(data))
# # ผลลัพธ์: [['listen', 'silent'], ['rat', 'tar']]