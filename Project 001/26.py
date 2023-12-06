def abc():
    pass


def b1(a):
    pass

def b2(a: int) -> None:
    pass


# def c1(a, b=77, c='HELLO', d='AAAA', zzzz=None, www=[], qqq={}): # PLEASE NOT APPLY for www=[], qqq={}

def c1(a, b=77, c='HELLO', d='AAAA', zzzz=None):
    if zzzz is None:
        print('NONEEEEEEE')

    if not bool(zzzz):
        print('NONE')

    print('c: [{}] d: [{}] b:[{}]'.format(c, d, b))


def c2(*args, **kwargs):
    print('args 0 {} ..... kwargs zzzz {}'.format(args[0], kwargs['zzzz']))
    pass



if __name__ == '__main__':
    c1(33, 88, zzzz=None, c='CCCCCC')
    print('--------------')
    c1(55,  d='HAHHA', b='BBBBBBBB')
    c2('################', zzzz=8888)