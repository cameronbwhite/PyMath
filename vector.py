#!/usr/bin/env python
# -*- coding: utf-8 -*-
from numbers import Number
from functools import reduce

class Vector(object):
    def __init__(self, element):
        if isinstance(element, Vector):
            self._elements = element.elements
        elif isinstance(element, list):
            self._elements = element
        elif isinstance(element, Number):
            self._elements = [0]*element
        else:
            self._elements = list(element)

    def __repr__(self):
        return 'Vector' + '('\
                + str(reduce(lambda x, y: str(x) + ', ' + str(y), self._elements))\
                + ')'

    def __str__(self):
        return '[' \
                + str(reduce(lambda x, y: str(x) + ', ' + str(y), self._elements))\
                + ']'

    def __add__(self, other):
        self._lengthCheck(other)
        new = Vector(len(self))
        for x,y,z in zip(new, self, other):
            x = y + z
        return new

    def __iadd__(self, other):
        self._lengthCheck(other)
        for x,y in zip(self, other):
            x += y
        return self

    def __sub__(self, other):
        self._lengthCheck(len(other))
        new = Vector(len(self))
        for x,y,z in zip(new, self, other):
            x = y - z
        return new

    def __isub__(self, other):
        self._lengthCheck(len(other))
        for x,y in zip(self, other):
            x -= y
        return self

    def __iter__(self):
        for element in self._elements:
            yield element

    def __setitem__(self, index, value):
        self._elements[index] = value

    def __getitem__(self, index):
        return self._elements[index]

    def __len__(self):
        return len(self._elements)

    def __abs__(self):
         return self.dot(self)

    def dot(self, other):
        self._lengthCheck(len(other))
        return reduce(lambda x, y: x+y, map(lambda x, y: x*y, self, other))

    def _lengthCheck(self, other):
        if len(self) != len(other):
            raise VectorLengthError

class VectorLengthError(Exception):
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)
