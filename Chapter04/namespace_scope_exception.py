#4.10名前空間とスコープ
animal = 'fruitbat'
def print_global():
    print('inside print_global:', animal)

print('at the top level:', animal)
print_global()

# #関数内でグローバル変数を更新するとエラーが起きることを確認
# def change_and_print_global():
#     print('inside change_and_print_global:', animal)
#     animal = 'wombat'
#     print('after the change:', animal)

# change_and_print_global()

#関数内の変数をグローバル名前空間では扱えないことの確認
animal = 'fruitbat'
def change_local():
    animal = 'wombat'
    print('inside change_local:', animal, id(animal))

change_local()
animal
id(animal)

#関数内からグローバル変数にアクセスするためにglobalキーワードを使って宣言する
animal = 'fruitbat'
def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)

animal
change_and_print_global()
animal

#グローバル/ローカルの名前空間の内容を確認してみる
animal = 'fruitsbat'
def change_local2():
    animal = 'wambat' #ローカル変数
    print('locals:', locals())

animal
change_local2()
print('globals:', globals())