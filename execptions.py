

class CoinError(Exception):
    
    coinsides = ['heads', 'tails']
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    
    def __str__(self) -> str:
        return f'The sides of a coin consist of {self.coinsides[0]} and {self.coinsides[1]}. Please type in "heads" or "tails"'
    
    def check(self, prompt):
        while True:
            value = input(prompt)
            try:
                if value not in self.coinsides:
                    raise CoinError
                else:
                    return value
            except CoinError:
                print(str(self))


