import json
import os
from typing import Tuple

def calc_acc(prediction_path: str) -> float:
    predictions = []
    with open(prediction_path, "r") as f:
        for line in f:
            predictions.append(json.loads(line))
    correct = 0
    total = 0
    metrics = {

    }
    for p in predictions:
        p["label"] = p["label"].replace("<|eot_id|>", "")
        if p["label"] == p["predict"]:
            correct += 1

        if p["gen_type"] not in metrics:
            metrics[p["gen_type"]] = {
                "correct": 0,
                "total": 0,
            }

        total += 1

    acc = correct / total
    print(f"Accuracy: {acc}")
    print(f"Correct: {correct}")
    print(f"Total: {total}")
    print(f"Total executed: {total}")


    return acc


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--prediction_path', type=str, required=True)
    args = parser.parse_args()
    calc_acc(args.prediction_path)

if __name__ == '__main__':
    main()


