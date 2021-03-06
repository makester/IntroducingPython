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

#5.5.3 OrderdDict()によるキー順のソート
quotes = {
    'Moe': 'A wise guy, huh?',
    'Curly': 'Nyuk nyuk!',
    'Larry': 'Ow!',

}
for stooge in quotes:
    print(stooge)
#環境依存なのかこのコードはkeyを順番どおりに返してくる

#キーが追加された順番を覚えておいて追加された順序にキーを返す
#イテレータになれる辞書は"OrderDict()"で作成できる
#ここではタプルのリストから辞書を作成している

from collections import OrderedDict
quotes = OrderedDict([('Moe', 'Awaise guy, huh?'),
                      ('Larry', 'Ow!'),
                      ('Curry', 'Nyku nyuk!'),
                      ])
for stooge in quotes:
    print(stooge)

#5.5.4 スタック+キュー=デック
#両端から要素を追加削除できるキューとスタックの要素を組みあせたのがデック
#このコードは単語の両端から文字を処理して回文かどうかをチェックするコード
def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
        return True

palindrome('a')
palindrome('racecar')
palindrome('')
palindrome('radar')
palindrome('halibut')

#スライスを使った効率的な回文チェッカー
def another_palindrome(word):
    return word == word[::-1]

another_palindrome('a')
another_palindrome('racecar')
another_palindrome('')
another_palindrome('radar')
another_palindrome('halibut')

#5.5.5 itertoolsによるコード構造の反復処理
#itertoolsには特別な反復処理の関数が使える

#itertools.chain
#引数全体をひとつのイテラブルのように扱う
import itertools
for item in itertools.chain([1,2], ['a', 'b']):
    print(item)

#itertools.cycle
#引数から循環的に要素を取り出す無限反復子
import itertools
for item in itertools.cycle(['a', 'b', 'c']):
    print(item)

#itertools.accumulate
#要素間を足したり掛けたりしつつ値を返す
import itertools
for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)

#accumulateは第二引数で2数値間の算出方法を指定できる
import itertools
def multiply(a, b):
    return a * b

for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)

#5.5.6 pprint()によるきれいな表示

from collections import OrderedDict
from pprint import pprint
quotes = OrderedDict([('Moe', 'Awaise guy, huh?'),
                      ('Larry', 'Ow!'),
                      ('Curry', 'Nyku nyuk!'),
                      ])
print(quotes)
pprint(quotes)