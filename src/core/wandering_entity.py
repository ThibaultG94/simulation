"""Wandering entity with avoidance behavior."""

import random
import math
from typing import Tuple, List, Optional
from .entity import Entity


class WanderingEntity(Entity):
    """Entity that wanders randomly while avoiding others."""
    
    def __init__(self, position: Tuple[float, float] = None, speed: float = 50.0):
        """Initialize a wandering entity."""
        super().__init__(position)
        self.max_speed = speed
        self.wander_strength = 20.0  # How much the entity changes direction
        self.avoidance_radius = 30.0  # Distance to avoid other entities
        self.avoidance_strength = 200.0  # Force applied when avoiding
        
    def wander(self) -> None:
        """Add random wandering behavior."""
        # Random angle change
        angle = random.uniform(-math.pi, math.pi) * self.wander_strength * 0.016
        
        # Current velocity magnitude
        speed = math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)
        
        # If barely moving, give it a random direction
        if speed < 0.1:
            angle_rad = random.uniform(0, 2 * math.pi)
            self.set_velocity(
                math.cos(angle_rad) * self.max_speed,
                math.sin(angle_rad) * self.max_speed
            )
        else:
            # Add some randomness to current direction
            current_angle = math.atan2(self.velocity[1], self.velocity[0])
            new_angle = current_angle + angle
            
            # Apply new velocity
            self.set_velocity(
                math.cos(new_angle) * self.max_speed,
                math.sin(new_angle) * self.max_speed
            )
    
    def avoid_others(self, other_entities: List[Entity]) -> None:
        """Avoid colliding with other entities."""
        avoidance_force = [0.0, 0.0]
        
        for other in other_entities:
            if other is not self:
                # Calculate distance
                dx = self.position[0] - other.position[0]
                dy = self.position[1] - other.position[1]
                distance = math.sqrt(dx**2 + dy**2)
                
                # If within avoidance radius, apply force
                if distance < self.avoidance_radius and distance > 0:
                    # Normalize direction
                    nx = dx / distance
                    ny = dy / distance
                    
                    # Apply inverse square law for force
                    force = self.avoidance_strength / (distance**2)
                    
                    avoidance_force[0] += nx * force
                    avoidance_force[1] += ny * force
        
        # Apply the avoidance force as acceleration
        self.set_acceleration(avoidance_force[0], avoidance_force[1])