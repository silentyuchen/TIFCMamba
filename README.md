# TIFCMamba
## 1.enviorment
conda create -n TIFCMamba python=3.10

conda activate TIFCMamba

pip install torch==1.12.1 torchvision==0.13.1

pip install -U openmim

pip install -r requirements.txt

python -m mim install mmcv-full==1.6.2 mmsegmentation==0.27.0

pip install img2dataset

python
import nltk

nltk.download('punkt')

nltk.download('averaged_perceptron_tagger')
## 2.dataset
Please download the training split annotation file from Conceptual Caption 3M and name it as gcc3m.tsv. Conceptual Caption 3M：https://ai.google.com/research/ConceptualCaptions/download

Then run img2dataset to download the image text pairs and save them in the webdataset format.

sed -i '1s/^/caption\turl\n/' gcc3m.tsv

img2dataset --url_list gcc3m.tsv --input_format "tsv" \
            --url_col "url" --caption_col "caption" --output_format webdataset \
            --output_folder data/gcc3m \
            --processes_count 16 --thread_count 64 \
            --image_size 512 --resize_mode keep_ratio --resize_only_if_bigger True \
            --enable_wandb True --save_metadata False --oom_shard_count 6
            
rename -d 's/^/gcc-train-/' data/gcc3m/*


cvc-clinicDB:https://storage.googleapis.com/kaggle-data-sets/930614/1574219/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20241213%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20241213T015922Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=13985afd566ead2d1059aeeeec031912ba3fb9fa4bf580dd9500c065c59f5c9c8c2cf737e1303bd861112697720d4d26bc7a991f796b1989006a6b1f155bf734c71be250034b13650dfe483959e6b037a85f3cee6b942930793df6db5223010a8a2937c839142f47271e939913bbe6e9a8f76610a34db457aaed68bb7fc3aa7eacaeb00efdb326ad42642477af8990c8adf710ec1d3380c512ad77cf0e3ff129d2df9564aee9d545f736410db514419b1a6d5e8122b769f0435666aed2fbdd7cd4d5bd6f2d781af749780995610aa7828ab1464895a95733f1bb208ab08fe6e73d4475c7c695a0815373444bd71922c16e53adb09f3fbeb64f9b334c6dc35b3d

cvc-colonDB:https://storage.googleapis.com/kaggle-data-sets/4609976/7859080/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20241213%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20241213T020123Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=9b3159954956d87f17b07a67794ff515f3e1597401f68a4794259a0c63446240e06211736079e0e4b97a42c474a4ecd2bec7e2a8a55523f233db75ef965a1b6d0ba9a72138426ee14614cc308808185822f663bfed331749fabd594cfbbed6880541d8a45b8199042b36827302bdb41ac222249c0e4b7b95716776624a6ecf6ec9ee5aa5b7a5d0b9b39258302a12da1993120b25bef0c61128b3653ba3b706987593be45114274c5c9ff18feb92ce1c8835d79186b36313b0c8ae3e5869baa50e4f1815401b18c9835b91716a6e5116921e213438e7e66ab8d4b6c1c4ae6cf4e4fe19ff0cf92f41e25df03a9e613866cd34462827b8465cc0888cc0badc14654

