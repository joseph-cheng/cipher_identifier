def split_by_period(ct, period):
    return "".join([ct[index] for index in range(0, len(ct), period)])
