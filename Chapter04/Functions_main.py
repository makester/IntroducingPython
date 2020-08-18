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