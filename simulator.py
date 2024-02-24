import random
from tqdm import tqdm

class Game():

    def __init__(self, N: int) -> None:
        """
        N should be a positive even integer.
        1 represents heads, 0 tails
        """
        self.N = N
        self.count = 0
        self.heads = 0
        self.payout = 0

        self.game = []
        self.won = None
        assert self.N > 0 and self.N % 2 == 0
    
    def roll(self) -> None:
        rand = random.random()
        if rand > 0.5:
            self.game.append(1)
            self.heads += 1
        else:
            self.game.append(0)
        self.count += 1

    def simulate(self) -> None:
        while self.count < self.N:
            self.roll()
            tails = self.count - self.heads
            if self.heads < tails:
                self.won = False
                self.payout = 0
                return
            
            tails = self.count - self.heads
            payout = self.heads - tails
            assert payout >= 0
            self.payout += payout
        
        tails = self.count - self.heads
        self.won =  self.heads == tails

def simulate_games(N: int, num_games: int) -> list:
    """
    Returns a list of simulated games.
    """
    games = []
    for i in tqdm(range(num_games)):
        games.append(Game(N=N))
        games[i].simulate()
    
    return games

def get_win_prob(N: int, num_games: int) -> None:
    games = simulate_games(N=N, num_games=num_games)

    total_won = 0
    for game in games:
        if game.won:
            total_won += 1
    win_prob = total_won/len(games)

    print(f"N={N}, num_games={num_games}")    
    print(f"Probability of winning: {win_prob}\n")


def get_unique_wins(N: int, num_games: int):
    games = simulate_games(N=N, num_games=num_games)

    game_lists = set()
    for game in games:
        if game.won:
            game_lists.add(tuple(game.game))

    game_lists = list(game_lists)
    game_strs = []
    for tup in game_lists:
        game_str = str(tup)
        for repl in ["(", ")", " ", ","]:
            game_str = game_str.replace(repl, "")
        game_str = game_str.replace("1", "H")
        game_str = game_str.replace("0", "T")
        game_strs.append(game_str)

    print(f"N={N}, num_games={num_games}, # winning combos={len(game_strs)}")    
    for game_str in sorted(game_strs):
        print(game_str)

def get_expected_payout(N: int, num_games: int) -> None:
    games = simulate_games(N=N, num_games=num_games)
    total_payout = 0
    # payouts = []
    for game in games:
        total_payout += game.payout
        # payouts.append(game.payout)
    expected_payout = total_payout/len(games)
    

    print(f"N={N}, num_games={num_games}")
    print(f"Expected payout: {expected_payout}\n")
    # print(f"Payouts:  {payouts}\n")


def main():
    # game = Game(N=6)
    # game.simulate()
    # print("gg")

    # Problem a
    # get_win_prob(6, 10000000)

    # Problem b
    # get_expected_payout(N=6, num_games=10000000)

    # Problem c
    get_win_prob(1000, 1000000)

    # Problem d
    # get_expected_payout(N=1000, num_games=10000000)


    # get_win_prob(N=8, num_games=1000000)
    # get_expected_payout(N=6, num_games=10000000)
    # get_win_prob(N=1000, num_games=10000000)
    # get_expected_payout(N=1000, num_games=1000000)

    # get_unique_wins(N=10, num_games=1000000)


if __name__ == "__main__":
    main()