from inspect import getgeneratorstate


def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


class UserEventException(Exception):
    pass


@coroutine
def send_gen():
    x = 'Ready to accept message'
    message = yield x
    print('Subgen received: ', message)


@coroutine
def average():
    count = 0
    summ = 0
    average_ = None

    while True:
        try:
            x = yield average_
        except StopIteration:
            print('Done!')
            break
        else:
            count += 1
            summ += x
            average_ = round(summ / count, 2)

    return average_


# @coroutine
def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            break
        except UserEventException:
            # print('Ku-ku!!')
            break
        else:
            print('.......', message)

    return 'Return from subgen()'

    # for i in 'Roman':
    #     yield i


@coroutine
def delegator(g):
    result = yield from g
    print(result)

    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except StopIteration:
    #         pass
    #     except UserEventException as e:
    #         g.throw(e)

    # for i in g:
    #     yield i


def a():
    yield from "Roman"


gyf = a()
print(next(gyf))
print(next(gyf))
print(next(gyf))

g = delegator(subgen())
g.throw(UserEventException)
# sg = subgen()
# g = delegator(sg)
# g.send('Ok')
# g.send('111Ok111')
# g.throw(StopIteration)

# g = average()
# print(getgeneratorstate(g))
