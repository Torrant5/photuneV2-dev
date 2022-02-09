import pandas as pd
import torch
from torch import nn
import torch.nn.functional as F
from transformers import AutoModel, AutoTokenizer
from playlist import * 

# model distilbert 読み込み
# TODO: tensorflowかpytorchかに合わせる
tokenizer = None
model = None

# 事前計算tensor読み込み
tvs_tensor = None
categories_tensor = None


def load_model():
    tokenizer = AutoTokenizer.from_pretrained("cl-tohoku/bert-base-japanese-whole-word-masking", max_length=512)
    model = AutoModel.from_pretrained("bandainamco-mirai/distilbert-base-japanese") 
    tvs_tensor = torch.load('data/playlist_text_vectors.pt')
    categories_tensor = torch.load('data/categories_vectors.pt')
    return (tokenizer, model)

def load_calculated():
    tvs_tensor = torch.load('data/playlist_text_vectors.pt')
    categories_tensor = torch.load('data/categories_vectors.pt')
    return (tvs_tensor, categories_tensor)


# 計算関数
def getTextVector(model, tokenizer, text):
    token = tokenizer.encode(text, return_tensors='pt')
    model.eval()
    with torch.no_grad():
        output = model(token)
    lastlayer = output.last_hidden_state
    return lastlayer[:, 0, :]

def calcCosineSimilarity(sample_tv, datanum, tensors):
    cos_sims = []
    for tensor in tensors:
        cs = F.cosine_similarity(sample_tv, tensor)
        cos_sims.append(cs.item())
    return pd.DataFrame(cos_sims)[0]

def predict_direct(input_text: str):
    global tokenizer, model, playlists_df, tvs_tensor, categories_tensor
    if tokenizer is None:
        tokenizer, model  = load_model()
        tvs_tensor, categories_tensor = load_calculated()
    
    sample_tv = getTextVector(model, tokenizer, input_text)
    cos_sims = calcCosineSimilarity(sample_tv, len(tvs_tensor), tvs_tensor)
    most_sim = cos_sims.idxmax()
    playlist_name = playlists_df["name"][most_sim]
    playlist_id = playlists_df["id"][most_sim]
    return {"playlist_id": playlist_id,
            "playlist_name": playlist_name}

def predict_indirect(input_text: str):
    global tokenizer, model, playlists_df, categories, tvs_tensor, categories_tensor
    if tokenizer is None:
        tokenizer, model  = load_model()
        tvs_tensor, categories_tensor = load_calculated()

    sample_tv = getTextVector(model, tokenizer, input_text)
    cos_sims = calcCosineSimilarity(sample_tv, len(categories), categories_tensor)
    most_sim = cos_sims.idxmax()

    # カテゴリの名前
    ctg_name = categories["category"][most_sim]
    # playlist全体のtensorからカテゴリのtensorを抜き出す
    ctg_tvs_tensor = tvs_tensor[playlists_df["category"]==ctg_name]
    # 抜き出す最初のindexを取り出し
    idx = categories["index"][most_sim]

    cos_sims = calcCosineSimilarity(sample_tv, len(ctg_tvs_tensor), ctg_tvs_tensor)
    most_sim = cos_sims.idxmax()
    playlist_name = playlists_df["name"][most_sim]
    playlist_id = playlists_df["id"][most_sim]
    return {"playlist_id": playlist_id,
            "playlist_name": playlist_name}
