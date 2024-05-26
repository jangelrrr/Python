# ****************
# CONTANDO VOCALES
# ****************


def run(text: str) -> int:
    num_vowels = 0
    for letter in text:
        if letter in 'aeiouAEIOUÓóá':
            num_vowels += 1
    return num_vowels


if __name__ == '__main__':
    run('El camión chocó contra el árbol')