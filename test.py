from pydmtx import DataMatrix
from PIL import Image

# Write a Data Matrix barcode
dm_write = DataMatrix()
dm_write.encode("Hello, world!")
dm_write.save("hello.png", "png")

# Read a Data Matrix barcode
dm_read = DataMatrix()
img = Image.open("hello.png")

print dm_read.decode(img.size[0], img.size[1], buffer(img.tostring()))
print dm_read.count()
print dm_read.message(1)
print dm_read.stats(1)


# Invalid input value
dm_invalid = DataMatrix(
    module_size=2,
    scheme=DataMatrix.DmtxSchemeC40,
    shape=DataMatrix.DmtxSymbol44x44
)
INVALID_VALUE = (
    u'JGB 6208620D02442190000000098351600   1230516230516MTA01  '
    'RS258658803GB    DEAD REI I SOFTBANK JP             NANIWAKUSITADERA2-1-'
    '1704  JP IG103TR  IG103TR  S                                             '
    '                  '
)
try:
    dm_invalid.encode(INVALID_VALUE)
except ValueError, ex:
    assert ex.message == 'Failed to encode input string.'
else:
    assert "Should not happen"
