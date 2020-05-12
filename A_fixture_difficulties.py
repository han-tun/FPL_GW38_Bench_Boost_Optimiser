import asyncio
import aiohttp
from fpl import FPL
import json


async def main():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        # fixture difficulty rating
        fdr = await fpl.FDR()

    '''
    make our own dict to round the difficulties to 2 places and capitalise the position names. The saved json will have the following format:
    {
    "Norwich": {
        "Goalkeeper": {
            "H": 2.54,
            "A": 3.4
        },
        "Defender": {
            "H": 1.0,
            "A": 2.69
        },
        "Midfielder": {
           ...


    these fixture difficulties are calculated by the fpl package by scaling the average points conceded per position between 1 and 5,
    where a value of 1 corresponds to the team that conceded the most points to that position, and 5 the least.
    '''

    cleaned_data = dict()
    for team in fdr.keys():
        cleaned_data[team] = {}
        for pos in ['Goalkeeper', 'Defender', 'Midfielder', 'Forward']:
            cleaned_data[team][pos] = {}
            cleaned_data[team][pos]["H"] = round(
                fdr[team][pos.lower()]["H"], 2)
            cleaned_data[team][pos]["A"] = round(
                fdr[team][pos.lower()]["A"], 2)

    with open("B_fixture_difficulties.json", "w") as f:
        json.dump(cleaned_data, f, indent=4)


if __name__ == '__main__':
    # using this instead of ``asyncio.run(main())`` as there is a problem when using asyncio.run on windows
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
