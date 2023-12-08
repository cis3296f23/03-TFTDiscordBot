
![RG_REMIX-RUMBLE_GAMEPLAY-OVERVIEW-ARTICLE_BANNER-IMAGE_1920X1080](https://github.com/cis3296f23/03-TFTDiscordBot/assets/118203614/661ffa48-fdec-4e60-8bcc-6a8933d93fff)
### Project Abstract
This proposed project involves the development of a discord bot for the game Teamfight Tactics
(TFT) by Riot Games. TFT is a popular online multiplayer strategy game with in-game purchases,
a ranking system, and frequent updates. The Discord bot will enable users to retrieve information
from the Riot Games system and provide relevant game-related data in response to user commands.
Additionally, this bot will also incorporate image-fetching capabilities, aligning with specific commands to
enhance the overall discord experience.

### Conceptual Design

Discord bot: this will be the core. This will be responsible for interacting with the Discord API to
receive and respond to user commands within Discord servers, which will be developed in Python.
The project will require access to Riot Games' APIs for real-time game data. It will involve proper
documentation and API key management to effectively integrate these APIs
TFT Game Data: Access to TFT game data via Riot Games' APIs will enable the bot to retrieve
information.
Game related images and icons: The bot will feature the display of game-related images and icons
within the Discord server
Authentication: To enable the bot to connect to a Discord server, a Discord bot key will be
required.

### Use Case

This bot can be used on Discord to collect TFT game data. See Personas for more detailed use cases.

### Feature List
  -  Summoner command 
  -  Item command
  -  Component command
  -  Component list command
  -  Match command
  -  Help command
  -  Droprates command
  -  Rank command


### Vision Statement

For TFT players and fans who want to keep track of TFT game statistics, the TFT Discord
Bot is a bot you can add to your favorite discord servers that provides statistics for any game
you would want to keep track of. Unlike other services, which are web-based and only give
stats after games complete, our product provides statistics in real time within discord itself.

# Personas
### Persona 1 - Dave, a game streamer
(Bao Nguyen) Dave is a 32-year-old game streamer who focuses on card games. One day he
surfs other streaming platforms and finds a new interesting game play mode called
Teamfight Tactics. He would like to play the game for streaming, but he is not familiar with
the mechanics, strategies of the game. As a streamer, he needs to learn the basic concept of
the game before streaming. Therefore, he wants an easy way to get that information for better
understanding the game.
Dave finds the TFT bot would be useful for his intention. Since it is not only helpful for
learning, but also searching the strategies and synergies of the champions while streaming.
The most important thing he likes that he can use the TFT bot side by side with the game
he's playing
### Persona 2 - Riccardo, an e-sports professional
(Francis R Scallatino) Riccardo (21) plays RTS games professionally while he’s studying
for a degree in Computer Science. When he was a kid, he absolutely loved planning things.
He would actively get involved in clubs and do his best to lead them in the right direction
to grow the clubs and go on informative yet fun field trips. His favorite subject was Math.
He’s a logical thinker who prefers to think things through at a deep level to yield the best
results with everything he does.
As a top player in TFT, he is constantly looking for new strategies to best his opponents.
He’s good at thinking on his feet in the moment, although he finds that’s not always the
best way to learn. He wants to watch more games, although he can’t always be so
distracted with background gameplay since he has a lot of schoolwork to get done as well.
On his search for ways to track live stats he finds the TFT Discord Bot and is overjoyed.
An easy, textual way to learn from games when he’s unable to view them.
### Persona 3 - Jack, a college student
(Jimmy Jiang) Jack is a 19-year-old college computer science student who is on spring break.
After speaking with his friend, he realized that most of them were playing a game called
TeamFight Tactics, which he wants to try out to be more connected with them. However,
after playing a couple games of tutorials, he still doesn't fully understand how the game
works. As a computer science student, Jack possesses a solid foundation in technical
concepts and is comfortable navigating the digital environment. However, Jack is more of
an expert in coding and programming than in strategy games, so he needs a user-friendly
resource to help him understand more about the game.
Jack is drawn into the TFT bot as a means to understand the strategic complexities of the
game. He needs a user-friendly resource that can provide a clear explanation of the game's
mechanics, synergies, and optimal strategies. Thus, the bot’s ability to simplify complex
concepts allows Jack to have a more enhanced gaming experience and was able to interact
with his friend on a shared passion.

### UML Diagrams
![SprintWeek4ClassDiagram drawio](https://github.com/cis3296f23/03-TFTDiscordBot/assets/118203614/812027df-e897-4d63-b2de-05ee6f93f12a)
  
  ![Untitled](https://github.com/cis3296f23/03-TFTDiscordBot/assets/118203614/e350a116-b663-4762-a98a-636a8e5d5fcb)
  ![TFT_Discord_Bot_Sequence_Diagram_2_-_Retrieving_Summoner_Info](https://github.com/cis3296f23/03-TFTDiscordBot/assets/118203614/86da70c7-626f-4dcc-a6df-281dfed329b6)

The user presented within this diagram can use several commands on discord bot. Then, the bot respond to the commands by making requests to the Riot server
to retrieve the data which the user is desired to know. Lastly, the bot returns the data to the user.
### Required Resources

  This project uses Python only. Knowledge about API is necessary to generate API key and retrieve the information from Riot server.
  Visual Studio is recommended for this project.  
  https://github.com/cis3296f23/03-TFTDiscordBot
  



