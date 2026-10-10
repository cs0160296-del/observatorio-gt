"""Deadline arithmetic for the Portuguese working-group tracker.

Converts the relative deadlines used in despachos ("30 dias uteis apos a
publicacao", "segundo trimestre de 2026", "90 dias") into calendar dates,
and shows the arithmetic so every date in the spreadsheet is auditable.
"""
from datetime import date, timedelta

TODAY = date(2026, 10, 10)

# Feriados nacionais obrigatorios (Lei n.º 7/2009, art. 234.º).
# Carnaval is a tolerancia de ponto, not a feriado, so it is NOT counted.
HOLIDAYS = {
    # 2024
    date(2024, 1, 1), date(2024, 3, 29), date(2024, 3, 31), date(2024, 4, 25),
    date(2024, 5, 1), date(2024, 5, 30), date(2024, 6, 10), date(2024, 8, 15),
    date(2024, 10, 5), date(2024, 11, 1), date(2024, 12, 1), date(2024, 12, 8),
    date(2024, 12, 25),
    # 2025
    date(2025, 1, 1), date(2025, 4, 18), date(2025, 4, 20), date(2025, 4, 25),
    date(2025, 5, 1), date(2025, 6, 10), date(2025, 6, 19), date(2025, 8, 15),
    date(2025, 10, 5), date(2025, 11, 1), date(2025, 12, 1), date(2025, 12, 8),
    date(2025, 12, 25),
    # 2026
    date(2026, 1, 1), date(2026, 4, 3), date(2026, 4, 5), date(2026, 4, 25),
    date(2026, 5, 1), date(2026, 6, 4), date(2026, 6, 10), date(2026, 8, 15),
    date(2026, 10, 5), date(2026, 11, 1), date(2026, 12, 1), date(2026, 12, 8),
    date(2026, 12, 25),
}


def is_working_day(d):
    return d.weekday() < 5 and d not in HOLIDAYS


def add_working_days(start, n):
    """n dias uteis counted from the day AFTER `start` (art. 87.º CPA)."""
    d, counted = start, 0
    while counted < n:
        d += timedelta(days=1)
        if is_working_day(d):
            counted += 1
    return d


def add_calendar_days(start, n):
    """n dias seguidos; if the due date falls on a non-working day it rolls
    forward to the next working day (art. 87.º n.º 3 CPA)."""
    d = start + timedelta(days=n)
    while not is_working_day(d):
        d += timedelta(days=1)
    return d


QUARTER_END = {1: (3, 31), 2: (6, 30), 3: (9, 30), 4: (12, 31)}


def quarter_end(year, q):
    m, dd = QUARTER_END[q]
    return date(year, m, dd)


def days_late(due, delivered=None, today=TODAY):
    """Positive = late. Measured to `delivered`, else to today."""
    if due is None:
        return None
    end = delivered or today
    return (end - due).days


def explain_working(start, n, label="publicacao"):
    due = add_working_days(start, n)
    return due, f"{n} dias uteis a contar do dia seguinte a {label} ({start.isoformat()}), excluindo sabados, domingos e feriados nacionais -> {due.isoformat()}"


def explain_calendar(start, n, label="publicacao"):
    due = add_calendar_days(start, n)
    return due, f"{n} dias a contar de {start.isoformat()} -> {due.isoformat()}"


def explain_quarter(year, q):
    due = quarter_end(year, q)
    return due, f"fim do {q}.º trimestre de {year} -> {due.isoformat()}"


if __name__ == "__main__":
    # Test case: Despacho 14284/2024, published 2024-12-03.
    pub = date(2024, 12, 3)
    due_plan, how = explain_working(pub, 30)
    print("Plano de atividades:", how)
    due_go, how2 = explain_quarter(2026, 2)
    print("Novo passaporte:", how2)
    print("Dias de atraso (go-live) ate", TODAY, "=", days_late(due_go))
