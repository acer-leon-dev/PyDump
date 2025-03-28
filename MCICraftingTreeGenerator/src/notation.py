"""Functions for representing numbers in Money Clicker Incremental """
import math

# Dysfunctional
# def letter(n):
#     frac, whole = math.modf(n)
#     whole_str = str(round(whole))
#
#     zeros = len(whole_str) - 1
#     u1 = zeros // 3
#
#     if u1 == 0 or u1 == 1:
#         coeff = whole_str
#         frac_str = str(round(frac * 100))
#         if len(frac_str) == 1:
#             frac_str = '0' + frac_str
#         coeff += ('.' + frac_str) if frac_str != '0' else ''
#     else:
#         u2 = zeros % 3
#         coeff = whole_str[:u2 + 1] + '.' + whole_str[u2 + 1:u2 + 3]
#         p = len(coeff) - 1
#         if coeff[p] == '0':
#             coeff = coeff[:p]
#
#     abbreviations = ("", "", 'M', 'B', 'T', 'Qd', "Qi", "Sx", "Sp", "Oc", "No", "De", "UDe", "DDe", "TDe", "QaDe",
#                      "QiDe", *["USE SCIENTIFIC NOTATION" for i in range(100)])
#     return coeff + abbreviations[u1]


def int_to_scietific_notation(n):
    _, whole_int = math.modf(n)
    whole_str: str = str(round(whole_int))

    zeros: int = len(whole_str) - 1
    u1: int = zeros // 3

    if u1 == 0 or u1 == 1:
        if n % 1 == 0:
            coeff: str = str(round(n))
        else:
            coeff: str = str(round(n, 2))
        note: str = ""
    else:
        coeff: str = str(int(str(whole_int)[:3]) / 100)
        note: str = 'e' + (f"0{zeros}" if zeros < 10 else str(zeros))

    return coeff + note
