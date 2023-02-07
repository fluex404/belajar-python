# import re
#
# print("Hallo World")
#
# txt = "Coding Bareng Cuyy"
# x = re.search("^Coding.*Cuyy$", txt)
#
# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")

try:
    x=10/''
    print(x)
except Exception as ex:
    print(str(ex))