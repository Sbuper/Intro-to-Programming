__author__ = 'Andrew'
class Horse :


    def getValue(self) :
        return self._value

    def advance(self) :
        self._value = self._value +1

    def slow_down(self) :
        self._value = self._value -2

    def reset(self) :
        self._value = 0
        
    def get_name(self) :
        self._name = "Bob"

    def whip_it(self) :
        self._value = self._value*3