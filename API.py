api_key = "RGAPI-93f45e9a-2a32-4b4d-8b2e-411239b2875d"
name = input("what is your summoner's name? ")
api_summoner_url = "https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-name"
api_url = api_summoner_url + "/" + name
api_url = api_url + "?api_key=" + api_key
import requests
resp = requests.get(api_url)
player_info = resp.json()
summonerName = player_info['name']
summonnerLeverl = player_info["summonerLevel"]
puuid = player_info['puuid']
print("Summoner level: ", summonnerLeverl)
print("Summoner puuid:", puuid)