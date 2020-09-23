#3.5.3 in を使った値の有無のテスト

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua','vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

for name, contents in drinks.items(): #どのカクテルに'vodka'が入っているか集合を利用して確認する
    if 'vodka' in contents:
        print(name)

 #どのカクテルに'vodka'が入っているが、'vermouth'と'cream'は入ってないもの
for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        #ここのif文の条件処理部分が重要！！
        print(name)

#'orange juice'かvermouth'の入ったカクテルを探したい →　積和集合演算
for name, contents in drinks.items():
    if contents & {'orange juice','vermouth'}:
        #ここの積和集合の指定が重要
        print(name)


#同じ処理を書き方を違う書き方で
for name, contents in drinks.items():
    if ('orange juice' in contents) or ('vermouth' in contents):
        print(name)

#'vodka'はあって'vermouth'と'ceam'のないもの
for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'cream','vermouth'}:
        print(name)

bruss = drinks['black russian']
wruss = drinks['white russian']

drinks

#集合演算の演算子

a = {1, 2}
b = {2, 3}

#積集合
a & b

a.intersection(b)

#和集合
a | b

a.union(b)

#差集合
a - b
b - a

a.difference(b)
b.difference(a)

#排他的OR(NOR)
a ^ b

a.symmetric_difference(b)

#部分集合(片方の集合がもう片方の集合の部分集合になっているか？)
#つまり、一方が一方のサブセットになっているかのCHECK

bruss.issubset(wruss)

bruss <= wruss

#第一の集合が第二の集合の真部分集合になるためには、第二集合は第一の集合の
#すべての要素に加えて別の要素をもっていなければならない。

bruss < wruss

#部分集合演算子のイメージ
# <=  ←口の開いた方が大きいベン図:部分集合
# <　:真部分集合

#上位集合(スーパーセット)
wruss.issuperset(bruss)
wruss > bruss