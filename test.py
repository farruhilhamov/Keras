import re
while True:
    phrase = input('phrase: ')
    for i in phrase:
        if re.match(r'[A-z]{1}',phrase):
            phrase = input('phrase MUST BE IN English: ')
    try:
        res = buildPhrase(phrase)
        print(res)
    except Exception:
        print(Exception.args)