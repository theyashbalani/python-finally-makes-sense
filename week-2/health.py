def cpu_ok(cpu):
    if cpu < 80:
        return "OK"
    else:
        return "Overload"