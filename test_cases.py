from matrixMult import *

a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,2,3],[1,2,5],[3,4,7]]
c = [[1,2,3],[4,5,6],[7,8,9],[4,2,3]]
d = [[1,2,3],[1,2,5],[3,4,7]]
x = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
y = [[1,2],[1,2],[3,4]]

def test_all():
    assert multiplyMatrices(a,b) == [[12, 18, 34], [27, 42, 79], [42, 66, 124]]
    assert multiplyMatrices(c,d) == [[12, 18, 34], [27, 42, 79], [42, 66, 124], [15, 24, 43]]
    assert multiplyMatrices(x,y) == [[12, 18], [27, 42], [42, 66], [57, 90]]
    