'''
[+] Count the number of times the digit k appears in all non-negative integers less than or equal to a given integer n.

ex: n=12, k=2 --> answer: 2
    [ once in 2 + once in 12, zero times in all other n from 1 to 12 ]

'''


def count_slow_but_obvious(n=124, k=1):
    ans = 0
    d = '%d' % k  # as digit
    for m in range(1, n+1):
        mstr = '%d' % m
        ans += mstr.count(d)
    return ans

def show_slow(n=7593, k=3):
    print('>>> %d in 0 --> %d:  %d times' % (k, n, count_slow_but_obvious(n, k)))

# if measured/tried --> too slow

#-| In [56]: foo(7593824, 3)   --> good test case
#-| 5597988
#-| ... foo() ran for: 2.9460 seconds --> do NOT go over millions with this...
#-| [ on aaea ]

# ============================================================================ +

plan = '''
will represent numbers as seq/list of digits as written and use darn recursion
to reduce nnss, ex:

    nl = [5, 0, 2, 7] for 5027  [number-list is the name-hint, if interested!]
'''

def num(nl): # back from nl -> int format for the number
    return eval(''.join([str(d) for d in nl]))

def red(nl): # cut-out leading 0's, until at most 1 stays if in digits' place
    while len(nl) > 1 and nl[0] == 0:
        nl = nl[1:]
    return nl


def foo4(n=124, k=1):
    acc = dict() # already-computed-counts (all for the same k, only n is different)
    def cnt(nl, k): # the tool doing the counting on nl-format input
        if len(nl) == 1:
            return 0 if nl[0] < k else 1
        else:
            if nl in acc.keys():
                return acc[nl]
            td = nl[0]  # top-digit, td != 0
            n10 = eval('1' + '0'*(len(nl)-1)) # [5, 0, 2, 7] --> p10 = [1, 0, 0, 0]
            p99 = tuple([9]*(len(nl)-1))       # ...         --> p99 =    [9, 9, 9]
            rnl = red(nl[1:])           # what's left after split: 5000 + 27
            acc[p99] = cnt(p99, k) # never compute
            acc[rnl] = cnt(rnl, k) # these again!!!
            return \
                td * acc[p99]  + \
                ( n10 if k < td else (num(rnl) + 1) if k == td else 0 ) + \
                acc[rnl]

    znl = tuple([int(d) for d in '%d' % n]) # n --> nl representation
    return cnt(znl, k)

def show4(n=7593824, k=3):
    print('<v4>: %d in 0 --> %d:  %d times' % (k, n, foo4(n, k)))


# --> run a crazy-large number:
show4(1234567891011121314151617181920, k=3)   # --> 0.0009s ... awesome!

