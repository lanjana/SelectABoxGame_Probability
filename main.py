import random
import matplotlib.pyplot as plt


class SelectBoxGame:
    def __init__(self, game_size, strategy) -> None:
        self.game_size = game_size
        self.strategy = strategy

    def play(self):
        self.init_game()

        # User select a box numebr, completly random.
        initial_guess = random.randint(1, self.game_size)

        # Another box number will be offered to the user and all other boxes will be opened as empty choices.
        offered_box = random.randint(1, self.game_size)
        if self.win_checker(initial_guess):
            while offered_box == initial_guess:
                offered_box = random.randint(1, self.game_size)
        else:
            offered_box = self.win_number

        # User sterategy, user can select to change the box or keep their inital guess
        if self.strategy == 0:
            final_choice = initial_guess
        elif self.strategy == 1:
            final_choice = offered_box

        return self.win_checker(final_choice)

    def init_game(self):
        self.win_number = random.randint(1, self.game_size)

    def win_checker(self, selected_number):
        if selected_number == self.win_number:
            return True
        return False


class StrategyChechker:
    def __init__(self, game_size, repeat) -> None:
        self.repeat = repeat
        self.keep_inital_strategy = SelectBoxGame(game_size, 0)
        self.keep_offer_strategy = SelectBoxGame(game_size, 1)
        self.run_test()

    def run_test(self):
        self.inital_strategy_wins, self.offer_strategy_wins, flip_head = 0, 0, 0
        for i in range(self.repeat):
            self.inital_strategy_wins += int(self.keep_inital_strategy.play())
            self.offer_strategy_wins += int(self.keep_offer_strategy.play())

            # Consider 1 as head.
            flip_head += random.randint(0, 1)

        self.plot_results(
            self.repeat, self.inital_strategy_wins, self.offer_strategy_wins, flip_head
        )

    def plot_results(self, total_rounds, init_strategy_wins, offer_strategy_wins, test):
        strategies = ["Initial Strategy", "Offer Strategy", "Flip Coin Test"]
        wins = [init_strategy_wins, offer_strategy_wins, test]

        fig, ax = plt.subplots()

        bar_positions = range(len(strategies))

        ax.bar(
            bar_positions,
            [total_rounds] * len(strategies),
            color="lightgray",
            edgecolor="black",
            label="Total Rounds",
        )

        bars = ax.bar(
            bar_positions,
            wins,
            color=["blue", "green", "red"],
            edgecolor="black",
            label="Wins",
        )

        ax.set_xlabel("Strategy")
        ax.set_ylabel("Rounds")
        ax.set_title("Comparison of Strategy Wins")
        ax.set_xticks(bar_positions)
        ax.set_xticklabels(strategies)

        for bar, win in zip(bars, wins):
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                height - 0.2 * height,
                f"{round(win/total_rounds*100)}%",
                ha="center",
                va="bottom",
                color="White",
                fontweight="bold",
            )

        # ax.legend()
        plt.show()


# try1 = StrategyChechker(100, 50000)


win = 0
for i in range(total := 100000):
    first = random.randint(0, 1)
    second = random.randint(0, 1)

    if first == 0:
        guess = 0
    else:
        guess = 1

    if guess == second:
        win += 1


print(win / total)
