#4.11エラー処理とtry,excpt

# 例外が起きそうなところにはすべて例外処理を追加して、
# ユーザに何が起きているのかを知らせておくことは
# グッドプラクティスだとされている。
# 問題を解決できないかもしれないが、
# 少なくとも状況をしらせて穏便にプログラムを終了させることはできる。

# ある関数で例外がおき、その関数で例外をキャッチしなければ、
# 上位の関数の対応するハンドラがキャッシするまで例外はバブルアップしていく。

#tryを使って例外が起きそうな場所を囲み、
#exceptを使って例外処理を提供するべきた

short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print('Need a position between 0 and', len(short_list)-1, 
    ' but got', position)

#例外のタイプを特定してexcept文を書く

short_list = [1, 2, 3]
while True:
    value = input('Position [q to quite]? ')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index:', position)
    except Exception as other:
        print('Something else broke:', other)

    #4.12独自例外の作成→クラスについて勉強した後
