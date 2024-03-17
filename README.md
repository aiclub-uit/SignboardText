# SignboardText
> Scene text detection and recognition have attracted much attention in recent years because of their potential applications. Detecting and recognizing texts in images may suffer from scene complexity and text variations. Some of these problematic cases are included in popular benchmark datasets, but only to a limited extent. In this work, we investigate the problem of scene text detection and recognition in a domain with extreme challenges. We focus on in-the-wild signboard images in which text commonly appears in different fonts, sizes, artistic styles, or languages with cluttered backgrounds. We first contribute an in-the-wild signboard dataset with 79K text instances on both line-level and word-level across 2,104 scene images. We then comprehensively evaluated recent state-of-the-art (SOTA) approaches for text detection and recognition on the dataset. By doing this, we expect to realize the barriers of current state-of-the-art approaches to solving the extremely challenging issues of scene text detection and recognition, as well as their applicability in this domain. 

This repository includes the code and data links mentioned in our papers, encompassing all the training data, evaluation scripts, and results utilized in our research.

<p align="center">
  <img alt="example1" src="resources/1.jpg" width="28%" height=250>
  <img alt="example2" src="resources/2.jpg" width="28%" height=250>
  <img alt="example3" src="resources/3.jpg" width="28%" height=250>
  <img alt="example4" src="resources/4.jpg" width="28%" height=250>
  <img alt="example5" src="resources/5.jpg" width="28%" height=250>
  <img alt="example6" src="resources/6.jpg" width="28%" height=250>
</p>



<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg" align="center">
<thead>
  <tr>
    <th class="tg-0pky">Dataset</th>
    <th class="tg-c3ow">IC15</th>
    <th class="tg-c3ow">TotalText</th>
    <th class="tg-c3ow">VinText</th>
    <th class="tg-c3ow">Ours</th>
    <th class="tg-c3ow">Total</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">No. of <br>signboard<br>images</td>
    <td class="tg-c3ow">2</td>
    <td class="tg-c3ow">411</td>
    <td class="tg-c3ow">516</td>
    <td class="tg-c3ow">1175</td>
    <td class="tg-c3ow">2104</td>
  </tr>
  <tr>
    <td class="tg-0pky">No. of <br>text instances</td>
    <td class="tg-c3ow" colspan="3">20261</td>
    <td class="tg-c3ow">59588</td>
    <td class="tg-c3ow">79849</td>
  </tr>
</tbody>
</table>

## Download
To download the data, please send a request email to thuyentd@uit.edu.vn and tell us which school you are affiliated with. And by downloading this dataset, USER agrees:
> * to use this dataset for research or educational purposes only;
> * to not distribute or part of this dataset in any original or modified form;
> * and to cite our github repo whenever this dataset are employed to help produce published results.

```
|-- annotations.json
|-- annotations_line.json
|-- detection
|-- images
`-- recognition
    |-- images
    `-- labels
```

