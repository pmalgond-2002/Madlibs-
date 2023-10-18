from sample_madlibs import hp, coding, zombie, hungergames
import random

if __name__ == "__main__":
    m = random.choice([hp, coding, zombie, hungergames])
    m.madlib()