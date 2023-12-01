
import requests

async def get_tft_leaderboard(ctx, leaderboard_url, API_KEY):
    try:
        # Fetch TFT leaderboard information
        leaderboard_api_url = f"{leaderboard_url}?api_key={API_KEY}"
        leaderboard_resp = requests.get(leaderboard_api_url)
        leaderboard_resp.raise_for_status()

        leaderboard_info = leaderboard_resp.json()  # Adjust this based on your API response

        await ctx.send(f"TFT Leaderboard:\n{leaderboard_info}")

    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
