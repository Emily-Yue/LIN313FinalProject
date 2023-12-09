# script that removes the answers from a JSON file representing a crossword puzzle

import argparse
import os
import json
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--Output", help="output folder")

args = parser.parse_args()

out_dir = args.Output

input_dir = 'crosswords_mini/2023'

def go_through_dir(input_dir_inner, out_dir_inner):
    # go through each file in the input directory
    for file in os.scandir(input_dir_inner):
        if file.is_file():
            filename = file.path
            f = open(filename)
            data = json.load(f)
            del data['puzzle_data']['answers']
            data['puzzle_data']['answers'] = []
            output_file = out_dir_inner+'/'+str(Path(file.path).stem)+'_empty.json'
            with open(output_file, 'w') as outfile:
                json.dump(data, outfile)

for i in range(1, 13):
    inner_input_dir = input_dir+"/"+"{:02d}".format(i)
    inner_out_dir = out_dir+"/"+"{:02d}".format(i)
    os.mkdir(inner_out_dir)
    # print(inner_input_dir, inner_out_dir)
    go_through_dir(inner_input_dir, inner_out_dir)

