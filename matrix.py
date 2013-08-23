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

from vector import Vector, VectorLengthError
from functools import reduce

class Matrix(object):
    def __init__(self, elements):
        """ Construct a Matrix

        Matrix implements a row matrix
        elements must be a list of list where each internal
        list must be the same length.

        >>> m1 = Matrix([[1.1, 1.2],\
                         [2.1, 2.2],\
                         [3.1, 3.2]])

        Args:
            elements: list of list
        """
        if isinstance(elements, Matrix):
            self._elements = elements._elements

        else:
            if not isinstance(elements, list):
                raise TypeError

            length = len(elements[0])
            for vector in elements:
                if len(vector) != length:
                    raise VectorLengthError
                if isinstance(vector, Vector):
                    vector = vector._elements
                if not isinstance(vector, list):
                    raise TypeError

            self._elements = elements

    def __str__(self):
        """ Return the string representation of the Matrix

        >>> m1 = Matrix([[1.1, 1.2],\
                         [2.1, 2.2],\
                         [3.1, 3.2]])
        >>> str(m1)
        '[[1.1, 1.2],\\n [2.1, 2.2],\\n [3.1, 3.2]]'
        >>> print(m1)
        [[1.1, 1.2],
         [2.1, 2.2],
         [3.1, 3.2]]

        """
        return '[' + reduce(lambda x, y: str(x) + ',\n ' + str(Vector(y)),
            self._elements) + ']'

    def __repr__(self):
        """ Return the representation of the Matrix

        >>> Matrix([[1.1, 1.2],\
                    [2.1, 2.2],\
                    [3.1, 3.2]])
        Matrix([[1.1, 1.2],
                [2.1, 2.2],
                [3.1, 3.2]])
        """
        prefix = 'Matrix(['
        indent = ' ' * len(prefix)
        return 'Matrix([' +\
            reduce(lambda x, y: str(x) + ',\n' + indent + str(Vector(y)),
            self._elements) + '])'

    def __add__(self, other):
        """ Add this matrix to the other matrix in a new matrix

        >>> m1 = Matrix([[1.1, 1.2], [2.1, 2.2]])
        >>> m2 = Matrix([[10.1, 10.2], [20.1, 20.2]])
        >>> m1 + m2
        Matrix([[11.2, 11.4],
                [22.2, 22.4]])
        """
        return Matrix(map(lambda x, y: Vector(x) + Vector(y), 
                          self._elements, other._elements))

    def __iadd__(self, other):
        """ Add this matrix to the other in place

        >>> m1 = Matrix([[1.1, 1.2], [2.1, 2.2]])
        >>> m2 = Matrix([[10.1, 10.2], [20.1, 20.2]])
        >>> m1 += m2
        >>> m1
        Matrix([[11.2, 11.4],
                [22.2, 22.4]])
        """
        return self.copy(self + other)

    def __sub__(self, other):
        """ Substract the other vector from this vector 

        >>> m1 = Matrix([[10.1, 10.2], [20.1, 20.2]])
        >>> m2 = Matrix([[1.1, 1.2], [2.1, 2.2]])
        >>> m1 - m2
        Matrix([[9.0, 9.0],
                [18.0, 18.0]])
        """
        return Matrix(map(lambda x, y: Vector(x) - Vector(y), 
                          self._elements, other._elements))

    def __isub__(self, other):
        """ Substract the other vector from this vector inplace

        >>> m1 = Matrix([[10.1, 10.2], [20.1, 20.2]])
        >>> m2 = Matrix([[1.1, 1.2], [2.1, 2.2]])
        >>> m1 -= m2
        >>> m1
        Matrix([[9.0, 9.0],
                [18.0, 18.0]])
        """
        return self.copy(self - other)

    def __mul__(self, other):
        if hasattr(other, '__iter__'):
            pass    # TODO
        else:
            return Matrix(map(lambda x: Vector(x) * other, 
                              self._elements))

    def __imul__(self, other):
        if not hasattr(other, '__iter__'):
            self.copy(self * other)
        return self

    def __iter__(self):
        for row in self._rowVectors:
            for element in row:
                yield element

    def __getitem__(self, index):
        """ Get an row Vector at the index

        >>> m1 = Matrix([[1.1, 1.2], [2.1, 2.2]])
        >>> m1[0]
        Vector([1.1, 1.2])
        """
        return Vector(self._elements[index])

    def __setitem__(self, index, value):
        """ Set the row Vector at the index

        >>> m1 = Matrix([[1.1, 1.2], [2.1, 2.2]])
        >>> m1[0] = Vector([10, 20])
        >>> m1[0]
        Vector([10, 20])
        >>> m1[1] = [30, 40]
        >>> m1[1]
        Vector([30, 40])
        """
        if len(value) != self.nColumns():
            raise VectorLengthError
        if isinstance(value, Vector):
            self._elements[index] = value._elements
        elif isinstance(value, list):
            self._elements[index] = value
        else:
            raise TypeError

    def copy(self, other):
        """ Copy the elements of the other matrix

        >>> m1 = Matrix([[1, 2, 3]])
        >>> m2 = Matrix([[]])
        >>> m2 = Matrix(m1)
        >>> m2._elements is m1._elements
        True
        """
        assert isinstance(other, Matrix)
        self._elements = other._elements
        return self

    def nRows(self):
        """ Return the number of rows in the matrix

        >>> Matrix([[1.1, 1.2, 1.3], [2.1, 2.2, 3.3]]).nRows()
        2
        """
        return len(self._elements)

    def nColumns(self):
        """ Return the number of columns in the matrix

        >>> Matrix([[1.1, 1.2, 1.3], [2.1, 2.2, 3.3]]).nColumns()
        3
        """
        return len(self._elements[0])

    def transpose(self):
        pass    # TODO

if __name__ == "__main__":
    import doctest
    doctest.testmod()