Physical Quantities
===================

This package provides types for representing physical quantities, which have a magnitude and 
a unit.

An in-depth usage guide is available in the module's docstring.


Quick Start
-----------

Create units by creating an enum class subclassing `QuantityUnit`.  The value of each item 
is scaled to its siblings, with an appropriate value chosen as the smallest representable 
quantity which forms the base precision when scaling quantities.  For example, units of 
distance where the smallest possible quantity is 0.1mm:

```python
from kodo.quantities import QuantityUnit


class Distance(QuantityUnit):

    MILLIMETERS = 10
    CENTIMETERS = 10 * MILLIMETERS
    METERS = 100 * CENTIMETERS
    KILOMETERS = 1000 * METERS

    SIXTEENTH_INCH = 15  # 1/16" == 1.5mm
    QUARTER_INCH = 4 * SIXTEENTH_INCH
    HALF_INCH = 8 * SIXTEENTH_INCH
    INCH = 16 * SIXTEENTH_INCH
    FOOT = 12 * INCH


class Time(QuantityUnit):

    MILLISECONDS = 1
    SECONDS = 1000 * MILLISECONDS
    MINUTES = 60 * SECONDS
```

Quantities are then created with the '@' operator, using a numeric value and the desired 
unit, for example 3m:

```python
from kodo.quantities import Quantity

distance: Quantity[Distance] = 3 @ Distance.METERS
```

Quantities can be compared with, added to, and subtracted from other quantities of the same 
type.  Note that while use of different types of quantities together will not be caught at 
run time, a type checker will report it as an error.  The following examples use quantities 
of the `Distance` type, so all work:

```python
assert (3 @ Distance.METERS) == (300 @ Distance.CENTIMETERS) == (3000 @ Distance.MILLIMETERS)
assert (3 @ Distance.METERS) + (2.5 @ Distance.METERS) == (5.5 @ Distance.METERS)
```

Scaling with multiplication and division must be with unitless values:

```python
assert (3 @ Distance.METERS) * 2.0 == (6 @ Distance.METERS)
assert (3 @ Distance.METERS) / 2 == (1.5 @ Distance.METERS)
```

Division with the floor division operator '//' and finding the remainder with the modulus 
operator '%' work a little differently; the second argument must be another quantity:

```python
# 10m divides into 3m three times…
assert (10 @ Distance.METERS) // (3 @ Distance.METERS) == 3

# … with 1m left over
assert (10 @ Distance.METERS) % (3 @ Distance.METERS) == (1 @ Distance.METERS)
```

Finally, for most uses the quantity will eventually have to be converted back to a unitless 
value of a known fixed unit, for example to pass to an external API, or store in a database.  
This is done with the right shift operator '>>':

```python
import time

def get_delay() -> Quantity[Time]:
    return 10000 @ Time.MILLISECONDS

# time.sleep() takes a single float argument for the sleep time in seconds
time.sleep( get_delay() >> Time.SECONDS )
```

If for some reason an integer value is needed instead, the floor division operator can be 
used as described above with a value of 1 of the desired unit.  As a convenience the unit 
item itself can be used, matching the '>>' operator:

```python
assert (3.6 @ Time.SECONDS) // (1 @ Time.SECONDS) is 3
assert (3.6 @ Time.SECONDS) // Time.SECONDS is 3
```
