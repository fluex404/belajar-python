import re


txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
print(re.findall("^The.*in$", txt))
print(re.search("^The.*in$", txt))
print(re.split(' ',txt))
print(re.sub(' ', '#',txt))




member_aneh = ["dr mute stev", "ikbbalm", "pace de rune", "linuk", ":v"]

