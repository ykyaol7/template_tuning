import random
import json
import random
random.seed(0)

def generate(data, templates):
    output = []
    num_samples = 5
    for line in data:
        source, target, gen_type = line.strip().split('\t')
        for _ in range(num_samples):
            template = random.choice(templates)
            instruction = template.format(input="'" + source + "'",
                                          output="'" + target + "'")
            data = {'instruction': instruction, 'input': "", 'output': "",
                    'gen_type': gen_type}
            output.append(data)

    return output


def main():
    with open("data/cogs/train.tsv") as f:
        data = f.readlines()
    output = generate(data)
    with open("data/cogs/train.json", 'w') as f:
        json.dump(output, f, indent=4, separators=(',', ':'))


if __name__ == '__main__':
    main()
