"""Visual test of the simulation."""

import sys
import os

# Add the parent directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.entity import Entity
from src.simulation.world import World


def main():
    """Run a visual simulation test."""
    # Create a world
    world = World(width=800, height=600)
    
    # Create some entities with different behaviors
    # Entity 1: Circular motion
    entity1 = Entity(position=(400, 300))
    entity1.set_velocity(100, 0)
    entity1.set_acceleration(0, 100)
    
    # Entity 2: Diagonal movement
    entity2 = Entity(position=(200, 200))
    entity2.set_velocity(50, 50)
    
    # Entity 3: Random walker (using friction to slow down)
    entity3 = Entity(position=(600, 400))
    entity3.set_velocity(80, -60)
    
    # Entity 4: Spiraling inward
    entity4 = Entity(position=(100, 500))
    entity4.set_velocity(120, 0)
    entity4.set_acceleration(-5, 100)
    
    # Entity 5: Stationary
    entity5 = Entity(position=(400, 100))
    
    # Entity 6: Wandering
    entity6 = Entity(position=(300, 400))
    entity6.set_velocity(20, 30)
    
    # Entity 7: Fast mover
    entity7 = Entity(position=(700, 100))
    entity7.set_velocity(-150, 100)
    
    # Add entities to the world
    entities = [entity1, entity2, entity3, entity4, entity5, entity6, entity7]
    for entity in entities:
        world.add_entity(entity)
    
    # Set some environment properties
    world.set_environment_property("friction", 0.01)  # Slightly lower friction for more dynamic movement
    
    # Run the visual simulation
    print("Starting visual simulation...")
    print("Close the window to exit.")
    world.run_visual(dt=0.016)  # ~60 FPS


if __name__ == "__main__":
    main()