## Detection
### Main results:
The results can be found in the `eval/det_results` directory and can be reproduced using the scripts in the `src/` folder. To verify the accuracy of the results marked with the symbol † (in supplemental tables), utilize the evaluation script provided in the `eval/detections/eval_det` directory.
| Methods     | **Signboard** |           |        | **ICDAR2015** |           |           | **TotalText** |           |        |Reference| Link to model|
|-------------|:-------------:|:---------:|:------:|:-------------:|:---------:|:---------:|:-------------:|:---------:|:------:|:------:|:------:|
|             |     Recall    | Precision | H-mean |     Recall    | Precision |   H-mean  |     Recall    | Precision | H-mean |||
| TextSnake   |         57.06 |     60.67 |  58.56 |      84.9     |    80.4   |    82.6   |      84.9     |    80.4   |  82.6  |[link](https://github.com/open-mmlab/mmocr/blob/main/configs/textdet/textsnake/README.md)|[link](https://download.openmmlab.com/mmocr/textdet/textsnake/textsnake_resnet50_fpn-unet_1200e_ctw1500/textsnake_resnet50_fpn-unet_1200e_ctw1500_20220825_221459-c0b6adc4.pth)|
| PANet       |         71.92 |     78.98 |  75.14 |      77.8     |    82.9   |    80.3   |       81      |    89.3   |   85   |[link](https://github.com/open-mmlab/mmocr/blob/main/configs/textdet/panet/README.md)|[link](https://download.openmmlab.com/mmocr/textdet/panet/panet_resnet18_fpem-ffm_600e_ctw1500/panet_resnet18_fpem-ffm_600e_ctw1500_20220826_144818-980f32d0.pth)|
| PSENet      |         78.09 |     82.06 |  79.94 |      84.5     |   86.92   |   85.69   |     77.96     |   84.02   |  80.87 |[link](https://github.com/open-mmlab/mmocr/blob/main/configs/textdet/psenet/README.md)|[link](https://download.openmmlab.com/mmocr/textdet/psenet/psenet_resnet50_fpnf_600e_ctw1500/psenet_resnet50_fpnf_600e_ctw1500_20220825_221459-7f974ac8.pth)|
| ABCNet v1   |         64.48 |     76.26 |   69.4 |   86.33 [1]   | 88.76 [1] | 87.53 [1] |     50.48     |   66.53   |  57.4  |[link](https://github.com/aim-uofa/AdelaiDet)|[link](https://huggingface.co/ZjuCv/AdelaiDet/blob/main/tt_e2e_attn_R_50.pth)|
| DBNet       |          60.7 |     73.39 |  66.09 |     82.76     |   87.44   |   85.04   |      82.5     |    87.1   |  84.7  |[link](https://github.com/open-mmlab/mmocr/blob/main/configs/textdet/dbnet/README.md)|[link](https://download.openmmlab.com/mmocr/textdet/dbnet/dbnet_resnet50_1200e_icdar2015/dbnet_resnet50_1200e_icdar2015_20221102_115917-54f50589.pth)|
| DRRG        |         50.82 |      71.6 |  59.22 |     84.69     |   88.53   |   86.56   |     84.69     |   88.53   |  86.56 |[link](https://github.com/open-mmlab/mmocr/blob/main/configs/textdet/drrg/README.md)|[link](https://download.openmmlab.com/mmocr/textdet/drrg/drrg_resnet50_fpn-unet_1200e_ctw1500/drrg_resnet50_fpn-unet_1200e_ctw1500_20220827_105233-d5c702dd.pth)|
| FCENet      |         70.38 |     75.93 |   72.9 |      82.6     |    90.1   |    86.2   |     88.34     |   82.43   |  85.28 |[link](https://github.com/open-mmlab/mmocr/blob/main/configs/textdet/fcenet/README.md)|[link](https://download.openmmlab.com/mmocr/textdet/fcenet/fcenet_resnet50-dcnv2_fpn_1500e_ctw1500/fcenet_resnet50-dcnv2_fpn_1500e_ctw1500_20220825_221510-4d705392.pth)|
| ABCNet v2   |         64.32 |     77.66 |  69.95 |      90.4     |     86    |    88.1   |      90.2     |    84.1   |   87   |[link](https://github.com/aim-uofa/AdelaiDet)|[link](https://huggingface.co/ZjuCv/AdelaiDet/blob/main/model_v2_totaltext.pth)|
| DPText-DETR |         60.46 |     90.56 |  72.07 |     90.93     |   41.61   |   57.09   |      86.4     |    91.8   |   89   |[link](https://github.com/ymy-k/DPText-DETR)|[link](https://1drv.ms/u/s!AimBgYV7JjTlgccGbLGc9wYB-CGfpg?e=kpyje7)|
| DeepSolo    |         63.11 |     91.05 |   74.2 |     92.54     |   87.19   |   89.79   |     93.19     |   84.64   |  88.72 |[link](https://github.com/ViTAE-Transformer/DeepSolo)|[link](https://1drv.ms/u/s!AimBgYV7JjTlgcd6XGlbZ-I7WvGslQ?e=rrkXLx)|



### Running the scripts
For examples:
python
```
python eval_det/script.py –g=gt/gt.icdar.zip –s=res/occluded/psenet/det.psenet-pretrained-icdar2015.rotatebox.zip –o=./ -p={\"IOU_CONSTRAINT\":0.4}
```


### Model usage:
- We use the following methods for predicting and get the results:
    + MMOCR `src/mmocr`: TextSnake(CTW1500-Resnet), PANet(ICDAR2015), PSENet (CTW1500-Resnet50), DBNet (ICDAR2015), DRRG(CTW1500-Resnet50), FCENet(CTW1500-Resnet50);
    + ABCNet v1 (v1-icdar2015-finetune), ABCNet v2 (v2-icdar2015-finetune) both are from `src/AdelaiDet/`;
    + DPText-DETR `src/DPText-DETR` (Total-Text	Res50) , DeepSolo (ViTAEv2 Synth150K+Total-Text+MLT17+IC13+TextOCR) `src/DeepSolo`

## Recognition

Similar to text detection, the results are stored in the `eval/rec_results` directory. For this section, re-evaluation is focused on results marked with the symbol † (in supplemental tables).

For examples:
python
```
python recognition/eval_rec.py --gt_file rec_gts/coco.txt --pred_file rec_results/results/starnet/coco.txt
```
### Main results:
| Method                | **Signboard** | **IC13** | **IC15** | **ToTalText** | **Coco-text** ||
|-----------------------|:-------------:|:--------:|:--------:|:-------------:|:-------------:|:-------------:|
| CRNN                  |     39.04     | 89.2 [2] | 64.2 [2] |     49.48     |     32.46     |[link](https://www.dropbox.com/sh/j3xmli4di1zuv3s/AACpKykhWSRBUU7xl2LGgt9ja/None-VGG-None-CTC.pth?dl=0)|
| STAR-Net              |      47.4     | 91.5 [2] | 70.3 [2] |     35.07     |     24.14     |[link](https://www.dropbox.com/sh/j3xmli4di1zuv3s/AAB0X-sX05-0psb4uXWPYSmza/TPS-ResNet-BiLSTM-CTC.pth?dl=0)|
| Rosetta               |     46.12     |  89 [2]  | 66.0 [2] |     15.81     |      9.3      |[link](https://www.dropbox.com/sh/j3xmli4di1zuv3s/AABzCC1KGbIRe2wRwa3diWKwa/None-ResNet-None-CTC.pth?dl=0)|
| SAR                   |     57.96     |  94 [5]  | 78.8 [5] |     56.88     |    66.8 [5]   |[link](https://download.openmmlab.com/mmocr/textrecog/sar/sar_resnet31_sequential-decoder_5e_st-sub_mj-sub_sa_real/sar_resnet31_sequential-decoder_5e_st-sub_mj-sub_sa_real_20220915_185451-1fd6b1fc.pth)|
| Paddle OCR            |     11.56     |   94.09  |   69.96  |      66.2     |      51.3     |[link](https://github.com/PaddlePaddle/PaddleOCR)|
| VietOCR-TranformerOCR |     68.57     |   89.85  |   60.13  |     56.07     |     39.59     |[link](https://github.com/pbcquoc/vietocr)|
| SATRN                 |     56.34     | 94.1 [4] |  79 [4]  |     57.38     |      23.6     |[link](https://download.openmmlab.com/mmocr/textrecog/satrn/satrn_shallow_5e_st_mj/satrn_shallow_5e_st_mj_20220915_152443-5fd04a4c.pth)|
| ViTSTR                |     67.13     | 94.2 [3] | 78.7 [3] |     58.47     |    56.4 [3]   |[link](https://github.com/baudm/parseq/releases/download/v1.0.0/vitstr-26d0fcf4.pt)|
| ABINet                |     66.07     | 95.0 [3] | 79.1 [3] |     77.37     |    57.1 [3]   |[link](https://github.com/baudm/parseq/releases/download/v1.0.0/abinet-1d1e373e.pt)|
| PARSeq                |     68.55     | 96.2 [3] | 82.9 [3] |     71.51     |     64 [3]    |[link](https://github.com/baudm/parseq/releases/download/v1.0.0/parseq-bb5792a6.pt)|


### Training:
- Firstly, we cropped the images from dataset anh prepare using `create_lmdb_dataset.py`;
- Secondly, then for each the methods:
    + CRNN, SAR, SATRN and SVTR  `src/DPText-DETR`;
    + STARNet `PaddleOCR`;
    + VietOCR `src/vietocr`; 
    + etc...
