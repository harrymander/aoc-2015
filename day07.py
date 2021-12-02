import sys


class Circuit(object):
    @staticmethod
    def and_(a, b):
        return a & b

    @staticmethod
    def or_(a, b):
        return a | b

    @staticmethod
    def not_(a):
        binrepr = f'{a:016b}'.replace('0', 'a').replace('1', 'b')
        return int(binrepr.replace('a', '1').replace('b', '0'), 2)

    @staticmethod
    def lshift(a, b):
        shifted = f'{(a << b):016b}'
        return int(shifted[-16:], 2)

    @staticmethod
    def rshift(a, b):
        return a >> b

    @staticmethod
    def pass_(a):
        return a

    class _WireOp(object):
        def __repr__(self):
            args = ', '.join(map(str, self.args))
            return f'_WireOp({self.op.__name__}({args})'

        def __init__(self, op, *args):
            self.op = op or Circuit.pass_

            self.args = []
            for arg in args:
                try:
                    arg = int(arg)
                except ValueError:
                    pass
                self.args.append(arg)

            self._original_args = self.args.copy()

        def reset(self):
            self.args = self._original_args.copy()

        def value(self, wires):
            resolved_args = []
            for arg in self.args:
                if type(arg) is str:
                    arg = wires[arg].value(wires)
                resolved_args.append(arg)

            self.args = resolved_args
            return self.op(*resolved_args)

    def __init__(self, lines):
        self.wires = {}
        for line in lines:
            try:
                wirein, wirename = map(str.strip, line.split('->'))
            except ValueError:
                raise InvalidLine(line)

            wireops = wirein.split()
            num_ops = len(wireops)
            if num_ops == 1:
                op = self._WireOp(None, wireops[0])
            elif num_ops == 2:
                if wireops[0] != 'NOT':
                    raise InvalidLine(line)
                op = self._WireOp(self.not_, wireops[1])
            elif num_ops == 3:
                try:
                    opfunc = {
                        'AND': self.and_,
                        'OR': self.or_,
                        'LSHIFT': self.lshift,
                        'RSHIFT': self.rshift
                    }[wireops[1]]
                except KeyError:
                    raise InvalidLine(line)

                op = self._WireOp(opfunc, wireops[0], wireops[2])
            else:
                raise InvalidLine(line)

            self.wires[wirename] = op

    def reset(self):
        for wire in self.wires.values():
            wire.reset()

    def update(self, wirename, op, *args):
        self.wires[wirename] = self._WireOp(op, *args)

    def value(self, wirename):
        return self.wires[wirename].value(self.wires)


class InvalidLine(Exception):
    def __init__(self, line):
        super().__init__(f'invalid line: {line.strip()}')


if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        circuit = Circuit(f.readlines())

    a_signal = circuit.value('a')
    print(a_signal)
    circuit.reset()

    circuit.update('b', None, a_signal)
    print(circuit.value('a'))
