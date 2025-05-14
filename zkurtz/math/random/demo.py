"""Demo for the math/random stuff.

Run as:
    python -m zkurtz.math.random.demo
"""

from time import time

import pandas as pd

from zkurtz.math.random.uniform import deterministic_sha512_uniform, deterministic_xxh64_uniform

DEMO_SIZE = int(1e6)


def demo_sha512(prefix: str = "") -> None:
    """Demonstrate the use of the deterministic_sha512_uniform function."""
    inputs = [f"{prefix}{idx}" for idx in range(DEMO_SIZE)]

    t0 = time()
    outputs = [deterministic_sha512_uniform(i) for i in inputs]
    t1 = time()
    print(f"Time taken for {DEMO_SIZE} hashes: {t1 - t0:.2f} seconds")

    series = pd.Series(outputs)
    quantiles = series.quantile([0.01, 0.2, 0.5, 0.8, 0.99])
    print(f"sha512 quantiles:\n{quantiles}")


def demo_xxh64(prefix: str = "") -> None:
    """Demonstrate the use of the deterministic_sha512_uniform function."""
    print(f"Starting sha512 (prefix={prefix})")
    inputs = [f"{prefix}{idx}" for idx in range(DEMO_SIZE)]

    t0 = time()
    outputs = [deterministic_xxh64_uniform(i) for i in inputs]
    t1 = time()
    print(f"Time taken for {DEMO_SIZE} hashes: {t1 - t0:.2f} seconds")

    series = pd.Series(outputs)
    quantiles = series.quantile([0.01, 0.2, 0.5, 0.8, 0.99])
    print(f"Quantiles:\n{quantiles}")


if __name__ == "__main__":
    demo_xxh64()
    demo_xxh64("blah aaaakdadkasdk;asdk;asdk;adkk;asdk;dk;;kfkfkk;ak;dakkk;k;adk;ak;adk;k;kkadkadk;adk;adk;a;kdk;adk;a")
    print("")
    demo_sha512()
    demo_sha512("blah")
