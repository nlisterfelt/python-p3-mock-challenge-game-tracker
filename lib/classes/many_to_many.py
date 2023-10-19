class Game:
    all = []

    def __init__(self, title):
        self.title = title
        Game.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title

    def results(self):
        return [result for result in Result.all if self == result.game]

    def players(self):
        unique_players = []
        for result in Result.all:
            if self == result.game and result.player not in unique_players:
                unique_players.append(result.player)
        return unique_players

    def average_score(self, player):
        player_scores = [result.score for result in self.results() if result.player == player]
        total_scores = sum(player_scores)
        num_scores = len(player_scores)
        return total_scores / num_scores

class Player:
    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username)>1 and len(username)<17:
            self._username = username

    def results(self):
        return [result for result in Result.all if self == result.player]

    def games_played(self):
        unique_games = []
        for result in Result.all:
            if self == result.player and result.game not in unique_games:
                unique_games.append(result.game)
        return unique_games

    def played_game(self, game):
        if isinstance(game, Game) and game in self.games_played():
            return True
        else:
            return False 

    def num_times_played(self, game):
        count = 0
        for result in Result.all:
            if result.game == game and result.player == self:
                count += 1
        return count

class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if isinstance(score, int) and score>0 and score<5001 and not hasattr(self, "score"):
            self._score = score

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game

game_1 = Game("Skribbl.io")
game_2 = Game("Scattegories")
player_1 = Player("Saaammmm")
player_2 = Player("ActuallyTopher")
Result(player_1, game_1, 2000)
Result(player_1, game_2, 19)
Result(player_1, game_1, 1900)
Result(player_2, game_2, 9)

print(player_1.num_times_played(game_1))