"""Tools related to uniform distributions.

Some code is copied from https://stackoverflow.com/a/44556106/2232265
"""

import hashlib

from xxhash import xxh64

Hash512 = hashlib.sha512
MAX_HASH_PLUS_ONE_512: int = 2 ** (Hash512().digest_size * 8)
MAX_HASH_PLUS_ONE_64: int = 2**64


def deterministic_sha512_uniform(value: str) -> float:
    """Hash an input string and map the output into [0,1].

    Using this function instead of a random number generator allows for reproducible results, including across different
    platforms and python versions.
    """
    seed = value.encode()
    hash_digest = Hash512(seed).digest()
    hash_int: int = int.from_bytes(hash_digest, "big")  # Uses explicit byteorder for system-agnostic reproducibility
    return hash_int / MAX_HASH_PLUS_ONE_512


def deterministic_xxh64_uniform(value: str) -> float:
    """Hash an input string and map the output into [0,1].

    Using this function instead of a random number generator allows for reproducible results, including across different
    platforms and python versions. We use a non-cryptographic hash function for speed.
    """
    return xxh64(value).intdigest() / MAX_HASH_PLUS_ONE_64
