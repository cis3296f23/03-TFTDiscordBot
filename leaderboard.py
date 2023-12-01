import requests

async def get_tft_leaderboard(ctx, leaderboard_url, API_KEY):
    try:
        # Fetch TFT leaderboard information
        leaderboard_api_url = f"{leaderboard_url}?api_key={API_KEY}"
        leaderboard_resp = requests.get(leaderboard_api_url)
        leaderboard_resp.raise_for_status()

        leaderboard_info = leaderboard_resp.json()

        top_10_entries = leaderboard_info['entries'][:10]
        
        # fix the display as its shown as I instead of Challenger, Gramaster etc so I need an def get_rank
        def get_rank(rank):
            
            ranks= {{'I': 'Challenger', 'II': 'Grandmaster', 'III': 'Master'}}
            return ranks.get(rank, rank)

        leaderboard_text = "Top 10 TFT Players:\n"
        for index, entry in enumerate(top_10_entries, start=1):
            
            summoner_name = entry['summonerName']
            league_points = entry['leaguePoints']
            wins = entry['wins']
            losses = entry['losses']
            rank = get_rank(entry['rank'])

            player_info = f"{index}. {summoner_name} ({rank}) - LP: {league_points} | Wins: {wins} | Losses: {losses}\n"
            leaderboard_text += player_info

        await ctx.send(leaderboard_text)

    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
