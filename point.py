class Point(object):
    def __init__(self, elements):
        self.elements = list(elements)
    def __repr__(self):
        return 'Point' + str(self) 
    def __str__(self):
        return '(' + \
                reduce(lambda x, y: str(x) + ', ' + str(y), self.elements)\
                + ')'
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
