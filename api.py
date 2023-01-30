import requests


class Search:
    def __init__(self, API_KEY, CSE_ID):
        self.API_KEY = API_KEY
        self.CSE_ID = CSE_ID

    def google_spell(self, query):
        try:
            res = requests.get(
                f"https://www.googleapis.com/customsearch/v1?key={self.API_KEY}&cx={self.CSE_ID}&q={query}"
            )
            if "spelling" in res.json():
                return res.json()["spelling"]["correctedQuery"]
            else:
                return "No Correction"
        except KeyError as e:
            print(e)
