"""World module for the simulation."""

from typing import List, Tuple
from ..core.entity import Entity
from ..core.environment import Environment


class World:
    """The simulation world containing entities and environment."""
    
    def __init__(self, width: float = 800, height: float = 600):
        """Initialize the world with given dimensions."""
        self.environment = Environment(width, height)
        self.entities: List[Entity] = []
        
    def add_entity(self, entity: Entity) -> None:
        """Add an entity to the world."""
        self.entities.append(entity)
        
    def update(self, dt: float) -> None:
        """Update all entities in the world."""
        for entity in self.entities:
            # Apply environmental forces
            entity.velocity = self.environment.apply_forces(entity.velocity)
            
            # Update entity
            entity.update(dt)
            
            # Apply environmental constraints
            entity.position = self.environment.apply_constraints(entity.position)
    
    def get_state(self) -> List[Tuple[float, float]]:
        """Get current positions of all entities."""
        return [entity.position for entity in self.entities]
    
    def set_environment_property(self, key: str, value: any) -> None:
        """Set an environment property."""
        self.environment.set_property(key, value)
    
    def get_environment_property(self, key: str, default: any = None) -> any:
        """Get an environment property."""
        return self.environment.get_property(key, default)