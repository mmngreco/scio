import logging
from time import sleep


# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)




def heavy_task():
    sleep(5)
    return 5


class LazyfyStr(object):
    __slots__ = 'fn', 'args'

    def __init__(self, fn, *args):
        self.fn = fn
        self.args = args

    def __str__(self):
        return str(self.fn(*self.args))


def main():

    for i in range(3):
        logging.info("%s", i)
        # logging.debug("%s", heavy_task())
        logging.debug("%s", LazyfyStr(heavy_task))


if __name__ == "__main__":
    main()
