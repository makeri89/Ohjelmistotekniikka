from score_repository import ScoreRepository

score = ScoreRepository()


def print_all_scores():
    score.print_scores()


if __name__ == '__main__':
    print_all_scores()
