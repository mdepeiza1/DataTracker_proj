import json
import requests
from types import SimpleNamespace


class VideoGames:
    def __init__(self, _id, rank, name, platform, year, genre, publisher, naSales, euSales, jpSales, otherSales,
                 globalSales, __v):
        self._id = _id
        self.rank = rank
        self.name = name
        self.platform = platform
        self.year = year
        self.genre = genre
        self.publisher = publisher
        self.naSales = naSales
        self.euSales = euSales
        self.jpSales = jpSales
        self.otherSales = otherSales
        self.globalSales = globalSales
        self.__v = __v

    @staticmethod
    def video_games_decoder(obj):
        return VideoGames(obj['_id'], obj['rank'], obj['platform'], obj['year'], obj['genre'], obj['publisher'],
                          obj['naSales'], obj['euSales'], obj['jpSales'], obj['otherSales'], obj['globalSales'],
                          obj['__v'])



#response = requests.get('https://api.dccresource.com/api/games')
response = requests.get('https://api.dccresource.com/api/games')

#json_data_dict = json.loads(response)

videogames = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))


###videogames = VideoGames.video_games_decoder(json_data_dict)

##Used this to verify that Get request works properly
###for videogame in videogames:
###    print(videogame.name)
