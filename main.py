import os
import sys
import ckt
import argparse
import readbench
import adapter
from lingeling import Solver


def main(argv):

    parser = argparse.ArgumentParser(description='bench to qcnf')
    parser.add_argument('bench1', type=str, help='1st bench file to analyze.')
    parser.add_argument('bench2', type=str, help='2nd bench file to analyze.')

    args = parser.parse_args()

    inputs_1, outputs_1, node_map_1 = readbench.readBenchFile(args.bench1)
    inputs_2, outputs_2, node_map_2 = readbench.readBenchFile(args.bench2)


    #match the outputs
    for o1, o2 in zip(outputs_1, outputs_2):
        assert o1.name == o2.name

    miter = []
    i = 0
    for o1, o2 in zip(outputs_1, outputs_2):
        miter.append(ckt.XorGate(o1, o2))
        i += 1
    out = ckt.OrGate(*miter)

    node_to_lit_map = {}
    S = Solver()
    clauses = adapter.circuitToCNF(out, node_to_lit_map, lambda n: S.newVar())
    print(clauses)
    for n in node_to_lit_map:
        print(n.name, node_to_lit_map[n])



if __name__ == '__main__':
    main(sys.argv)
