def h(char='-', repeat=80):
    """
    function to print repeat characters
    very handy to draw a horizontal line for logging purpose
    usage : h('*') default repeat = 80
    """
    import random
    sq = list('abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+[{]};:'"")
    # print char[0]*repeat
    print random.choice(sq)*repeat

h()

# h('_')
