"""World module for the simulation."""

from typing import List, Tuple
from ..core.entity import Entity
from ..core.wandering_entity import WanderingEntity
from ..core.environment import Environment
from ..visualization.display import Display


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
        # First, let wandering entities apply their behaviors
        for entity in self.entities:
            if isinstance(entity, WanderingEntity):
                # Apply wandering behavior
                entity.wander()
                
                # Apply avoidance behavior
                entity.avoid_others(self.entities)
            
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
    
    def run_visual(self, dt: float = 0.016, max_frames: int = None) -> None:
        """Run the simulation with visual display."""
        display = Display(
            width=int(self.environment.width), 
            height=int(self.environment.height)
        )
        
        frame_count = 0
        
        try:
            while display.is_running:
                # Update simulation
                self.update(dt)
                
                # Get positions for drawing
                positions = self.get_state()
                
                # Draw frame
                if not display.draw(positions, frame_count):
                    break
                
                frame_count += 1
                
                # Check if we've reached max frames
                if max_frames is not None and frame_count >= max_frames:
                    break
                    
        finally:
            display.quit()