import requests

async def rank_info(ctx, name, summoner_url, rank_url, RIOT_GAMES_API_KEY):
    try:
        # Summoner information
        api_url = f"{summoner_url}/{name}?api_key={RIOT_GAMES_API_KEY}"
        resp = requests.get(api_url)
        resp.raise_for_status()  # Check for errors in the response

        # Get Summoner Information 
        summoner_info = resp.json()
        summoner_id = summoner_info['id']

        # Rank information using summoner ID
        get_rank = f"{rank_url}/{summoner_id}?api_key={RIOT_GAMES_API_KEY}"
        rank_resp = requests.get(get_rank)
        rank_resp.raise_for_status()

        # Fetch TFT data
        rank_info = rank_resp.json()

        if rank_info:
            tft_rank = f"TFT Rank: {rank_info[0]['tier']} {rank_info[0]['rank']}"
            
            # WinRate 
            if 'wins' in rank_info[0] and 'losses' in rank_info[0]:
                wins = rank_info[0]['wins']
                losses = rank_info[0]['losses']
                winrate = (wins / (wins + losses)) * 100
                tft_rank += f"\nWins: {wins}, Lost: {losses}, Winrate: {winrate:.2f}%"
        else:
            tft_rank = "TFT Rank: Unranked"

        await ctx.send(f"{tft_rank}")

    except requests.exceptions.HTTPError as err:
        await ctx.send(f"Error fetching match information: {err}")
