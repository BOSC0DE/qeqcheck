import os
import sys
import ckt
import argparse
import readbench
import adapter
from lingeling import Solver


def to_dimacs(cnf, filename):
    for output in cnf:
        num_literals = max([max([abs(l) for l in clause]) for clause in output])
        with open(filename, "w") as f:
            f.write("p cnf %d %d\n" % (num_literals, len(output)))
            for clause in output:
                for literal in clause:
                    f.write("%d " % literal)
                f.write("0\n")


def main(argv):
    # Read two bench files
    parser = argparse.ArgumentParser(description='bench to qcnf')
    parser.add_argument('bench', type=str, help='1st bench file to analyze.')
    args = parser.parse_args()

    inputs, outputs, node_map = readbench.readBenchFile(args.bench)

    # get cnf of each output
    cnf = []
    S = Solver()
    node_to_literal_map = {}
    for o in outputs:
        cnf.append(adapter.circuitToCNF(o, node_to_literal_map, lambda n: S.newVar()))
        to_dimacs(cnf, os.path.splitext(args.bench)[0] + "_" + o.name + ".qcnf")


if __name__ == '__main__':
    main(sys.argv)
