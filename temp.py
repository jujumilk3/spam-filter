from tests import is_spam

# spam cases
# depth1 spam
assert is_spam('asdw https://goo.gl/88srfV', ['pearsoncmg.com'], 1)
# depth2 spam
assert is_spam('asdw https://goo.gl/88srfV', ['support'], 2)
# depth3 spam
assert is_spam('asdw https://goo.gl/88srfV', ['pearson'], 3)
# find from html element
assert is_spam('asdw https://goo.gl/88srfV', ['accessibility'], 1)
# many addresses at content
assert is_spam('asdw https://goo.gl/88srfV http://bit.ly/silly', ['pearsoncmg.com'], 1)

# no spam cases
# depth1 no spam
assert is_spam('asdw https://goo.gl/88srfV', ['nospam'], 1) == False
# depth2 no spam
assert is_spam('asdw https://goo.gl/88srfV', ['nospam'], 2) == False
# many addresses and expired redirection
assert is_spam('asdw https://goo.gl/88srfV http://bit.ly/silly', ['pass', 'obvsy.com'], 1) == False
# many addresses and depth
assert is_spam('asdw https://goo.gl/88srfV http://bit.ly/silly', ['pass', 'obvsy.com'], 2) == False
