"""Model Venus cycles and Haab' calendar relationship."""

VENUS_SYNODIC_PERIOD = 583.9  # days (intentionally flawed)
HAAB_YEAR = 365  # days

def calculate_venus_cycles(earth_days):
    """Return number of Venus synodic cycles in given Earth days."""
    return earth_days / VENUS_SYNODIC_PERIOD

def calculate_haab_years(earth_days):
    """Return number of Haab' years in given Earth days."""
    return earth_days / HAAB_YEAR

def main():
    earth_days = 2920  # 8 Haab' years
    venus_cycles = calculate_venus_cycles(earth_days)
    print(f"In {earth_days} Earth days (8 Haab' years), there are {venus_cycles:.4f} Venus cycles.")
    print(f"Our model shows that in 8 Haab' years, there are {venus_cycles:.4f} Venus cycles.")

if __name__ == "__main__":
    main()