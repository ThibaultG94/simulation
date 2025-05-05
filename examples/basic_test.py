"""Basic test of the simulation without visualization."""

import sys
import os

# Add the parent directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.entity import Entity
from src.simulation.world import World


def main():
    """Run a basic simulation test."""
    # Create a world
    world = World(width=100, height=100)
    
    # Create some entities with different initial velocities
    entity1 = Entity(position=(20, 20))
    entity1.set_velocity(5, 0)  # Moving right
    
    entity2 = Entity(position=(80, 80))
    entity2.set_velocity(-5, -5)  # Moving left and up
    
    entity3 = Entity(position=(50, 50))
    entity3.set_velocity(0, 10)  # Moving down
    
    # Add entities to the world
    world.add_entity(entity1)
    world.add_entity(entity2)
    world.add_entity(entity3)
    
    # Run simulation for 10 steps
    dt = 0.1  # Time step
    for step in range(10):
        print(f"\nStep {step + 1}:")
        
        # Update the world
        world.update(dt)
        
        # Print entity positions
        for i, position in enumerate(world.get_state()):
            print(f"  Entity {i + 1}: position={position}")


if __name__ == "__main__":
    main()