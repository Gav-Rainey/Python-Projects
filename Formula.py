# i = 0
#
# list1 = [1, 2, 3, 4, 5]
# list2 = ["a", "b", "c", "d", "e"]
# read = ""
#
# with open("text.txt", "r") as file:
#     while read.strip("\n") != str(list1[0]):
#         read = file.readline()
#         if read.strip("\n") == str(list1[0]):
#             print(list2[i])
#             break
#         else:
#             i += 1

# list1 = [1, 2, 3, 4, 5]
# list2 = ["a", "b", "c", "d", "e"]
# read = ""
#
# with open("text.txt", "r") as file:
#
#     for x in list1:
#         while read.strip("\n") != str(list1[x-1]):
#             read = file.readline()
#             if read.strip("\n") == str(list1[x-1]):
#                 print(list1[x-1])
#                 break
#
i=0
list2 = ["BP", "GP", "YP", "RP", "OP"]
list3 = [1, 0.5, 0.33, 0.25, 0.2, 1, 0]

with open("Belfast_SouthEast.txt", "r") as file:
    for x in enumerate(file):
        i = 0
        print(x[1])

        if x[1] == list3[0]:
            print("Blue Party - " + str(x[1]))
        elif x[1] == list3[0]:
            print("Green Party - " + str(x[1]))
        elif x[1] == list3[0]:
            print(list2[2])
        elif x[1] == list3[0]:
            print(list2[3])
        elif x[1] == list3[0]:
            print(list2[4])
        else:
            break
