import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
#m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input())
#m = re.findall(r"[%s]([%s]{2,})[?=%s]" % (c, v, c), input())
print(*m)


#lookahead and lookbehind are called lookarounds
'''
(?!) - negative lookahead
(?=) - positive lookahead
(?<=) - positive lookbehind
(?<!) - negative lookbehind

https://stackoverflow.com/questions/2973436/regex-lookahead-lookbehind-and-atomic-groups

https://www.rexegg.com/regex-disambiguation.html#lookarounds
'''
