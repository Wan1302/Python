# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# count = 0
# print("[", end = "")
# for i in range(0, x+1):
#     for j in range(0, y+1):
#         for k in range(0, z+1):
#             if i + j + k != n:
#                 count = count + 1
#                 formatted_string = "[{}, {}, {}]".format(i, j, k)
#                 if(i == x and j == y and k == z and count != 0): print(formatted_string, end = "")
#                 else: print(formatted_string, end = ", ")
# print("]")


# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
    
# outcome = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k != n)]
    
# print(outcome)


# n = int(input())
# arr = map(int, input().split())
# other_arr = my_list(set(arr))
# other_arr = sorted(other_arr, reverse = True)
# print(other_arr[1])

# participants = []
# score_set = set()
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     participants.append((name,score))
#     if score not in score_set:
#         score_set.add(score)

# score_set = sorted(score_set)
# max = score_set[1]
# names = [participant[0] for participant in participants if participant[1] == max]
# names = sorted(names)
# for name in names:
#     print(name)


# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = map(float, line)
#     student_marks[name] = scores
# query_name = input()
# scores = student_marks[query_name]
# output = sum(scores) / 3.0
# output = "{:.2f}".format(output)
# print(output)

# def print_formatted(number):
#     dorong = len("{0:b}".format(number))
#     for i in range(1, number+1):
#         print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width = dorong))

# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)

# n = int(input())
# my_list = []
# for i in range(0,n):
#     s = str(input()).split()
#     if(s[0] == 'insert'):
#         x = int(s[1])
#         y = int(s[2])
#         my_list.insert(x, y)
#     elif(s[0] == 'print'):
#         print(my_list)
#     elif(s[0] == 'remove'):
#         x = int(s[1])
#         my_list.remove(x)
#     elif(s[0] == 'append'):
#         x = int(s[1])
#         my_list.append(x)
#     elif(s[0] == 'sort'):
#         my_list.sort()
#     elif(s[0] == 'pop'):
#         my_list.pop()
#     else:
#         my_list.reverse()   

# def swap_case(s):
#     result = ''
#     for i in s:
#         if('a' <= i <= 'z'):
#             result += i.upper()
#         elif('A' <= i <= 'Z'):
#             result += i.lower()
#         else: 
#             result += i
#     return result

# if __name__ == '__main__':
#     s = str(input())
#     s = swap_case(s)
#     print(s)


# def mutate_string(string, position, character):
#     string = string[:position] + character + string[6:] 
#     return string

# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)


#Replace all ______ with rjust, ljust or center. 

# thickness = int(input()) #This must be an odd number
# c = 'H'

# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# # #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))    

# # #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

# # #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# import textwrap

# def wrap(string, max_width):
#     result = textwrap.wrap(string, max_width)
#     return result

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)

# n, m = map(int, input().split())
# char = '.|.'
# for i in range(0, n//2):
#     print((char*(2*i + 1)).center(m, '-'))

# print('WELCOME'.center(m, '-'))

# for i in range(n//2 - 1, -1, -1):
#     print((char*(2*i + 1)).center(m, '-'))

# def print_rangoli(size):
#     import string

#     # Create a string of lowercase letters
#     alphabet = string.ascii_lowercase

#     # Create a list of letters to be used in the rangoli
#     letters = [alphabet[i] for i in range(size)]

#     # Create the top half of the rangoli
#     top_half = []
#     for i in range(size, 0 , -1):
#         row = '-'.join(letters[size - 1:i-1:-1] + letters[i - 1:size])
#         top_half.append(row.center(size * 4 - 3, '-'))

#     # Combine the top half and its reverse to get the full rangoli
#     rangoli = top_half + top_half[::-1][1:]

#     # Print the rangoli
#     for row in rangoli:
#         print(row)

# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)

from math import *

# n = int(input())
# x = list(map(int, input().split()))
# y = list(map(int, input().split()))

# s1 = sqrt(sum(i*i for i in x))
# s2 = sqrt(sum(i*i for i in y))

# s = sum(X*Y for X,Y in zip(x, y))

# result = s / (s1*s2)

# print(f'{result :.4f}')


def Tinh(x):
    max = 0
    for i in range(len(x)):
        sub = x[i+1] - x[i]
        if(sub > max): max = sub 
    return max
n = int(input())
x = list(map(int, input().split()))
result = Tinh(x)
print(result)