from pathlib import Path

ROOT_PATH = Path(__file__).parent
DATA_PATH = ROOT_PATH.joinpath("src", "data")
DATA_PATH2 = ROOT_PATH.joinpath("tests")
OPERATIONS_JSON_PATH = DATA_PATH.joinpath("operations.json")
TEST_OPERATIONS_PATH = DATA_PATH2.joinpath("test_operations.json")
