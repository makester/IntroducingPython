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

#4.5 forによる反復処理
#辞書系のデータからキーと値の組をfor文を使ってタプルで返す

#辞書の定義
accusation = {
    'room': 'ballroom',
    'weapon': 'lead pipe',
    'person': 'Col. Mustrad'
}
#タプルでキーとバリューと取り出す
for item in accusation.items():
    print(item)

#4.5.3 elseによるbreakのチェック
#forループが途中でbreakを呼ばずに最後まで実行されたことを確認するのに使える
cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else: #breakしてないから"cheese"はない
    print('This is not much of a cheese shop, is it?')

#4.5.4 zip()を使った複数シーケンスの反復処理
#dict()は2要素のシーケンスから辞書を作れるので、zip()で2要素のシーケンスを生成し
#それをdict()に渡すと辞書が作れる

dict(zip(range(1,10,1),range(2,20,2)))

#4.5.5 range()による数値シーケンスの生成
#rangeはイテラブルなオブジェクトを返すので、戻り値は
#for ... inで反復処理するか、リストなどのシーケンスに変換する必要がある
list(range (0, 11, 2)) #0から10までの偶数のリストを得る