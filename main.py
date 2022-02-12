
# main.py
from asyncio.log import logger
from ctypes import ArgumentError
from datetime import date, datetime
import sys
from typing import List
import logging
import logging.config

from league_results_processor.dtos.game_points import GamePoints
from league_results_processor.dtos.game_result import game_result
from league_results_processor.exceptions.invalid_arguments_exception import InvalidArgumentsException
from league_results_processor.file_objects.simple_game_results_line import simple_game_results_line
from league_results_processor.file_processors.simple_file_processor import simple_file_processor
from league_results_processor.file_readers.simple_file_reader import SimpleFileReader
from league_results_processor.file_writers.simple_file_writer import SimpleFileWriter
from league_results_processor.file_writers.simple_output_file_formatter import SimpleOutputFileFormatter
from league_results_processor.game_result_calculators.simple_game_result_calculator import SimpleGameResultCalculator
from league_results_processor.league_calculators.simple_league_table_calculator import SimpleLeagueTableCalculator

def get_logger(logfilename):
    config_file = ('log.config')
    logging.config.fileConfig(config_file, defaults={'logfilename': logfilename}, disable_existing_loggers=False)
    logger = logging.getLogger("main")
    return logger

date_time_now = datetime.now()
log_file_name = date_time_now.strftime("%d-%b-%Y") + "-app.log"

# logging.basicConfig(filename=log_file_name, filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

logger = get_logger(logfilename=log_file_name)

if __name__ == "__main__":
    try:
        print(f"Arguments count: {len(sys.argv)}")
        for i, arg in enumerate(sys.argv):
            print(f"Argument {i:>6}: {arg}")
        if len(sys.argv) <= 1:
            raise InvalidArgumentsException("Not enough arguments given ...")

        input_file_path = sys.argv[1]

        print("Reading file at path: " + input_file_path)
        logger.info("Reading file at path: " + input_file_path)
        file_reader = SimpleFileReader()
        input_file_lines: List[simple_game_results_line] = file_reader.read_file(input_file_path)

        print("Processing into usable objects ...")
        logger.info("Processing into game result objects ...")
        simple_game_calculator = SimpleGameResultCalculator()
        file_processor = simple_file_processor(simple_game_calculator)
        game_results = file_processor.process_file(input_file_objects=input_file_lines)

        print("Processing results into league table ...")
        logger.info("Processing results into league table ...")
        game_points = GamePoints(win_points=3, draw_points=1, loss_points=0)
        league_calculator = SimpleLeagueTableCalculator(game_points)
        league_table = league_calculator.get_league_table(game_results_list=game_results)

        print("Writing league table to output file ...")
        logger.info("Writing league table to output file ...")
        output_file_formatter = SimpleOutputFileFormatter()
        simple_file_writer = SimpleFileWriter(output_file_formatter)

        # datetime object containing current date and time
        date_time_now = datetime.now()
        dt_string = date_time_now.strftime("%d%m%Y_%H-%M-%S")
        output_file_path = "league_table_" + dt_string + ".txt"
        simple_file_writer.write_to_file(output_file_path=output_file_path, league_rows=league_table)

        print("Successfully processed league table ...")
        logger.info("Successfully processed league table ...")
    except Exception as e:
        logger.error("Unexpected error ocurred while processing file: " + e.message)


