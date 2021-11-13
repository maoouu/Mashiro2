import json
import traceback
import os
from replit import Database


def config(filename: str = "config"):
    """Fetches default config file"""
    try:
        with open(f"{filename}.json", encoding="utf-8") as data:
            return json.load(data)

    except FileNotFoundError:
        raise FileNotFoundError("Config json file not found.")


def traceback_maker(err, advanced_traceback_mode: bool = False):
    """Traceback for code debugging"""
    _traceback = "".join(traceback.format_tb(err.__traceback__))
    error = ("```py\n{1}{0}: {2}\n```").format(type(err).__name__, _traceback, err)

    return error if advanced_traceback_mode else f"{type(err).__name__} : {err}"


def database(database_url: str = os.environ["REPLIT_DB_URL"]):
    """Fetches database class"""
    try:
        return Database(db_url=database_url)
    except KeyError:
        raise KeyError("Environment variable 'REPLIT_DB_URL' is missing.")
