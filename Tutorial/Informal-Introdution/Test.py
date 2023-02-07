
#this is the first comment
spam = 1 # and this is the secound comment
# ... and now a third!
text = "# This is not a comment because it's inside quotes."
text2 = 'kudanil"'
print(spam)
print(text)
print(text2)

x = 42
if x < 0:
    x = 0
    print(x, 'Negative')
elif x == 0:
    print(x, 'Zero')
elif x == 1:
    print(x, 'Single')
else:
    print(x, 'More')


words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, ' : ', len(w))

users = {'Hans':'active', 'Eleonore':'inactive', 'a': 'active'}
del users['Eleonore']
for v, k in users.items():
    print(v, k)

for i in range(5):
    print(i)

l = list(range(6, 9))

for x in l:
    print(x)