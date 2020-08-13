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