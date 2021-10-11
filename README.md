# Crowd-sourcing for Language Processing (Data and Baseline Systems)

This repo provides the list of files and baseline recipe for the CLAP dataset. 

## Software Setup Instructions
These recipes are fine-tuned with [XLSR/wav2vec2.0](https://huggingface.co/transformers/model_doc/wav2vec2.html) style models as an ASR framework. Please use HuggingFace baseline [CLSRIL](https://huggingface.co/Harveenchadha/wav2vec2-pretrained-clsril-23-10k) as the baseline model for fine-tuning experiments and reproducing the baseline results.

The baseline code has been modified from the standard huggingface fine-tuning script that is available [here](https://huggingface.co/blog/fine-tune-xlsr-wav2vec2)

## Data Setup Instructions

The data used for our baseline recipe can be found on our [website](https://www.cse.iitb.ac.in/clap/download_link_challenge.html)
Please choose the corresponding language and enter your details before the download can proceed.

## Folder Setup

Each of the language folders contains the csv files used for training and evaluating the models. 
```bash
CLAP_baseline
├── Hindi																
│   ├── Hindi_train_2.5.csv   	-> Contains 2.5 hrs of Hindi audio data File paths used for training					
│   │																	
│   └── Hindi_dev.csv         	-> Contains 2 hrs of Hindi audio data File paths used for evaluating					
|																	
├── Marathi																
│   ├── Marathi_train_2.5.csv   -> Contains 2.5 hrs of Marathi audio data File paths used for training					
│   │																	
│   └── Marathi_dev.csv         -> Contains 2 hrs of Marathi audio data File paths used for evaluating
|
├── Tamil
│   ├── Tamil_train_2.5.csv   	-> Contains 2.5 hrs of Tamil audio data File paths used for training
│   │
│   └── Tamil_dev.csv         	-> Contains 2 hrs of Tamil audio data File paths used for evaluating
|
├── Telugu
│   ├── Telugu_train_2.5.csv   	-> Contains 2.5 hrs of Telugu audio data File paths used for training
│   │
│   └── Telugu_dev.csv         	-> Contains 2 hrs of Telugu audio data File paths used for evaluating
|
└── Training_scripts
    ├── wav2vec_CLSRIL.ipynb    -> Finetuning script for training the wav2vec base model (CLSRIL)
    │
    └── LM
        ├── test_final.py     				 -> Modified LM scripts from wav2vecwrapper
        └── config_example_external_LM_rescore.json	 
	|__ wer.py					 -> WER calculation script from final outputs

```

## Running the baseline script

The baseline fine-tuning script can be directly run after setting up a virtual environment and installing the packages given in the notebook or on hugging-face.

For LM-setup we used [wav2vecwrapper](https://github.com/Edresson/Wav2Vec-Wrapper) and replaced the corresponding files as given in the folder setup with our own setup.The LM lexicon files and the Kenlm models used were trained on the data from [AIBharat] (https://indicnlp.ai4bharat.org/corpora/) corpus.

## Baseline Results

| Language        |     Without LM(% WER/CER) |     With LM (% WER/CER) |
|-----------------|---------------------------|-------------------------|
| Hindi	          | 42.85/14.93               | 32.32/10.92             |
| Marathi         | 54.77/15.21               | 34.58/10.41             |
| Tamil           | 68.93/14.80               | 38.13/8.29              |
| Telugu          | 73.77/19.24               | 59.00/15.90             |
