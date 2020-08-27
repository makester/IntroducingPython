#4-1
guess_me = 7
if guess_me < 7:
    print('too low')
elif guess_me > 7:
    print('too high')
else:
    print('just it')

#4-1(追加)
a = 3
if a == 1:
    print(1)
elif a > 1:
    print(a)
else:
    print('small')

# 上記のコードは両者ともインタラクティブシェルに直接入力だと
# 上手く動くのだがファイルに記載する場合は上手く動かない
# elif文のところをコメントアウトすると動く
# elif文の部分にvscodeのこの機能を使った時の環境依存の何かがある？

#4-2
guess_me = 7
start = 1
while True:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('find it')
    elif start > guess_me:
        print('oops')
        break
    start += 1
#ここではelifを使っても上手くいく。4-1のエラーはなんだろう？

#4-3
for i in range(0,4):
    print(i)