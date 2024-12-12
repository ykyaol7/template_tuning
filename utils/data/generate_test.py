import random
import json
import os
from template import *

def generate(data):
    num_samples = 1
    output = []
    for line in data:
        source, target, gen_type = line.strip().split('\t')
        for _ in range(num_samples):
            template = "Parse {input} into COGS meaning representation:"
            instruction = template.format(input="'"+source+"'")
            data = {'instruction': instruction, 'input': "", 'output': "'"+target+"'",
                    'gen_type': gen_type}
            output.append(data)

    return output

def main():
    with open("data/cogs/gen.tsv") as f:
        data = f.readlines()
    output = generate(data)

    os.makedirs("data/cogs", exist_ok=True)
    with open("data/cogs/gen.json", 'w') as f:
        json.dump(output, f, indent=4, separators=(',', ':'))

if __name__ == '__main__':
    main()