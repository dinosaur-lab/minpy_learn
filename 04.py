"""
# タプル
a = [('sensya', 1, 2, 3), ('sensya1', 1, 2, 4), ('sensya2', 1, 2, 5)]


def b(a):

    return a[1] + a[2] + a[3]


print(b(a[0]))

# アンパック代入
a = 1
b = 2
b, a = a, b
print(a, b)

# スライスのステップ数
a = [1, 2, 3, 4, 5]
print(a[1:4])
print(a[2: 100])
print(a[::2])

# set型のメソッドを使う
S = {1, 1, 2, 3, 4, 5}
S2 = {1, 2, 6, 6, 7, 8, 9}
print(S.union(S2))
print(S.intersection(S2))

# dict型を使いこなす
dic = {'one': 1, 'two': 2}
dic2 = {'three': 1, 'four': 2}

dic.update(dic2)
print(dic)
print(dic.keys())
if dic:
    print("pythonは長さ>０だったらtureらしいよ〜")

zero = 0
if zero:
    print("表示されない")
else:
    print("表示される")

for i in range(10, 21, 2):
    print(i)


# zip関数
for n, w in zip({1, 2, 3, 4}, {"a", "b", 'c', 'd'}):
    print(n, w)
"""


# f = open('memo.md', "r", encoding='utf-8')
# for line in f:
#     print(line, end='')

s = '書き込めたぜ！'
# f = open('memo.md', 'w', encoding='utf-8')
# f.write(s)
# f.close()

# open()
# f = open("./memo.md", 'r', encoding='utf-8')
# s = f.read()
# print(s)
# f.close()

# f = open("./memo.md", 'a', encoding='utf-8')
# s = f.write("書き込み成功！")
# print(s)
# f.close()

f = open("./memo.md", 'r', encoding='utf-8')
for line in f:
    print(line, end='')

