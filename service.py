from dataclasses import dataclass


@dataclass
class Service:
    qozje: int = 48
    mtaav: int = 223

    def total(self):
        return self.qozje + self.mtaav


if __name__ == "__main__":
    x = Service()
    print(x.total())
