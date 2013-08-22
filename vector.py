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
