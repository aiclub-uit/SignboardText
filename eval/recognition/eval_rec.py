from argparse import ArgumentParser
from typing import List, Dict, Any
from unicodedata import normalize
def eval_rec(gts: Dict[str, str],
    preds: Dict[str, str])  -> float:
    total_n_correct = 0
    missing_dict = list()
    for image_name, gt in gts.items():
        pred = preds.get(image_name, None)
        if pred == gt:
            total_n_correct += 1
        if pred is None:
            missing_dict.append(image_name)
    print(missing_dict)
    return total_n_correct / len(gts)
if __name__ == "__main__":

    argparser = ArgumentParser()
    argparser.add_argument("--gt_file", type=str, required=True)
    argparser.add_argument("--pred_file", type=str, required=True)
    args = argparser.parse_args()
    gt_lines = open(args.gt_file).readlines()
    pred_lines = open(args.pred_file).readlines()
    
    gts = dict()
    preds = dict()
    for gt_line, pred_line in zip(gt_lines, pred_lines):
        gt_line = gt_line.strip()
        pred_line = pred_line.strip()
        gt = gt_line.split("\t")
        if len(gt) == 2:
            gt_img_name, gt = gt
            gts[gt_img_name] = gt.lower()
        pred = pred_line.split("\t")
        if len(pred) == 2:
            pred_img_name, pred = pred

            preds[pred_img_name] = pred.lower()

    res = eval_rec(gts, preds)
    print(f"Accuracy: {res*100:.2f}")