def find_first_pair_with_product(nums: list, target: int):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] * nums[j] == target:
                return nums[i], nums[j]  # ส่งค่าคืนเฉพาะคู่แรกที่เจอทันที
                # result.append((nums[i], nums[j]))  คืนทุกคู่เลย
    return None

# ตัวอย่างการใช้งาน
numbers = [2, 4, 3, 6, 8, 12]
target_product = 24

result = find_first_pair_with_product(numbers, target_product)
print(result)  # Output: (2, 12)