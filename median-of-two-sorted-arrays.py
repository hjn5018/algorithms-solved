def findMedianSortedArrays(nums1, nums2):
    # nums1이 항상 짧은 배열이 되도록 보장
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1  

    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partitionX = (low + high) // 2  # nums1을 나누는 위치
        partitionY = (x + y + 1) // 2 - partitionX  # nums2를 나누는 위치

        # 경계 값 설정 (넘어가면 무한대나 -무한대로 처리)
        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == x else nums1[partitionX]

        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == y else nums2[partitionY]

        # 정답 조건 확인
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (x + y) % 2 == 0:  # 전체 길이가 짝수인 경우
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:  # 전체 길이가 홀수인 경우
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:  # 왼쪽이 너무 크면 왼쪽으로 이동
            high = partitionX - 1
        else:  # 오른쪽이 너무 크면 오른쪽으로 이동
            low = partitionX + 1
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
