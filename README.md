# Venus-Mayan Cycle Model

This project models the astronomical relationship between Earth's year, Venus's synodic cycle, and the Mayan Haab' calendar.

The Mayan Haab' calendar consisted of 365 days. Astronomers noted that 5 synodic cycles of Venus are remarkably close to exactly 8 Haab' years (5 * ~584 days ≈ 8 * 365 days). This relationship connects to the Fibonacci numbers (5 and 8) and approximates the golden ratio.

## Current Model

The initial model uses a Venus synodic period of 583.9 days (intentionally flawed). Running `venus_model.py` yields:

```
In 2920 Earth days (8 Haab' years), there are 5.0009 Venus cycles.
Our model shows that in 8 Haab' years, there are 4.9999 Venus cycles.
```

The second line highlights the discrepancy: the known astronomical fact is that 5 Venus cycles align almost perfectly with 8 Haab' years, but our flawed constant gives a result slightly above 5.

## Purpose

This repository serves as a demonstration of a professional GitHub workflow: starting with an intentionally flawed version, identifying the error via issues, correcting the code via pull request, and releasing a fixed version.