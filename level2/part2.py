games_dict = {}


def game_text_to_dict(text: str):
    game_id = (text.split(":")[0]).removeprefix("Game ")
    game_info = (text.split(":")[1]).strip().split("; ")
    game_info_list = []
    for viewing in game_info:
        game_info_list.append(viewing.split(", "))

    games_dict[game_id] = game_info_list


if __name__ == '__main__':

    with open('games.txt', 'r') as games_file:
        games = {}
        games_power_sum = 0
        for line in games_file:
            game_text_to_dict(line)
        for i in range(1, len(games_dict) + 1):
            print(i)
            max_blue = 0
            max_green = 0
            max_red = 0
            for viewing in games_dict[str(i)]:
                print(viewing)
                for view in viewing:
                    amount, color = view.split(" ")
                    if color == "blue" and int(amount) > max_blue:
                        max_blue = int(amount)
                    if color == "green" and int(amount) > max_green:
                        max_green = int(amount)
                    if color == "red" and int(amount) > max_red:
                        max_red = int(amount)
            print(f"Max blue {max_blue}, Max green {max_green}, Max red {max_red}")
            games_power_sum += (max_blue * max_green * max_red)
        print("The sum is", games_power_sum)
        print(sum(range(1, 100)))
