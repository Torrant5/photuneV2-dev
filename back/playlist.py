import pandas as pd

# spotifyデータよみこみ
playlists_df = pd.read_pickle('data/all_playlists.pkl')
playlists_text = pd.read_pickle('data/playlists_text.pkl')
categories = playlists_df["category"].drop_duplicates().reset_index()

# API用関数
def get_random():
    global playlists_df
    sample_idx = playlists_df.sample().index[0]
    playlist_name = playlists_df["name"][sample_idx]
    playlist_id = playlists_df["id"][sample_idx]

    return {"playlist_id": playlist_id,
            "playlist_name": playlist_name}

def get_sample(id):
    # TODO 余裕があれば変える きちんと予測した方が良い？
    if id==1:
        data = {"playlist_id": '3zVlpKfmFSKVHTfe8p8Kr5',
            "playlist_name": '204 ピクニック日和に聴きたいプレイリスト'}
    elif id==2:
        data = {"playlist_id": '37i9dQZF1DXdLD1ufgw60J',
            "playlist_name": 'Classical Cooking'}
    else:
        data = {"playlist_id": '75wr3eDFIfQJXNX1A3Vqq1',
            "playlist_name": '海で聴きたい洋楽'}
    return data