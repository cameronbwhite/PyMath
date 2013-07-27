#!/usr/bin/env python
# -*- coding: utf-8 -*-
from numbers import Number

class Vector(object):
    def __init__(self, element):
        if isinstance(element, Vector):
            self.elements = element.elements
        else:
            try:
                self.elements = list(element)
            except:
                self.elements = [element]
    def __repr__(self):
        return 'Vector' + '('\
                + str(reduce(lambda x, y: str(x) + ', ' + str(y), self.elements))\
                + ')'
    def __str__(self):
        return '[' \
                + str(reduce(lambda x, y: str(x) + ', ' + str(y), self.elements))\
                + ']'
    def __add__(self, other):
        self._vectorTypeCheck(type(other))
        self._lengthCheck(len(other))
        length = len(self)
        new_vector = self._new_vector(type(self), length)
        for i in range(length):
             new_vector[i] = self[i] + other[i]
        return new_vector
    def __iadd__(self, other):
        self._vectorTypeCheck(type(other))
        self._lengthCheck(len(other))
        length = len(self)
        for i in range(length):
             self[i] += other[i]
        return self
    def __sub__(self, other):
        self._vectorTypeCheck(type(other))
        self._lengthCheck(len(other))
        length = len(self)
        new_vector = self._new_vector(type(self), length)
        for i in range(length):
             new_vector[i] = self[i] - other[i]
        return new_vector
    def __isub__(self, other):
        self._vectorTypeCheck(type(other))
        self._lengthCheck(len(other))
        for i in range(lenght):
            self[i] -= other[i]
        return self
    def __iter__(self):
        for element in self.elements:
            yield element
    def __setitem__(self, index, value):
        self._indexCheck(index)
        self.elements[index] = value
    def __getitem__(self, index):
        self._indexCheck(index)
        return self.elements[index]
    def __len__(self):
        return len(self.elements)
    def __abs__(self):
         return self.dot(self)
    def dot(self, other):
        self._vectorTypeCheck(type(other))
        assert type(other) == Vector
        assert len(self) == len(other)
        return reduce(lambda x, y: x+y, map(lambda x, y: x*y, self, other))
    def _indexCheck(self, index):
        if index < 0 or index >= len(self):
            raise IndexError
    def _new_vector(self, vector_type, length, element=0):
        if vector_type is RowVector or vector_type is ColumnVector:
            return vector_type([element]*length)
        else:
            raise TypeError
    def _lengthCheck(self, length1, length2=None):
        if length2 is None:
            length2 = len(self)
        if type(length1) is type(length2) is int: 
            if length1 == length2:
                return True
            else:
                raise VectorLengthError
        else:
            raise TypeError
    def _vectorTypeCheck(self, vectorType1, vectorType2=None):
        if vectorType2 is None:
            vectorType2 = type(self)
        if vectorType1 is vectorType2 is RowVector:
                return True
        elif vectorType1 is vectorType2 is ColumnVector:
                return True
        else:
            raise TypeError

class RowVector(Vector):
    def __repr__(self):
        return 'RowVector' + '('\
                + str(reduce(lambda x, y: str(x) + ', ' + str(y), self.elements)) \
                + ')'
    def __str__(self):
        return '[' \
                + str(reduce(lambda x, y: str(x) + ', ' + str(y), self.elements))\
                + ']'

class ColumnVector(Vector):
    def __repr__(self):
        return 'ColumnVector' + '('\
                + str(reduce(lambda x, y: str(x) + ', ' + str(y), self.elements))\
                + ')'
    def __str__(self):
        return '[' \
                + str(reduce(lambda x, y:  str(x) + ',\n' + ' ' + str(y), self.elements))\
                + ']'

class VectorLengthError(Exception):
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)
