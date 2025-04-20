"""Basic entity module for the simulation."""

import random
from typing import Tuple

class Entity:
    """Basic entity that can move in 2D space."""

    def __init__(self, position: Tuple[float, float] = None):
        """Initialize the entity with a random position."""
        if position is None:
            position = (random.uniform(0, 100), random.uniform(0, 100))
        self.position = position
        self.velocity = (0.0, 0.0)
        self.acceleration = (0.0, 0.0)

    def update(self, dt: float) -> None:
        """Update entity state based on time step."""
        # Update velocity based on acceleration
        self.velocity = (
            self.velocity[0] + self.acceleration[0] * dt,
            self.velocity[1] + self.acceleration[1] * dt,
        )

        # Update position based on velocity
        self.position = (
            self.position[0] + self.velocity[0] * dt,
            self.position[1] + self.velocity[1] * dt,
        )

    def set_velocity(self, vx: float, vy: float) -> None:
        """Set the entity's velocity."""
        self.velocity = (vx, vy)

    def set_acceleration(self, ax: float, ay: float) -> None:
        """Set the entity's acceleration."""
        self.acceleration = (ax, ay)