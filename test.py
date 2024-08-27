"""
Tests for quantities
"""

from typing import TYPE_CHECKING

from kodo.quantities import QuantityUnit


class Time(QuantityUnit):

	MS = 10
	S = 1000 * MS


def test_add() -> None:
	assert (1500 @ Time.MS) + (500 @ Time.MS) == (2000 @ Time.MS)
	assert (1500 @ Time.MS) - (500 @ Time.MS) == (1000 @ Time.MS)


def test_multiplication() -> None:
	assert (1800 @ Time.MS) * 2 == (3600 @ Time.MS)
	assert (3600 @ Time.MS) * 0.5 == (1800 @ Time.MS)

	assert (3600 @ Time.MS) / 2 == (1800 @ Time.MS)
	assert (1800 @ Time.MS) / 0.5 == (3600 @ Time.MS)


def test_division_by_quantity() -> None:
	assert (3600 @ Time.MS) // (1 @ Time.S) == 3
	assert isinstance((3 @ Time.S) // (1 @ Time.S), int)

	assert (3600 @ Time.MS) // Time.S == 3
	assert isinstance((3 @ Time.S) // Time.S, int)


def test_modulus() -> None:
	assert (3600 @ Time.MS) % (2 @ Time.S) == 1600 @ Time.MS
	assert (3600 @ Time.MS) % Time.S == 600 @ Time.MS


def test_order() -> None:
	assert (1 @ Time.S) > (999 @ Time.MS)
	assert (1 @ Time.S) >= (999 @ Time.MS)
	assert (1 @ Time.S) >= (1 @ Time.S)

	assert (999 @ Time.MS) < (1 @ Time.S)
	assert (999 @ Time.MS) <= (1 @ Time.S)
	assert (1 @ Time.S) <= (1 @ Time.S)

	assert (1 @ Time.S) != (2 @ Time.S)


if TYPE_CHECKING:
	def type_checks() -> None:
		# Checks for type checker false negatives
		#
		# All the following should result in an error when checked with mypy or pyright; the
		# errors are suppressed but if they are not raised the suppression itself will cause
		# mypy to raise an error in strict mode.

		_ = (1 @ Time.S) + 3  # type: ignore[operator]
		_ = (1 @ Time.S) - 3.0  # type: ignore[operator]

		_ = (1 @ Time.S) * (1 @ Time.S)  # type: ignore[operator]
		_ = (1 @ Time.S) / (1 @ Time.S)  # type: ignore[operator]

		_ = (1 @ Time.S) // 2  # type: ignore[operator]
		_ = (1 @ Time.S) // 2.0  # type: ignore[operator]

		_ = (1 @ Time.S) > 10  # type: ignore[operator]
		_ = (1 @ Time.S) >= 10  # type: ignore[operator]
		_ = (1 @ Time.S) < 10  # type: ignore[operator]
		_ = (1 @ Time.S) <= 10  # type: ignore[operator]
