# TIFCMamba
### enviorment
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
