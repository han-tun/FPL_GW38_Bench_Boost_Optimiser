import json
import csv


def main():
    with open("G_players_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # this is where we calculate the score for each player.
    # needs work as it's difficult to know what to take into account and what weighting everything should have
    for player in data.values():
        if player["games_played"] == 0:
            player["score"] = 0
        else:
            # points per  game played - to raise score of players who score highly when they play
            ppg = player["points"] / player["games_played"]

            # proportion of matches played - to raise score of players who play often
            # issue is this will ruin the score of anyone who joined in the January transfer window, Fernandes being a good example
            prop_played = player["games_played"] / (38 - player["fixtures_remaining"])

            # 1/average difficulty * fixtures remaining - to raise score of those with easeir fixtures and those with more fixtures
            fixture_score = player["fixtures_remaining"] / player["average_difficulty"]

            player["score"] = round(ppg * prop_played * fixture_score, 2)

    # The optimiser takes a csv file with headers "pos, name, cost, score, team", where score is what we want to optimise.
    with open("I_final_player_data.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["pos", "name", "cost", "score", "team"])
        writer.writerows([[player["pos"][0], player["name"], player["cost"], player["score"], player["team_name"]]
                          for player in data.values()])


if __name__ == "__main__":
    main()
