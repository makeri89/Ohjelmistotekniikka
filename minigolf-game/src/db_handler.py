from repositories.score_repository import ScoreRepository

score_repository = ScoreRepository()


def print_all_scores():
    all_scores = score_repository.find_all()
    for score in all_scores:
        print(f'level: {score[0]}, player: {score[1]}, score: {score[2]}')


if __name__ == '__main__':
    print_all_scores()
