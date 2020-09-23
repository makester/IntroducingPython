#3-1
year_list = [1981,1982,1983,1984,1985]

#3-2
year_list[3]

#3-3
year_list[-1:]

#3-4
things = ["mozzarella","cinderella","salmonella"]

#3-5
things[1].capitalize()

#3-6
things[0].upper()

#3-7
things.pop()
things
#別解
#things.remove("salmonella")
#del things[2]

#3-8
surprise = ["Groucho","Chico","Harpo"]

#3-9
surprise[-1].lower()[::-1].capitalize()

#3-10
e2f = {
    "dog" : "chine",
    "cat" : "chat",
    "walrus" :"morse"
}

#3-11
e2f['walrus']

#3-12
f2e = {}
for English , French in e2f.items():
    f2e[French] = English

#3-13
f2e["chine"]

#3-14
set(e2f.keys())

#3-15
life = {
    'animals':{
        'cat':[
            'Henri','Grumpy','Lucy'
            ],
        'octop':{},
        'emus':{},
    },
    'plants':{},
    'other':{}
}

#3-16
life.keys()

#3-17
life['animals'].keys()

#3-18
life['animals']['cat']