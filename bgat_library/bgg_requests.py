import requests
import bs4

def get_bga_game_list():
    """Gets a geeklist containing all games currently on Board Game Arena."""
    result = requests.get('https://www.boardgamegeek.com/xmlapi2/geeklist/252354')
    return result.text

def get_user_plays(username, mindate=None, maxdate=None):
    """Gets all plays recorded by a user on BGG between a pair of dates."""
    req_text = f"https://www.boardgamegeek.com/xmlapi2/plays?username={username}"
    if mindate is not None:
        req_text += f"&mindate={mindate}"
    if maxdate is not None:
        req_text += f"&maxdate={maxdate}"
    
    result = requests.get(
        req_text
    )

    return result.text
