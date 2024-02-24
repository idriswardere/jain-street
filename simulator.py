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


def get_expected_payout(N: int, num_games: int) -> None:
    games = simulate_games(N=N, num_games=num_games)
    total_payout = 0
    for game in games:
        total_payout += game.payout
    expected_payout = total_payout/len(games)

    print(f"N={N}, num_games={num_games}")
    print(f"Expected payout: {expected_payout}\n")


def main():
    # game = Game(N=6)
    # game.simulate()
    # print("gg")

    # Problem a
    # get_win_prob(6, 1000000)

    # get_win_prob(N=8, num_games=1000000)
    get_expected_payout(N=6, num_games=1000000)


if __name__ == "__main__":
    main()