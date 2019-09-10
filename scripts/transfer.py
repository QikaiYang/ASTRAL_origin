import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_tree", type=str, help="Input Fasta File Name")
parser.add_argument("output_tree", type=str, help="Output file")
args = parser.parse_args()


