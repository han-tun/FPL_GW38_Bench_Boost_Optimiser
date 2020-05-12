import asyncio
import aiohttp
import json
from fpl import FPL
from fpl.utils import team_converter, position_converter

'''
the goal here is to download all relevant player data and save as a json along with the remaining fixture data so that a ``score`` can be calculated from that json. It is important that we only have to download the data once, as calcualting games played takes a long time for all players. The key for the dict is the player id to ensure that no player gets overwritten - two players known as stevens, for example, would otherwise be a problem.
e.g.
{
    "1": {
        "team_name": "Arsenal",
        "team_code": 1,
        "pos": "Defender",
        "name": "Mustafi",
        "cost": 5.1,
        "points": 26,
        "minutes": 620,
        "points_per_90": 3.77,
        "games played": 8
    },
'''


async def main():
    with open("E_average_fixture_difficulties.json", "r") as f:
        fixture_data = json.load(f)

    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        players = await fpl.get_players()
        player_dict = dict()
        for x in players:
            id = x.id
            team_code = x.team
            team_name = team_converter(team_code)
            pos = position_converter(x.element_type)
            name = x.web_name
            cost = x.now_cost / 10
            points = x.total_points
            minutes = x.minutes
            pp90 = round(x.pp90, 2)
            played = await x.games_played
            fixtures_remaining = fixture_data[team_name]["num_fixtures"]
            average_difficulty = fixture_data[team_name]["difficulties"][pos]

            player_dict[id] = {"team_name": team_name,
                               "team_code": team_code,
                               "pos": pos,
                               "name": name,
                               "cost": cost,
                               "points": points,
                               "minutes": minutes,
                               "points_per_90": pp90,
                               "games_played": played,
                               "fixtures_remaining": fixtures_remaining,
                               "average_difficulty": average_difficulty
                               }

    with open("G_players_data.json", "w", encoding="utf-8") as f:
        json.dump(player_dict, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
