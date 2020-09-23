def get_description():
    """プロと同じようにランダムな天気を返す"""
    from random import choice #関数定義の中でモジュールインポート
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities) #関数の中にchoiceがないことがわかっているのでモジュール前置修飾なしでchoceを呼び出している