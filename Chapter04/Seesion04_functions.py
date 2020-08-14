#4.6内包表記
#4.6.1リスト内包表記

#1~5までを格納するリストをrangeをリテラブルに内包表記で生成してください

number_list = [number for number in range(1,6)]

#1~5までの奇数だけのリストをrangeでイテラブルを生成し内包表記で生成してください

odd_number_list = [number for number in range(1,6) if number %2 == 1]
odd_number_list

#リスト内包表記のネストの実験
#内包表記を使わない書き方
rows = range(1,4)
cols = range(1,3)
for row in rows:
    for col in cols:
        print(row,col)

#内包表記のネストを使った書き方
rows = range(1,4)
cols = range(1,3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

#4.6.2辞書内括表記
word = 'letter'
letter_count = {text: word.count(text) for text in word}
letter_count

#4.6.3集合内包表記
a_set = {number for number in range(1,6) if number % 3 == 1}
a_set

#4.6.4ジェネレータ内包表記
number_things = (number for number in range(1,6))
type(number_things)

#ジェネレータを使ってみる
for number in number_things:
    print(number)

#ジェネレータが一度しか使えないことの確認
number_list = list(number_things)
number_list