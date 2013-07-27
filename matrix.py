#!/usr/bin/env python
# -*- coding: utf-8 -*-

from vector import ColumnVector, RowVector, VectorLengthError

class Matrix(object):
    def __init__(self, vectors=None, nRows=None, nColumns=None):
        if vectors is not None:
            vector_length = len(vectors[0])
            vector_type = type(vectors[0]) 
            if vector_type is not RowVector \
               and vector_type is not ColumnVector \
               and vector_type is not list \
               and vector_type is not tuple: 
                raise TypeError
            for vector in vectors:
                if type(vector) != vector_type:
                    raise TypeError
                if len(vector) != vector_length:
                    raise VectorLengthError
            if vector_type is RowVector:
                self._rowVectors = vectors
            elif vector_type is ColumnVector:
                self._rowVectors = self._changeVectorType(vectors, RowVector)
            else:
                self._rowVectors = []
                for vector in vectors:
                    self._rowVectors.append(RowVector(vector))
        elif nRows is not int and nColumns is not int:
                self._rowVectors = [RowVector([0]*nColumns)]*nRows
        else:
            raise TypeError
    def __str__(self):
        string = ''
        for index, row in enumerate(self._rowVectors):
            for element in row:
                string += str(element) + ' '
            if index < len(self._rowVectors) - 1:
                string += '\n'        
        return string
    def __repr__(self):
        string = 'Matrix('
        indent = ' '*len(string)
        for index, row in enumerate(self._rowVectors):
            if index > 0:
                string += indent
            for i, element in enumerate(row):
                string += str(element)
                if i < len(row) - 1:
                    string += ' '
            if index < len(self._rowVectors) - 1:
                string += '\n'        
            else:
                string += ')'
        return string
    def __iadd__(self, other):
        for i in range(self.nRows()):
            self._rowVectors[i] += other._rowVectors[i]
        return self
    def __add__(self, other):
        new_matrix = Matrix(self.nColumns(),self.nRows())
        for i in range(self.nRows()):
            new_matrix._rowVectors[i] = self._rowVectors[i] + other._rowVectors[i]
        return new_matrix
    def __isub__(self, other):
        for i in range(self.nRows()):
            self._rowVectors[i] -= other._rowVectors[i]
        return self
    def __sub__(self, other):
        new_matrix = Matrix(self.nColumns(),self.nRows())
        for i in range(self.nRows()):
            new_matrix._rowVectors[i] = self._rowVectors[i] - other._rowVectors[i]
        return new_matrix
    def __imul__(self, other):
        new_matrix = Matrix(self.nColumns(),self.nRows())
    def __iter__(self):
        for row in self._rowVectors:
            for element in row:
                yield element
    def __getitem__(self, key):
        return self._rowVectors[key]
    def nRows(self):
        return len(self._rowVectors)
    def nColumns(self):
        return len(self._rowVectors[0])
    def _changeVectorType(self, vectors, newType):
        if newType is not RowVector and newType is not ColumnVector:
            raise TypeError
        new_vectors = []
        j = 0
        for i in range(len(vectors)):
            new_vector = []
            for vector in vectors:
                new_vector.append(vector[j])
            j += 1
            new_vectors.append(newType(new_vector))
        return new_vectors

r1 = RowVector((1, 2, 3))
r2 = RowVector((2, 3, 4))
r3 = RowVector((3, 4, 5))

c1 = ColumnVector((1, 2, 3))
c2 = ColumnVector((2, 3, 4))
c3 = ColumnVector((3, 4, 5))

m1 = Matrix([r1,r2,r3])
m2 = Matrix([c1,c2,c3])
