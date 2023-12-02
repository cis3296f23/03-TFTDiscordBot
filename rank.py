import requests

async def rank_info(ctx, name, summoner_url, rank_url, RIOT_GAMES_API_KEY):
    try:
        # Summoner information
        api_url = f"{summoner_url}/{name}?api_key={RIOT_GAMES_API_KEY}"
        resp = requests.get(api_url)
        resp.raise_for_status()  # Check for errors in the response

        # Parse summoner information
        summoner_info = resp.json()

        # Extract summoner ID
        summoner_id = summoner_info['id']

        # Rank information using summoner ID
        get_rank = f"{rank_url}/{summoner_id}?api_key={RIOT_GAMES_API_KEY}"
        rank_resp = requests.get(get_rank)
        rank_resp.raise_for_status()

        # Fetch TFT data
        rank_info = rank_resp.json()

        if rank_info:
            tft_rank = f"TFT Rank: {rank_info[0]['tier']} {rank_info[0]['rank']}"
        else:
            tft_rank = "TFT Rank: Unranked"

        await ctx.send(f"{tft_rank}")

    except requests.exceptions.RequestException as err:
        await ctx.send(f"Error fetching summoner information: {err}")
