#4.7関数
#4.7.1位置引数
def menu(wine,entree,dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

menu('chaldonnay','checken','cake')
#関数を使う側が引数を与える順番を覚えておいて実行する必要がある

#4.7.2キーワード引数
#関数定義時のパラメータの順序とは関係なく引数を指定できる
menu(entree='beef',dessert='bagel',wine='bordeaux')

#位置引数とキーワード引数を併用できるが、先に位置引数を与える必要がある
menu('frontenac', dessert='flan',entree='fish')
#引数を与えた順番ではなく、関数定義時の順番で値は返ってくる

#4.7.3デフォルト引数値の指定
def menu2(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

menu2('chardonnay','chicken')

#4.7.4*による位置引数のタプル化
#宣言時のパラメータの一部にアスタリスクを使うと可変個のいち引数をタプルにまとめることができる
def print_args(*args):
    print('Positional argument tuple:', args)

print_args()
print_args(3,3,1,4,'test','te')

#可変個の実引数を受け付けるが、必須の位置引数もある関数を作る時に役にたつ

def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')

#4.5.4 **によるキーワード引数の辞書化
#**で関数宣言時のキーワード引数を1個の辞書にまとめることができる
def print_kwarg(**kwargs):
    print('keyword argments:', kwargs)

print_kwarg(winr='merlot', entree='mutton', dessert='macaroon')

#4.7.6 docstring
#関数本体の先頭に文字列を組み込みドキュメントをつけることができる
#これを"docstring"と呼ぶ

def echo(anything):
    'echoは、与えられた引数を返す'
    return anything

#help()関数で呼び出しているのが関数のdocstring
#整形前のdocstringsはprint(関数名.__doc__)で表示できる

#4.7.7一人前のオブジェクトとしての関数
def answer():
    print(42)

def run_somethihg(func):
    func()

run_somethihg(answer)
#answer()ではなく括弧なしanswerを渡した点に注目
#Pythonは括弧のない関数を他のオブジェクトと同様に扱う
type(run_somethihg)

def sum_args(*args):
    return sum(args)

def run_with_positional_args(func, *args):
    return func(*args)

run_with_positional_args(sum_args, 1, 2, 3, 4)

#4.7.8関数内関数
#関数を他の関数の中で定義できる
#中の関数に別の値を与えて連続実行したりできる
def knight(sayiing):
    def inner(quote):
        return "We are the knight who say: '%s'" % quote #quoteをstrにして%sの位置に代入
    return inner(sayiing)

knight('Ni!')

#4.7.9クロージャ
def knight2(saying):
    def inner2():
        return "We are the knight who say: '%s'" % saying #innnerがKnight2に与えた引数を覚えている
    return inner2

a = knight2('Duck')
b = knight2('Hasenprefeer')

type(a)
type(b)

a()
b()

#4.7.10 無名関数：ラムダ関数

def edit_story(words, func):
    for word in words:
        print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']

def enliven(word): #これをedit_storyのfuncにする
    return word.capitalize() + '!'

edit_story(stairs,enliven)

#enliven部分をラムダで実装する

edit_story(stairs, lambda word: word.capitalize() + '!!!!')





