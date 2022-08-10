#function for areof a circle

from xml.etree.ElementTree import PI

PI = 22/7
def areaCircle(radius):
    area = PI * (radius * radius)
    print('Area of a circle is = ' + str(area))

areaCircle(30)