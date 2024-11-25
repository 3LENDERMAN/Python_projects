from ib111 import week_03  # noqa


# V tomto domácím úkolu si naprogramujete zjednodušenou variantu hry «2048¹».
# Na rozdíl od původní hry budeme uvažovat jen jednorozměrný hrací plán,
# tj. jeden řádek.
#
# ¹ ‹https://play2048.co/›
#
# Hrací plán budeme reprezentovat pomocí seznamu nezáporných celých čísel;
# nuly budou představovat prázdná místa.
# Například seznam ‹[2, 0, 0, 2, 4, 8, 0]› reprezentuje následující situaci:
#
#  ┌───┬───┬───┬───┬───┬───┬───┐
#  │ 2 │   │   │ 2 │ 4 │ 8 │   │
#  └───┴───┴───┴───┴───┴───┴───┘
#
# Základním krokem hry je posun doleva nebo doprava. Při posunu se všechna
# čísla „sesypou“ v zadaném směru, přičemž dvojice stejných číslic se sečtou.
# Posunem doleva se tedy uvedený seznam změní na ‹[4, 4, 8, 0, 0, 0, 0]›.
#
# Abyste si hru mohli vyzkoušet (poté, co úlohu vyřešíte), je vám k dispozici
# soubor ‹game_2048.py›, který vložte do stejného adresáře, jako je soubor
# s vaším řešením, případně jej upravte dle komentářů na jeho začátku
# a spusťte. Hra se ovládá šipkami doleva a doprava, ‹R› hru resetuje
# a ‹Q› ukončí.
#
# Napište proceduru ‹slide›, která provede posun řádku reprezentovaného
# seznamem ‹row›, a to buď doleva (pokud má parametr ‹to_left› hodnotu ‹True›)
# nebo doprava (pokud má parametr ‹to_left› hodnotu ‹False›). Procedura přímo
# modifikuje parametr ‹row› a vrací ‹True›, pokud posunem došlo k nějaké
# změně; v opačném případě vrací ‹False›.

def slide(row, to_left) -> bool:
    if row == []: return False
    changed = False
    x = -1; start = (len(row) - 1); end = 0
    if to_left: x = 1; start = 0; end = (len(row) - 1) 
    for i in range(start, end, x):
        val = row[i]
        if val != 0:
            for j in range(i + x, end, x):
                if val == row[j]:
                    row[i] = val * 2
                    row[j] = 0
                    changed = True
                    break
                elif row[j] != 0:
                    break
    remove_zeros(row, to_left)
    return changed

def remove_zeros(row: list[int], to_left: bool) -> None:
    change = True
    x = -1; start = (len(row) - 1); end = 0
    if to_left: x = 1; start = 0; end = (len(row) - 1) 
    while change:
        temp = row.copy()
        for i in range(start, end, x):
            if row[i] == 0 and row[i + x] != 0:
                row[i] = row[i + x]
                row[i + x] = 0 
        if temp == row: change = False

def main():
    row = [0, 2, 2, 0]
    assert slide(row, True)
    assert row == [4, 0, 0, 0]

    row = [2, 2, 2, 2, 2]
    assert slide(row, False)
    assert row == [0, 0, 2, 4, 4]

    row = [2, 0, 0, 2, 4, 2, 2, 2]
    assert slide(row, True)
    assert row == [4, 4, 4, 2, 0, 0, 0, 0]

    row = [3, 0, 6, 3, 3, 3, 6, 0, 6]

    assert slide(row, False)
    assert row == [0, 0, 0, 0, 3, 6, 3, 6, 12]

    row = [16, 8, 4, 2, 0, 0, 0]
    assert not slide(row, True)
    assert row == [16, 8, 4, 2, 0, 0, 0]


if __name__ == '__main__':
    main()
