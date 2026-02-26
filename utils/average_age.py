import re


def parse_age_value(age_text: str):
    if not age_text:
        return None

    age_text = age_text.lower().strip()

    numbers = list(map(int, re.findall(r"\d+", age_text)))

    if not numbers:
        return None

    if len(numbers) >= 2:
        return (min(numbers) + max(numbers)) // 2

    return numbers[0]
