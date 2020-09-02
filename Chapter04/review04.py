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

#4-4
even_list = [number for number in range(10) if number % 2 == 0]
print(even_list)

#4-5
squares = {item:item*item for item in range(10)}
squares

#4-6
odd = {num for num in range(10) if num % 2 != 0}
print(odd)

#4-7
for thing in ('Got %s' % number for number in range(10)):
    print(thing)

#4-8(my first code)
def good():
    potter = ['Harry', 'Ron', 'Hermione']
    return potter

PotterOutPut = good()
PotterOutPut
#4-8(textcode)
def good_text():
    return ['Harry', 'Ron', 'Hermione']
good_text()

#4-9(自分コード)

def get_odd():
    return (number for number in range(10) if number %2 ==1 )

#4-9(テキストコード)
#奇数を返すget_oddsというジェネレータ関数を定義しよう。
#またforループを使って3番目の値を見つけて表示しよう

def get_odds():
    for number in range(1, 10, 2):
        yield number

for count, number in enumerate(get_odds(), 1):
    if count == 3:
        print("The third odd number is", number)
        break

#4-10(まったくわからない)
#関数が呼び出された時にStart,終了したときにEndと表示するtestというデコレータ
def test(func):
    def new_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_func

#デコレータは定義してShift + Enterではそのままは呼べない？←呼べない

@test
def greeting():
    print("greetings,Erthling")

greeting()

#4-11(クラスを知らないのでもう一度)
try:
    num_list = [1, 2, 3]
    num_list[4]
except :
    print('Caught an oops')

#4-12(できなかった)
title = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun into a monster', 'A haunted yarn shop']
#ここからできない
movies = dict(zip(title, plots))
movies