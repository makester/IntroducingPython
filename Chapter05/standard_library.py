#5.5.1 setdefault()とdefaultdict()による存在しないキーの処理
periodic_table = {'Hydorogen': 1, 'Helium': 2}
print(periodic_table)

carbon = periodic_table.setdefault('Carbon', 12)
#辞書に値がなければ上記の値が追加される
carbon

helium = periodic_table.setdefault('Helium', 947)
#既に値があるものにsetdefaultで値を追加しようとしても変更できない
helium

periodic_table

#defaultdict()は辞書作成時に指定されたキーに勝手に入るデフォルトバリューを設定する
from collections import defaultdict
periodic_table = defaultdict(int)

periodic_table['hoge']
periodic_table['huga']
periodic_table['piyo'] = 5
periodic_table

#defaultdictの使い方の例
from collections import defaultdict

def no_idea():
    return '知らんがな'

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable snowman'
bestiary['B'] = 'basilisk'
bestiary['A']
bestiary['B']
bestiary['C']

#defaultdictの便利な使い方の例
#int(),list(),dict()を引数なしで与えて空の値をデフォルト値にする
#Lambdaを使って値を与える

Lambda_dict = defaultdict(lambda : 'Lambda is cool')
Lambda_dict['A'] = "inserted value"

Lambda_dict['A']
Lambda_dict['B']

#5.5.2Counter()による要素数の計算
from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
breakfast_counter

#most_common()関数はすべての要素を降順で返す。引数で要素数指定
breakfast_counter.most_common()
breakfast_counter.most_common(1)

#Counterを使った結合
breakfast = ['spam', 'spam', 'eggs', 'spam']
lunch = ['eggs', 'eggs', 'bacon']
breakfast_counter = Counter(breakfast)
lunch_counter = Counter(lunch)

breakfast_counter
lunch_counter

breakfast_counter + lunch_counter #加算結合
breakfast_counter - lunch_counter #朝食にあって昼食にない
lunch_counter - breakfast_counter #昼食にあって朝食にない
breakfast_counter & lunch_counter #両方にある
breakfast_counter | lunch_counter #全部組み合わせると..