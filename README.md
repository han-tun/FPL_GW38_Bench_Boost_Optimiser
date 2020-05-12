# Fantasy Premier League Gameweek 38 Bench Boost Optimiser

Due to the current COVID-19 pandemic, there is an unprecedented situation with regards to the English Premier League as nobody knows if or when the remaining fixtures are going to be played. Since the matches have been postponed, weekly deadlines have been passing by on FPL with no games being played, meaning that all remaining fixtures will take place after the Gameweek 38 deadline. 

It is unknown what FPL will do about this, but there is a chance that all remaining games will be a part of a huge Gameweek 38. In this case, it would be a major advantage if you could play your bench boost chip (your bench players score points too) for this gameweek.

This optimiser sets out to find what would be the ideal team to have going into this jumbo Gameweek 38 so that you can plan for it accordingly.

# Usage

The important files in this repository are the three marked with H, I, and J. 

 - H is where the 'score' that is given to players is defined, and is what will be maximised by the optimiser. It currently takes into account a player's points per game, the proportion of matches they've played in, and the average difficulty of their remaining fixtures for their particular position. This is by no means the best function for a score, so feel free to change it as you see fit.
 - I is the csv file that is used by the optimiser. This doesn't need to be touched.
 - J is the optimiser. It is a slightly edited version of the optimiser created by Rasmus Christensen. The original code is available [here](https://github.com/wiscostret/optimize_fpl). You will need to edit the filepath variable so that it points to I, and edit the variables in the call to the model function. These are both found near the end of the file.

# Result

For a budget of 101.5m, the optimiser suggests the following team:
```markdown
| pos | team           | name             | cost | score |
|-----|----------------|------------------|------|-------|
| G   | Leicester      | Schmeichel       | 5.4  | 11.65 |
| G   | Watford        | Foster           | 4.9  | 10.9  |
| D   | Liverpool      | Alexander-Arnold | 7.8  | 16.51 |
| D   | Liverpool      | van Dijk         | 6.5  | 14.03 |
| D   | Wolves         | Doherty          | 6.3  | 13.65 |
| D   | Sheffield Utd  | Baldock          | 5.1  | 13.42 |
| D   | Sheffield Utd  | Stevens          | 5.2  | 12.84 |
| M   | Man City       | De Bruyne        | 10.6 | 23.03 |
| M   | Man City       | Mahrez           | 8.5  | 15.66 |
| M   | Wolves         | Traoré           | 5.7  | 12.32 |
| M   | Aston Villa    | Grealish         | 6.4  | 12.11 |
| M   | Norwich        | Cantwell         | 4.7  | 11.45 |
| F   | Arsenal        | Aubameyang       | 11.1 | 17.8  |
| F   | Wolves         | Jiménez          | 8.1  | 15.11 |
| F   | Crystal Palace | Ayew             | 5.2  | 10.95 |
```
## Notes
 - It is not confirmed that all remaining fixtures will be moved to Gameweek 38. Playing the bench boost chip is not guaranteed to be a good decision, but the upside of having a bench boost for such a gameweek is huge for a relatively small downside.
 - The function that scores each player is flawed because it doesn't take into account players that have moved to their club in January.
 - You can not play two chips in one gameweek, so it is too late to wildcard during GW37 and bench boost for GW38
 - The files are named like they are so that it is easier to follow how the data was gathered.
