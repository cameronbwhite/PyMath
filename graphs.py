#!/usr/bin/env pyhton
from numbers import Number

class Point(object):
    def __init__(self, elements):
        self.elements = list(elements)
    def __repr__(self):
        return 'Point' + str(self) 
    def __str__(self):
        return '(' + reduce(lambda x, y: str(x) + ', ' + str(y), self.elements) + ')'
    def __iter__(self):
        for element in self.elements:
            yield element
    def __add__(self, other):
        assert type(other) == Point
        assert len(self) == len(other)
        new_point = Point([0]*len(self))
        for i in range(len(self)):
            new_point[i] = self[i] + other[i]
        return new_point
    def __iadd__(self, other):
        assert type(other) == Point
        assert len(self) == len(other)
        for i in range(len(self)):
            self[i] += other[i]
        return self
    def __sub__(self, other):
        assert type(other) == Point
        assert len(self) == len(other)
        new_point = Point([0]*len(self))
        for i in range(len(self)):
            new_point[i] = self[i] + other[i]
        return new_point
    def __iadd__(self, other):
        assert type(other) == Point
        assert len(self) == len(other)
        for i in range(len(self)):
            self[i] -= other[i]
        return self
    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self)
        self.elements[index] = value
    def __getitem__(self, index):
        assert index >= 0 and index < len(self)
        return self.elements[index]
    def __len__(self):
        return len(self.elements)

       
class Graph(object):
    def __init__(self, point):
        assert type(point) == Point
        self.point = point

class NormalForm(Graph):
    def __init__(self, point, normal):
        assert type(normal) == Vector
        super(NormalForm, self).__init__(point)
        self.normal = normal
    def __repr__(self):
        return 'NormalForm(' + 'point=' + str(self.point) + ', ' \
                + 'normal=' + str(self.normal) + ')'
    def __str__(self):
        return repr(self)
    def isParell(self, other):
        if type(other) == NormalForm:
            if self.normal.dot(other.normal) == \
                    abs(self.normal) == abs(other.normal):
               return True
        elif type(other) == VectorForm:
            if self.normal.dot(other.distance) == 0:
               return True
        return False
    def isPerpendicular(self, other):
        if type(other) == VectorForm:
            if self.normal.dot(other.distance) == \
                    abs(self.normal) == abs(other.distance):
               return True
        elif type(other) == NormalForm:
            if self.normal.dot(other.normal) == 0:
               return True
        return False
    def vectorForm(self):
        pass
    def parametricForm(self):
        pass
    def generalForm(self):
        pass

class VectorForm(Graph):
    def __init__(self, point, distance):
        assert type(distance) == Vector
        super(VectorForm, self).__init__(point)
        self.distance = distance
    def __repr__(self):
        return 'VectorForm(' + 'point=' + str(self.point) + ', '\
                + 'distance=' + str(self.distance) + ')'
    def __str__(self):
        return repr(self)
    def isParell(self, other):
        if type(other) == VectorForm:
            if self.distance.dot(other.distance) == \
                    abs(self.distance) == abs(other.distance):
               return True
        elif type(other) == NormalForm:
            if self.distance.dot(other.normal) == 0:
               return True
        return False
    def isPerpendicular(self, other):
        if type(other) == NormalForm:
            if self.distance.dot(other.normal) == \
                    abs(self.distance) == abs(other.normal):
               return True
        elif type(other) == VectorForm:
            if self.distance.dot(other.distance) == 0:
               return True
        return False
    def NormalForm(self):
        pass
    def parametricForm(self):
        pass
    def generalForm(self):
        pass

if __name__ == '__main__':
    P1 = Point((1, 2, 3))
    P2 = Point((4, 5, 6))
    V1 = Vector(P1)
    V2 = Vector(P2)
    normalForm = NormalForm(P1, V1)
    vectorForm = VectorForm(P2, V1)
