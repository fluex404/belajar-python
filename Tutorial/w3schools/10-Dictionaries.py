thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

#access item
print(thisdict["model"])

thisdict['color'] = 'red'
print(thisdict)

thisdict['color'] = 'blak'
print(thisdict, type(thisdict))

thisdict = dict(name='isa', email='isa@gmail.com')
print(thisdict)

thisdict.get