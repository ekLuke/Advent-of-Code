import re

games_lines = open("input.txt").read().split("\n")
regex = "(?:\s(?P<number>\d{1,3})\s(?P<color>[^,;]+)(?:,)?)"


class Turn:
    def __init__(self, red=0, green=0, blue=0): self.red, self.green, self.blue = (red, green, blue)


class Game:
    cb = Turn(12, 13, 14)

    def __init__(self): self.IsPossible, self.Turns = (False, list())

    def max_turn(self):
        red, green, blue = (0, 0, 0)
        for turn in self.Turns:
            if turn.red > red: red = turn.red
            if turn.green > green: green = turn.green
            if turn.blue > blue: blue = turn.blue

        return red * green * blue

    def check_turns(self):
        self.IsPossible = all((turn.red <= self.cb.red and turn.green <= self.cb.green and turn.blue <= self.cb.blue) for turn in self.Turns)


games = list()
for game_lines in games_lines:
    game_line = game_lines.split(";")
    #print(f"game lines => {game_lines}")
    game = Game()
    for turn_line in game_line:
        #print(turn_line)
        game.Turns.append(Turn())
        for set_value in re.findall(regex, turn_line):
            game.Turns[-1].__setattr__(set_value[1], int(set_value[0]))

    game.check_turns()
    games.append(game)

print(sum([games.index(games_count)+1 for games_count in games if games_count.IsPossible]))
print(sum(games_count.max_turn() for games_count in games))
