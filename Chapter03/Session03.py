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