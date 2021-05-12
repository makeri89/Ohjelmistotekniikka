from repositories.score_repository import ScoreRepository
from ui.score_viewer import ScoreViewer
from levels.field_importer import get_keys


def open_table():
    score_repository = ScoreRepository()
    score_viewer = ScoreViewer(score_repository, get_keys())
    score_viewer.fire_up()
