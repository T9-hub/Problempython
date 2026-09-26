def analyze_user_activity(log_file_path: str) -> dict:
    users = set()
    action_counts = {}
    user_total_duration = {}
    login_durations = []

    try:
        with open(log_file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue  # ข้ามบรรทัดว่าง

                parts = line.split()
                if len(parts) != 4:
                    continue    # ข้ามบรรทัดที่ข้อมูลไม่ครบ 4 ส่วน

                timestamp_str, user_id, action, duration_str = parts

                try:
                    duration = float(duration_str)
                except ValueError:
                    continue    # ข้ามบรรทัดที่แปลง duration เป็นตัวเลขไม่ได้

                users.add(user_id) # เพิ่ม ID เข้า set (คำนวณจำนวน user แบบไม่ซ้ำ)
                action_counts[action] = action_counts.get(action, 0) + 1 # นำ action ไปนับจำนวนเพิ่มทีละ 1
                user_total_duration[user_id] = ( # บวกสะสมเวลาการใช้งานของ user คนนั้นๆ
                    user_total_duration.get(user_id, 0.0) + duration
                )

                if action == "login": # ถ้า action คือ 'login' ให้เก็บระยะเวลาไว้คำนวณค่าเฉลี่ย
                    login_durations.append(duration)

    except FileNotFoundError:
        # กรณีหาไฟล์ไม่พบ
        pass

    most_active_user = None
    if user_total_duration:
        most_active_user = max(
            user_total_duration, key=user_total_duration.get
        )

    if login_durations:
        average_session_time = sum(login_durations) / len(login_durations)
    else:
        average_session_time = 0.0

    return {
        "total_users": len(users),
        "action_counts": action_counts,
        "most_active_user": most_active_user,
        "average_session_time": average_session_time,
    }


if __name__ == "__main__":
    result = analyze_user_activity("activity.log")
    from pprint import pprint
    pprint(result)
# {'action_counts': {'login': 2, 'logout': 2, 'submit': 1, 'view': 2},
#  'average_session_time': 160.0,
#  'most_active_user': 'u002',
#  'total_users': 2}