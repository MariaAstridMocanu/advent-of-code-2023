games_dict = {}


def game_text_to_dict(text: str):
    game_id = (text.split(":")[0]).removeprefix("Game ")
    game_info = (text.split(":")[1]).strip().split("; ")
    game_info_list = []
    for viewing in game_info:
        game_info_list.append(viewing.split(", "))

    games_dict[game_id] = game_info_list


if __name__ == '__main__':
    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14

    with open('games.txt', 'r') as games_file:
        games = {}
        impossible_game = False
        possible_game_id_sum = 0
        for line in games_file:
            game_text_to_dict(line)
        for i in range(1, len(games_dict) + 1):
            print(i)
            for viewing in games_dict[str(i)]:
                print(viewing)
                for view in viewing:
                    amount, color = view.split(" ")
                    if color == "blue" and int(amount) > MAX_BLUE:
                        impossible_game = True
                    if color == "green" and int(amount) > MAX_GREEN:
                        impossible_game = True
                    if color == "red" and int(amount) > MAX_RED:
                        impossible_game = True
            if not impossible_game:
                print("Adding Correct ID:", i)
                possible_game_id_sum += int(i)
            else:
                print("BAD ID:", i)
                impossible_game = False
        print("The sum is", possible_game_id_sum)
        print(sum(range(1, 100)))
