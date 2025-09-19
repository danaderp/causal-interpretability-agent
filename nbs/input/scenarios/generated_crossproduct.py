from typing import List

def cross_product(vec1: List[float], vec2: List[float]) -> List[float]:
    """
    Compute the cross product of two 3D vectors.

    Args:
        vec1 (List[float]): First vector of length 3.
        vec2 (List[float]): Second vector of length 3.

    Returns:
        List[float]: The cross product vector.

    Raises:
        ValueError: If either vector is not of length 3.
    """
    if len(vec1) != 3 or len(vec2) != 3:
        raise ValueError("Both vectors must have exactly 3 elements.")

    return [
        vec1[1] * vec2[2] - vec1[2] * vec2[1],
        vec1[2] * vec2[0] - vec1[0] * vec2[2],
        vec1[0] * vec2[1] - vec1[1] * vec2[0]
    ]