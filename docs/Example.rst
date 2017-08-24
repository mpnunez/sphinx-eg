Examples
=========

We look at an example usage.

This script makes a dog and has it bark and wag its tail.

.. literalinclude:: ../main.py
   :language: python
    
This produces::

	Woof!
	wag tail
    wag tail
    wag tail

Now let us write this as command lines.

>>> from objects import Dog
>>> Spot = Dog()
>>> Spot.bark()
>>> Spot.wag_tail(3)