import random
import json
import os
from template import *

def generate(data, templates):
    num_samples = 1
    output = []
    for line in data:
        source, target, gen_type = line.strip().split('\t')
        for _ in range(num_samples):
            template = templates[0]
            instruction = template.format(input="'"+source+"'", output="'"+target+"'")
            data = {'instruction': instruction, 'input': "", 'output': "",
                    'gen_type': gen_type}
            output.append(data)

    return output

def main():
    with open("data/cogs/train.tsv") as f:
        data = f.readlines()
    output = generate(data, templates=templates["COGS"])

    os.makedirs("data/cogs_base", exist_ok=True)
    with open("data/cogs_base/train.json", 'w') as f:
        json.dump(output, f, indent=4, separators=(',', ':'))

if __name__ == '__main__':
    main()