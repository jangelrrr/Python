#calcular milisegundos dando un determinado tiempo
def run(hours: int, minutes: int, seconds: int) -> int:
    hour = hours * 3600
    minute = minutes * 60
    miliseconds = (hour + minute + seconds) * 1000
    return miliseconds

print(run(10, 45, 30))