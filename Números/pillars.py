# **********************
# POSTES EN LA CARRETERA
# **********************


def run(num_pillars: int, gap_pillars: float, pillar_width: float) -> float:
    width = pillar_width * (num_pillars-2)
    gap = (gap_pillars * 100)c * (num_pillars -1)
    inter_distance = width + gap

    return inter_distance


if __name__ == '__main__':
    run(10, 5, 30)