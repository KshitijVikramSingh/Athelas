import asyncio
from lichess.lichess import LichessRequests
from beautifullogs.beautifullogs import log

lichess = LichessRequests()

def print_top_50_classical_players() -> None:
    """
    Retrieves the top 50 classical players from lichess and prints their usernames.
    """
    players = lichess.get_top_50_classical_players()
    usernames = [player['username'] for player in players]
    log(usernames)


def print_last_30_day_rating_for_top_player() -> None:
    """
    Retrieves the rating history for the top player in the last 30 days and prints it.
    """
    players = lichess.get_top_50_classical_players()
    top_player = players[0]['username']

    rating_history = lichess.get_parsed_30_day_rating_history_for_classical_player(top_player)
    log(rating_history)


def generate_rating_csv_for_top_50_classical_players() -> None:
    """
    Generates a CSV file containing the rating history of the top 50 classical players on lichess.
    """
    players = lichess.get_top_50_classical_players()

    top_player = players[0]['username']
    rating_history = lichess.get_parsed_30_day_rating_history_for_classical_player(top_player)

    dates = rating_history.keys()
    top_player_ratings = rating_history.values()

    with open('top_classical_players_ratings.csv', 'w', encoding='utf-8') as csvfile:
        csvfile.write(f'username,{",".join(dates)}\n')

        csvfile.write(f'{top_player},{",".join(map(str, top_player_ratings))}\n')
        players = players[1:]

        for player in players:
            username = player['username']
            rating_history = lichess.get_parsed_30_day_rating_history_for_classical_player(username)
            ratings = rating_history.values()

            csvfile.write(f'{username},{",".join(map(str, ratings))}\n')


async def async_generate_rating_csv_for_top_50_classical_players() -> None:
    """
    Generates a CSV file containing the rating history of the top 50 classical players on lichess, asynchronously.
    This function is around 3.5 times faster than the synchronous version.
    """
    def fetch_rating_history(username):
        return lichess.get_parsed_30_day_rating_history_for_classical_player(username)

    players = lichess.get_top_50_classical_players()

    top_player = players[0]['username']
    rating_history = await loop.run_in_executor(None, fetch_rating_history, top_player)

    dates = rating_history.keys()
    top_player_ratings = rating_history.values()

    with open('top_classical_players_ratings.csv', 'w', encoding='utf-8') as csvfile:
        csvfile.write(f'username,{",".join(dates)}\n')
        csvfile.write(f'{top_player},{",".join(map(str, top_player_ratings))}\n')

        players = players[1:]

        tasks = [loop.run_in_executor(None, fetch_rating_history, player['username']) for player in players]
        rating_histories = await asyncio.gather(*tasks)

        for player, rating_history in zip(players, rating_histories):
            username = player['username']
            ratings = rating_history.values()

            csvfile.write(f'{username},{",".join(map(str, ratings))}\n')


loop = asyncio.get_event_loop()
loop.run_until_complete(async_generate_rating_csv_for_top_50_classical_players())