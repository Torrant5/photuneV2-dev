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
    # TODO AIチューニング後、予測したものに変える...
    if id==1:
        data = {"playlist_id": '37i9dQZF1E4lH3u1Jp9uoD',
            "playlist_name": 'Flower Radio'}
        # rapeseed
        # data = {"playlist_id": '37i9dQZF1DXafb0IuPwJyF',
        #     "playlist_name": 'Tokyo Super Hits!'}
    elif id==2:
        data = {"playlist_id": '37i9dQZF1DWVqFWv4EZA70',
            "playlist_name": 'Relax Brunch'}
        # running_shoe
        # data = {"playlist_id": '37i9dQZEVXbINTEnbFeb8d',
        #     "playlist_name": 'Viral 50 - Japan'}
    else:
        data = {"playlist_id": '37i9dQZF1DX4Y4RhrZqHhr',
            "playlist_name": 'Beach Party'}
        # coral_reef
        # data = {"playlist_id": '37i9dQZEVXbINTEnbFeb8d',
        #     "playlist_name": 'Viral 50 - Japan'}
    return data