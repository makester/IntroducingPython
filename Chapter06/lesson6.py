#6.3継承
# Carというクラスを定義してからそのサブクラスYugoというサブクラスを作る


# Yugoでスーパークラスのメソッドをオーバーライドする

# class Car():
#     def exclaim(self):
#         print("I'm a Car!")

# class Yugo(Car):
#     def exclaim(self):
#         print("I'm a Yugo!")

# give_me_a_car = Car()
# give_me_a_Yugo = Yugo()

# give_me_a_car.exclaim()
# give_me_a_Yugo.exclaim()

#__init__()を含むあらゆるメソッドをオーバーライドできる
# class Person():#親クラス
#     def __init__(self, name):
#         self.name = name

# class MDPerson(Person):#子クラス1 ←　継承時親クラスを引数に与えるのを忘れない
#     def __init__(self, name):
#         self.name = "Docter" + name

# class JDPerson(Person):#子クラス2
#     def __init__(self,name):
#         self.name = name + ", Esquire"

# person = Person('Fudd')
# doctor = MDPerson('Fudd')
# lawyer = JDPerson('Fudd')
# print(person.name)
# print(doctor.name)
# print(lawyer.name)

#6.5メソッドの追加
#サブクラスにスーパークラスに存在しなかったメソッドを追加する

class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo!")
    def need_a_push(self):
        print("A little help here?")

give_me_a_car = Car()
give_me_a_Yugo = Yugo()

give_me_a_Yugo.need_a_push()
# give_me_a_car.need_a_push()

#6.6 superによる親への支援要請
class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):#サブクラスの__init__は置き換えられスーパークラスのものとは別になっている
        super().__init__(name)#superで親クラスの__init__を呼び出している
        self.email = email

#EmailPersonのクラスをインスタンス化する
bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
#bobは子クラスにしかないプロパティを使えている
bob.name
bob.email

# class EmailPerson(Person):
#     def __init__(self, name, email):
#         super().__init__(name) #superを使った定義
#         self.email = email

# class EmailPerson(Person):
#     def __init__(self, name, email):
#         self.name = name #superを使わない定義
#         self.email = email

#6.7 selfの自己弁護
car = Car()
car.exclaim()
#I'm a Car1と出力される。
#このコードの背後でPythonがやっているのは
#1.carオブジェクトのクラス(Car)を探しだす。
#2.Carクラスのexplain()メソッドにself引数(=carオブジェクト自体)を渡す

#6.8 プロパティによる属性値の取得、設定

# class Duck():
#     def __init__(self, input_name):
#         self.hidden_name = input_name
#     def get_name(self):
#         print('inside the getter')
#         return self.hidden_name
#     def set_name(self, input_name):
#         print('inside the setter')
#         self.hidden_name = input_name
#     name = property(get_name, set_name)

# fowl = Duck('Howard')
# fowl.name
#getter/setterというものがあるというところで今は我慢しておく
#このgetter/setterを使いたいときは最後のproperty()関数を書かずに
#デコレータを使って書くこともできる
#あらかじめそれようデコレータがあるようで
#@propery ←　getter
#@name.setter ← setter
#のようだ

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

fowl = Duck('Howard')
fowl.name
fowl.name = 'Donald'
fowl.name
