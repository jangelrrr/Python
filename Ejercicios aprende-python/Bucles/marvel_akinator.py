# *******************************
# ADIVINANDO PERSONAJES DE MARVEL
# *******************************


def run(can_fly: bool, is_human: bool, has_mask: bool) -> str:
    if can_fly:
        if is_human:
            if has_mask:
                return 'Ironman'
            else:
                return 'Captain Marvel'
        elif not is_human:
            if has_mask:
                return 'Ronan Accuser'
            else:
                return 'Vision'
    elif not can_fly:
        if is_human:
            if has_mask:
                return 'Spiderman'
            else:
                return 'Hulk'
        elif not is_human:
            if has_mask:
                return 'Black Bolt'
            else:
                return 'Thanos'


if __name__ == '__main__':
    run(True, True, True)