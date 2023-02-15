from collections import namedtuple

Point = namedtuple('Point', 'x,y')
print(type(Point))

pt = Point(-1,2)
print(pt.x)
print(pt.y)
