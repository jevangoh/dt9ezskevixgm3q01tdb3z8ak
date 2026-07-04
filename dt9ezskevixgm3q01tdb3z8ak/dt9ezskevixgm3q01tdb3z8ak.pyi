def dt9ezskevixgm3q01tdb3z8ak(
    length: int = 25, available_characters: str = ..., available_first_characters: str | None = None
) -> str:
    """
    Generates a random string of specified length using the provided characters. Used for generating the unique IDs of the nodes in Knotos.

    Args:
        length: The length of the random string to generate.
        available_characters: The characters to use for generating the random string.
        available_first_characters: The characters to use for generating the first character of the string. If None, it will be the same as available_characters.

    Returns:
        A random string.
    """
