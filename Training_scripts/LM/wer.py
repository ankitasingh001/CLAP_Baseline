'''
Check WER/CER of obtained results
'''
import pandas as pd
import re
from datasets import load_dataset, load_metric, concatenate_datasets

chars_to_ignore_regex = '[\,\?\.\!\-\;\:\"\“\%\‘\”\�\–\…]'

def remove_spcl(string):
    return re.sub(chars_to_ignore_regex, '', string) + " "

# Enter path to test dataset csv output prompts from model
df = pd.read_csv('hin_eval_outputs.csv')
wer_pred = load_metric("wer")
cer_pred = load_metric("cer")

# Enter path to actual test dataset csv prompths
df1 = pd.read_csv('/ankita/Data/Hindi_eval_pratham.csv')
path ="/ankita/Data/Hindi_Data/Hindi_pratham/"

df1["text"] = df1["text"].apply(remove_spcl)
df1["audioFileName"] = path + df1["audioFileName"]
df1.sort_values(by=['audioFileName'], inplace=True)

print(df.head())
print(df1["text"].head())
print("***************************************************************************")
print("WER: {:2f}".format(100 * wer_pred.compute(predictions=df['transcription'], references=df1['text'])))
print("CER: {:2f}".format(100 * cer_pred.compute(predictions=df['transcription'], references=df1['text'])))
