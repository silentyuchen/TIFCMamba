# TIFCMamba
## 1.enviorment
conda create -n TIFCMamba python=3.10

conda activate TIFCMamba

pip install torch==1.12.1 torchvision==0.13.1

pip install -U openmim

pip install -r requirements.txt

python -m mim install mmcv-full==1.6.2 mmsegmentation==0.27.0

python
import nltk

nltk.download('punkt')

nltk.download('averaged_perceptron_tagger')
## 2.dataset
cc3m: https://github.com/rom1504/img2dataset/blob/main/dataset_examples/cc3m.md
  

