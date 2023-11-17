# summoner_command.py

import requests

async def get_summoner_info(ctx, name, summoner_url, rank_url, icon_url, API_KEY):
    try:
        # Summoner information
        api_url = f"{summoner_url}/{name}?api_key={API_KEY}"
        resp = requests.get(api_url)
        resp.raise_for_status()  # Check for errors in the response

        # Fetch data
        player_info = resp.json()
        summoner_level = player_info["summonerLevel"]
        puuid = player_info['puuid']
        profile_icon = player_info['profileIconId']

        # Get Icon 
        icon = f"{icon_url}{profile_icon}.png"

        # Rank information using summoner ID
        get_rank = f"{rank_url}/{player_info['id']}?api_key={API_KEY}"
        rank_resp = requests.get(get_rank)
        rank_resp.raise_for_status()

        # Fetch TFT data
        rank_info = rank_resp.json()
        if rank_info:
            tft_rank = f"TFT Rank: {rank_info[0]['tier']} {rank_info[0]['rank']}"
        else:
            tft_rank = "TFT Rank: Unranked"

        await ctx.send(f"Summoner level: {summoner_level}\nSummoner PUUID: {puuid}\n{tft_rank}\nProfile Icon: {icon}")

    except requests.exceptions.HTTPError as err:
        await ctx.send(f"Error fetching summoner information: {err}")
