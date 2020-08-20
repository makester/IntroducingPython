#4.8ジェネレータ
#内包表記で間に合わないジェネレータを作るときジェネレータ関数を使う
#returnの代わりにyieldを使う以外は普通の関数と同じ
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

