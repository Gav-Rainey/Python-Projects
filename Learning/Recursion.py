# Numbers = [2, 4, 6]
# Result = 0
#
#
# def Sum(Nums, Res):
#     if len(Nums) > 0:
#         Res += Nums[0]
#         print(Res)
#         Nums.remove(Nums[0])
#         Sum(Nums, Res)
#
#     return
#
#
# Sum(Numbers, Result)

# List = [2, 4, 8, 10]
# Result = 0
# Index = 0
#
#
# def Count(Elements, Res, Counter):
#     if len(Elements) > 0:
#         Counter += 1
#         Elements.remove(Elements[0])
#         Count(Elements, Res, Counter)
#     else:
#         print(Counter)
#
#     return
#
#
# Count(List, Result, Index)

# List = [2, 4, 8, 10, 20, 3, 18]
# Result = 0
# Index = 0
#
#
# def Max(Elements, NumA):
#     if len(Elements) > 1:
#         NumA = Elements[0]
#         NumB = Elements[1]
#
#         if NumA > NumB:
#             Elements.remove(NumB)
#             Max(Elements, NumA)
#         else:
#             Elements.remove(NumA)
#             Max(Elements, NumB)
#     else:
#         print(NumA)
#
#     return
#
#
# Max(List, 0)

List = [10, 4, 8, 8, 20, 3, 18]
Result = 0
Index = 0
Jango = 1


# def QuickSort(Elements, Index, Jango):
#     if Elements[Index] < Elements[Jango]:
#         Elements[Index], Elements[Jango] = Elements[Jango], Elements[Index]
#         Index += 1
#         Jango += 1
#         QuickSort(Elements, Index, Jango)
#     else:
#         print(Elements)
#
#     return
#
#
# QuickSort(List, Index, Jango)

def QuickSort(Elements):
    if len(Elements) < 2:
        return Elements
    else:
        pivot = Elements[0]
        lessThan = [i for i in Elements[1:] if i < pivot]
        greaterThan = [i for i in Elements[1:] if i > pivot]

        return QuickSort(lessThan) + [pivot] + QuickSort(greaterThan)


print(str(QuickSort(List)))
