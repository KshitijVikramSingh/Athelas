def _log_list(array: list) -> None:
    for i in range(len(array)):
        print(f'{i + 1}. {array[i]}')


def _log_dict(dictionary: dict) -> None:
    for key in dictionary.keys():
        print(f'{key}: {dictionary[key]}')

    
def log(*args) -> None:
    """
    The `log` function is a helper function that prints the arguments passed to it, handling lists and
    dictionaries separately.
    """
    for arg in args:
        if isinstance(arg, list):
            _log_list(arg)
        elif isinstance(arg, dict):
            _log_dict(arg)
        else:
            print(arg)

