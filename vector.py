# Copyright (C) 2013, Cameron White
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the project nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE PROJECT AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE PROJECT OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from numbers import Number
from functools import reduce
from math import sqrt

class Vector(object):
    """ Mathematical Vector """

    def __init__(self, value):
        """ Construct a Vector

        If value is a number the vector becomes a vector all 0 of
        that length. If the value is a list the vector will 
        contain the elements of that length with out any copying.
        Any other type for value will be converted to list if 
        possible, this will probably result in copying of data.
        Also if value is a Vector then the constructor copies.

        >>> v1 = Vector([1, 2, 3, 4, 5])
        >>> v2 = Vector([0.1, 0.2, 0.3, 0.4, 0.5])
        >>> v3 = Vector(5)

        Args:
            value: list, number, or something that can be converted 
                   to a list.
        """
        if isinstance(value, Vector):
            self._elements = value._elements
        elif isinstance(value, list):
            self._elements = value
        elif isinstance(value, Number):
            self._elements = [0]*value
        else:
            self._elements = list(value)

    def __repr__(self):
        """ Return the representation of the Vector

        >>> Vector([1,2,3])
        Vector(1, 2, 3)
        """
        return 'Vector' + '('\
                + str(reduce(lambda x, y: str(x) + ', ' + str(y), self._elements))\
                + ')'

    def __str__(self):
        """ Return the string of the Vector

        >>> print(Vector([1,2,3]))
        [1, 2, 3]
        """
        return '[' \
                + str(reduce(lambda x, y: str(x) + ', ' + str(y), self._elements))\
                + ']'

    def __add__(self, other):
        """ Add this vector to the other vector in a new vector

        >>> v1 = Vector([1, 2, 3, 4, 5])
        >>> v2 = Vector([0.1, 0.2, 0.3, 0.4, 0.5])
        >>> v1 + v2
        Vector(1.1, 2.2, 3.3, 4.4, 5.5)

        Args:
            other: The other vector

        Returns:
            The new vector.
        """
        try:
            return Vector(map(lambda a, b: a + b, self, other))
        except TypeError:
            raise VectorLengthError

    def __iadd__(self, other):
        """ Add this vector to the other vector in place.

        >>> v1 = Vector([1, 2, 3, 4, 5])
        >>> v2 = Vector([0.1, 0.2, 0.3, 0.4, 0.5])
        >>> v1 += v2
        >>> v1
        Vector(1.1, 2.2, 3.3, 4.4, 5.5)

        Args:
            other: The other vector
        """
        return self.copy(self + other)

    def __sub__(self, other):
        """ Subtract the other vector from this vector in a new vector.

        >>> v1 = Vector([1, 2, 3, 4, 5])
        >>> v2 = Vector([0.1, 0.2, 0.3, 0.4, 0.5])
        >>> v1 - v2
        Vector(0.9, 1.8, 2.7, 3.6, 4.5)

        Args:
            other: The other vector

        Returns:
            The new vector.
        """
        try:
            return Vector(map(lambda a, b: a - b, self, other))
        except TypeError:
            raise VectorLengthError

    def __isub__(self, other):
        """ Subtract the other vector from this vector in a new vector.

        >>> v1 = Vector([1, 2, 3, 4, 5])
        >>> v2 = Vector([0.1, 0.2, 0.3, 0.4, 0.5])
        >>> v1 - v2
        Vector(0.9, 1.8, 2.7, 3.6, 4.5)

        Args:
            other: The other vector
        """
        return self.copy(self - other)

    def __iter__(self):
        for element in self._elements:
            yield element

    def __setitem__(self, index, value):
        """ Set the element to the value at the index.

        >>> v1 = Vector([0, 0, 0])
        >>> v1[0] = 1
        """
        self._elements[index] = value

    def __getitem__(self, index):
        """ Get the element at the index.

        >>> v1 = Vector([1, 2, 3])
        >>> v1[0]
        1
        >>> v1[1]
        2
        """
        return self._elements[index]

    def __len__(self):
        """ Return the length of the vector.

        >>> len(Vector([1, 2, 3]))
        3
        """
        return len(self._elements)

    def __abs__(self):
        """ Return the magnitude of the Vector.

        >>> abs(Vector([1, 2, 3]))
        3.7416573867739413
        """
        return sqrt(self * self)

    def copy(self, other):
        """ Copy the elements of the other vector

        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector(0)
        >>> v2 = Vector(v1)
        >>> v2._elements is v1._elements
        True
        """
        self._elements = other._elements
        return self

    def __mul__(self, other):
        """ Return the dot product of the two vectors

        >>> Vector([1,2]) * (Vector([2, 3]))
        8
        >>> Vector([1, 2]) * 2
        Vector(2, 4)
        """
        if hasattr(other, '__iter__'):
            return reduce(lambda x, y: x+y, 
                          map(lambda x, y: x*y, self, other))
        else:
            return Vector(map(lambda x: x*other, self))

    def __imull__(self, other):
        """
        >>> v1 = Vector([1, 2])
        >>> v1 *= 2
        >>> v1
        Vector(2, 4)
        """
        if not hasattr(other, '__iter__'):
            self.copy(self * other)
        return self

class VectorLengthError(Exception):
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)

if __name__ == "__main__":
    import doctest
    doctest.testmod()