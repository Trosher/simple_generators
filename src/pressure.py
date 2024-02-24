from random import randint
from time import sleep
import logging

def emit_gel(step):
    while True:
        negativStep = -1 if step < 0 else 1
        pressure = randint(50, 100) + randint(0, abs(step)) * negativStep
        if 90 < pressure or pressure < 10:
            if (pressure > 100):
                logging.error("Pressure level error." + "\n" + \
                              "Pressure level above possible permissible values > 100.")
            return
        yield pressure
        sleep(0.2)

def valve(step):
    invers = 1
    gen_emit = emit_gel(step)
    while True:
        try:
          next(gen_emit)
          pressure = gen_emit.send(step * invers)
          print(pressure)
          invers *= -1 if 80 < pressure or pressure < 20 else 1
        except StopIteration:
            break

if __name__ == "__main__":
    valve(-20)