import json


def config(filename: str = "config"):
  """ Fetch default config file """
  try:
    with open(f"{filename}.json", encoding='utf-8') as data:
      return json.load(data)

  except FileNotFoundError:
    raise FileNotFoundError("Config json file not found.")