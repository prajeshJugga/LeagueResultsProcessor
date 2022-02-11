from typing import List
from league_results_processor.dtos.dto import DTO
from league_results_processor.file_objects.ifile_object import ifile_object
from league_results_processor.game_result_calculators.igame_result_calculator import IGameResultCalculator

class ifile_processor:
    """docstring for ifile_processor."""

    def __init__(self, game_calculator: IGameResultCalculator):
        self.game_result_calculator = game_calculator

    def process_file(self, input_file_objects: List[ifile_object]) -> List[object]:
        pass
