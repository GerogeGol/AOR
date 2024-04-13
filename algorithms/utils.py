def compare(str1: str, str2: str) -> tuple[bool, int]:
    if len(str1) != len(str2):
        return False, 1

    counter = 0
    for a, b in zip(str1, str2):
        counter += 1
        if a != b:
            return False, counter
    return True, counter


def compare_builtin(str1: str, str2: str) -> tuple[bool, int]:
    return str1 == str2, len(str1)
