def merge(list1, list2):
    merge_list = []
    if list1 is not None or list2 is not None:
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] > list2[j]:
                    merge_list.append(list1[i])
                    i += 1
                else:
                    merge_list.append(list2[j])
                    j += 1

        return merge_list
# 코드를 작성하세요.

# 테스트
print(merge([1], []))
print(merge([], [1]))
print(merge([2], [1]))
print(merge([1, 2, 3, 4], [5, 6, 7, 8]))
print(merge([5, 6, 7, 8], [1, 2, 3, 4]))
print(merge([4, 7, 8, 9], [1, 3, 6, 10]))