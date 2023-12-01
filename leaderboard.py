import requests

async def get_tft_leaderboard(ctx, leaderboard_url, API_KEY):
    try:
        # Fetch TFT leaderboard information
        leaderboard_api_url = f"{leaderboard_url}?api_key={API_KEY}"
        leaderboard_resp = requests.get(leaderboard_api_url)
        leaderboard_resp.raise_for_status()

        # Extract leaderboard data
        leaderboard_data = leaderboard_resp.json()
        leaderboard_info = "\n".join([f"{i + 1}. {entry['summonerName']} - {entry['leaguePoints']} LP" for i, entry in enumerate(leaderboard_data)])
        await ctx.send(f"TFT Leaderboard:\n{leaderboard_info}")

    except requests.exceptions.HTTPError as err:
        await ctx.send(f"Error {err}")