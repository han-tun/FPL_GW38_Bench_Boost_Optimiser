import json

'''
The goal of this is to find the average fixture difficulty per team per position for their remaining fixtures
e.g.
{
    "Norwich": {
        "num_fixtures": 9,
        "difficulties": {
            "goalkeeper": 3.48,
            "defender": 3.06,
            "midfielder": 2.71,
            "forward": 3.2
        }
    }, ...
}
'''


def main():
    with open("B_fixture_difficulties.json", "r") as f:
        difficulties = json.load(f)

    with open("C_remaining_fixtures.json", "r") as f:
        fixtures = json.load(f)

    average_difficulties = dict()
    for team in difficulties.keys():
        num_fixtures = len(fixtures[team])
        for pos in ["Goalkeeper", "Defender", "Midfielder", "Forward"]:
            total_difficulty = 0
            for opponent in fixtures[team]:
                total_difficulty += difficulties[opponent[:-2]
                                                 ][pos][opponent[-1]]

            average_difficulty = round(total_difficulty / num_fixtures, 2)

            if team in average_difficulties.keys():
                average_difficulties[team]["difficulties"][pos] = average_difficulty
            else:
                average_difficulties[team] = {"num_fixtures": num_fixtures,
                                              "difficulties": {pos: average_difficulty}}

    with open("E_average_fixture_difficulties.json", "w") as f:
        json.dump(average_difficulties, f, indent=4)


if __name__ == "__main__":
    main()
