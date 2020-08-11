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
        continue
    print(number, "自乗は", number * number)