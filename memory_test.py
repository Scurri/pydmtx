import random
import pydmtx
from time import sleep
from cStringIO import StringIO


def gen():
    dm = pydmtx.DataMatrix(
        module_size=2,
        scheme=pydmtx.DataMatrix.DmtxSchemeC40,
        shape=pydmtx.DataMatrix.DmtxSymbol44x44)
    def empty(*args, **kwargs):
        pass
    # dm._start = dm._plot = empty
    dm.encode("".join([str(random.randint(0, 100)) for _ in range(100)]))
    image = StringIO()
    dm.save(image, 'PNG')


if __name__ == '__main__':
    counter = 0
    while True:
        gen()
        sleep(0.2)
        counter += 1
        if counter % 1000 == 0:
            print counter