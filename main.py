import os
import sys
import ckt
import argparse
import readbench
import adapter


def main(argv):

    parser = argparse.ArgumentParser(description='bench to qcnf')
    parser.add_argument('bench1', type=str, help='1st bench file to analyze.')
    parser.add_argument('bench2', type=str, help='2nd bench file to analyze.')

    args = parser.parse_args()

    inputs_1, outputs_1, node_map_1 = readbench.readBenchFile(args.bench1)
    inputs_2, outputs_2, node_map_2 = readbench.readBenchFile(args.bench2)

    assert outputs_2 == outputs_1

    print (outputs_2)
    print (outputs_1)




if __name__ == '__main__':
    main(sys.argv)
