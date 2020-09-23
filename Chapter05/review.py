#5-5
plain = {
    'a': 1,
    'b': 2,
    'c': 3,
    }
plain

from collections import OrderedDict
fancy = OrderedDict(plain)
fancy

#5-6
from collections import defaultdict
dict_of_lists = defaultdict(list)      #関数を実行系ではくオブジェクトとしてあたえる
dict_of_lists['a'] = 'something for a'

dict_of_lists['a']
dict_of_lists['b']
dict_of_lists['c']