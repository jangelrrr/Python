def run(hours: int, minutes: int, seconds: int) -> int:
    hour = hours * 3600
    minute = minutes * 60
    miliseconds = (hour + minute + seconds) * 1000
    return miliseconds

print(run(0, 1, 1))