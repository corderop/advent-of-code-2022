from enum import Enum


class Play(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"


class Points(Enum):
    WIN = 6
    DRAW = 3
    LOST = 0


PLAY_POINTS = {
    Play.ROCK.value: 1,
    Play.PAPER.value: 2,
    Play.SCISSORS.value: 3,
}

WINNER_AGAINST = {
    Play.ROCK.value: Play.SCISSORS.value,
    Play.PAPER.value: Play.ROCK.value,
    Play.SCISSORS.value: Play.PAPER.value,
}

LOSER_AGAINST = {value: key for key, value in WINNER_AGAINST.items()}


class Results(Enum):
    WIN = "WIN"
    DRAW = "DRAW"
    LOST = "LOST"


RESULT_BY_CODE = {
    "X": Results.LOST.value,
    "Y": Results.DRAW.value,
    "Z": Results.WIN.value,
}
