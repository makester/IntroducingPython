#4.8ジェネレータ
#内包表記で間に合わないジェネレータを作るときジェネレータ関数を使う
#returnの代わりにyieldを使う以外は普通の関数と同じ
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

#4.9 デコレータ
#入力として関数をひとつ取り、別の関数を返すのがデコレータ

#デコレータdocument_itの宣言
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

#手作業でデコレータを使ってみる
# def add_ints(a, b):
#     return a + b

# add_ints(3, 5)

# cooler_add_ints = document_it(add_ints) #手作業でデコレータの戻り値を代入
# cooler_add_ints(3, 5)

#関数に対するデコレータは複数持てる。結果を自乗するデコレータを宣言する
def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

@square_it
def add_ints(a, b):
    return a + b


