from Base import JokeApiBase
import requests


class DadJokes(JokeApiBase):
    def __init__(self, apikey, apihost):
        self.apikey = apikey
        self.apihost = apihost

    def get_random_joke(self):
        headers = {
            "X-RapidAPI-Key": self.apikey,
            "X-RapidAPI-Host": self.apihost
        }
        url = "https://dad-jokes.p.rapidapi.com/random/joke"
        results = requests.request("GET", url, headers=headers)
        results_json = results.json()
        setup = results_json["body"][0]["setup"]
        punchline = results_json["body"][0]["punchline"]
        return setup + " " + punchline

class ChuckNorris(JokeApiBase):
    def __init__(self, apikey, apihost):
        self.apikey = apikey
        self.apihost = apihost

    def get_random_joke(self):
        headers = {
            "accept": "application/json",
            "X-RapidAPI-Key": self.apikey,
            "X-RapidAPI-Host": self.apihost
        }
        url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"
        results = requests.request("GET", url, headers=headers)
        results_json = results.json()
        return results_json["value"]

class JokesByApiNinjas(JokeApiBase):
    def __init__(self, apikey, apihost):
        self.apikey = apikey
        self.apihost = apihost

    def get_random_joke(self):
        headers = {
            "X-RapidAPI-Key": self.apikey,
            "X-RapidAPI-Host": self.apihost
        }
        url = "https://jokes-by-api-ninjas.p.rapidapi.com/v1/jokes"
        results = requests.request("GET", url, headers=headers)
        results_json = results.json()
        return results_json[0]["joke"]

apikey = "80ecd0a414mshc27bcad53002d39p1b0f5ajsnc508eba85232"
apihost_dadjokes = "dad-jokes.p.rapidapi.com"
apihost_chunknorris = "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
apihost_JokesbyAPI_Ninjas = "jokes-by-api-ninjas.p.rapidapi.com"
if __name__ == "__main__":
    joke1 = DadJokes(apikey, apihost_dadjokes)
    joke2 = ChuckNorris(apikey, apihost_chunknorris)
    joke3 = JokesByApiNinjas(apikey, apihost_JokesbyAPI_Ninjas)
    abj1 = joke1.get_random_joke()
    abj2 = joke2.get_random_joke()
    abj3 = joke3.get_random_joke()
    print('1-',abj1)
    print('...........................')
    print('2-',abj2)
    print('...........................')
    print('3-',abj3)