from networking.networking import HTTPRequests
import datetime

def _get_date_from_rating_array(rating) -> str:
    [year, month, day] = [int(rating[0]), int(rating[1]) + 1, int(rating[2])]
    return datetime.datetime(year, month, day).date().isoformat()


def _parse_rating_history_by_dates(rating_history) -> dict:
    return {
        _get_date_from_rating_array(rating): int(rating[3])
        for rating in rating_history
    }


def _get_last_known_rating_before_date(parsed_rating_history, date) -> int:
    for day in reversed(parsed_rating_history):
        if day <= date:
            return parsed_rating_history[day]
    return None


def _parse_rating_history_for_last_n_days(rating_history, n) -> dict:
    parsed_rating_history = _parse_rating_history_by_dates(rating_history)
    
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    last_n_days = [yesterday - datetime.timedelta(days=i) for i in range(n)]
    last_n_days = [day.isoformat() for day in last_n_days]

    last_known_rating = _get_last_known_rating_before_date(parsed_rating_history, last_n_days[-1])
    result = {}

    for day in reversed(last_n_days):
        if day in parsed_rating_history:
            last_known_rating = parsed_rating_history[day]
        result[day] = last_known_rating if last_known_rating is not None else None

    return result


class LichessRequests:
    def __init__(self) -> None:
        self.instance = HTTPRequests('https://lichess.org/api')

    def _get_top_players(self, number: int, category: str) -> list:
        return self.instance.get(f'/player/top/{number}/{category}')['users']
    
    def get_top_50_classical_players(self) -> list:
        """
        The function returns a list of the top 50 classical players.
        
        Returns:
            list: a list of the top 50 classical players.
        """
        return self._get_top_players(50, 'classical')
    
    def _get_rating_history_for_player(self, username: str) -> list:
        return self.instance.get(f'/user/{username}/rating-history')
    
    def _get_rating_history_for_player_by_format(self, username: str, format: str) -> list:
        history = self._get_rating_history_for_player(username)
        return [rating['points'] for rating in history if rating['name'] == format][0]
    
    def _get_rating_history_for_classical_player(self, username: str) -> list:
        return self._get_rating_history_for_player_by_format(username, 'Classical')
    
    def get_parsed_30_day_rating_history_for_classical_player(self, username: str) -> dict:
        """
        The function returns the parsed rating history for a classical player for the last 30 days.
        
        Args:
            username (str): The username of the player.

        Returns:
            dict: a dictionary containing the rating history for the last 30 days.
        """
        return _parse_rating_history_for_last_n_days(self._get_rating_history_for_classical_player(username), 30)
    