# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright 2015-2018 by Exopy Authors, see AUTHORS for more details.
#
# Distributed under the terms of the BSD license.
#
# The full license is in the file LICENCE, distributed with this software.
# -----------------------------------------------------------------------------
"""Specialised container used to store measures.

"""
from __future__ import (division, unicode_literals, print_function,
                        absolute_import)

from collections import Iterable

from atom.api import Atom, List, Signal

from ..utils.container_change import ContainerChange


class MeasurementContainer(Atom):
    """Generic container for measures.

    """
    #: List containing the measures. This must not be manipulated directly
    #: by user code.
    measurements = List()

    #: Signal used to notify changes to the stored measures.
    changed = Signal()

    def add(self, measurement, index=None):
        """Add a measurement to the stored ones.

        Parameters
        ----------
        measurement : Measurement
            Measurement to add.

        index : int | None
            Index at which to insert the measurement. If None the measurement
            is appended.

        """
        notification = ContainerChange(obj=self, name='measurements')
        if index is None:
            index = len(self.measurements)
            self.measurements.append(measurement)
        else:
            self.measurements.insert(index, measurement)

        notification.add_operation('added', (index, measurement))
        self.changed(notification)

    def remove(self, measures):
        """Remove a measurement or a list of measurement.

        Parameters
        ----------
        measures : Measurement|list[Measurement]
            Measurement(s) to remove.

        """
        if not isinstance(measures, Iterable):
            measures = [measures]

        notification = ContainerChange(obj=self, name='measurements')
        for measurement in measures:
            old = self.measurements.index(measurement)
            del self.measurements[old]
            notification.add_operation('removed', (old, measurement))

        self.changed(notification)

    def move(self, old, new):
        """Move a measurement.

        Parameters
        ----------
        old : int
            Index at which the measurement to move currently is.

        new_position : int
            Index at which to insert the measurement.

        """
        measurement = self.measurements[old]
        del self.measurements[old]
        self.measurements.insert(new, measurement)

        notification = ContainerChange(obj=self, name='measurements')
        notification.add_operation('moved', (old, new, measurement))
        self.changed(notification)
