#4.3 if,elif,elseによる比較はAnkiに記入
# コードなし、比較演算子とブール演算子についてまとめた

#4.4 whileによる反復処理
#4.4.1 breakによるループ中止
while True:
    stuff = input("string to capitalize [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())

#4.4.2 continueによる次のイテレーションの開始
#偶数なら何もせず次のイテレーションに送り、奇数なら自乗して次のイテレーションへ
while True:
    value = input("整数を入力してください ['q'をタイプすると終了します]: ")
    if value == "q":
        break
    number = int(value)
    if number % 2 == 0:
        continue #次のイテレーションに送る
    print(number, "自乗は", number * number)

#4.4.3 elseによるbreakのチェック
#whileループで何かを探し見つかったらbreak、見つからなかったらelseに渡して判定
numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print("偶数を見つけました",number)
        break
    position += 1
else: #breakが呼び出されていない
    print("偶数は見つかりませんでした")