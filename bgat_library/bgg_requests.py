from datetime import datetime, timedelta

import requests
import bs4


def bgg_date_format(date: datetime):
    return datetime.strftime(date, "%Y-%m-%d")


def get_bga_game_list():
    """Gets a geeklist containing all games currently on Board Game Arena."""
    result = requests.get("https://www.boardgamegeek.com/xmlapi2/geeklist/252354")
    return result.text


def get_user_plays(username, mindate: datetime = None, maxdate: datetime = None):
    """Gets all plays recorded by a user on BGG between a pair of dates."""
    req_text = f"https://www.boardgamegeek.com/xmlapi2/plays?username={username}"

    if mindate is not None:
        if (maxdate is not None and maxdate < mindate) or mindate > datetime.now():
            raise ValueError("Must be a valid date range")
        req_text += f"&mindate={bgg_date_format(mindate)}"

    if maxdate is not None:
        req_text += f"&maxdate={bgg_date_format(maxdate)}"

    result = requests.get(req_text)

    return result.text
