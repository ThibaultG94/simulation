"""Visual test with wandering entities that avoid each other."""

import sys
import os
import random

# Add the parent directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.wandering_entity import WanderingEntity
from src.simulation.world import World


def main():
    """Run a visual simulation test with wandering entities."""
    # Create a world
    world = World(width=800, height=600)
    
    # Create wandering entities with different speeds
    for i in range(20):
        # Random position
        x = random.uniform(50, 750)
        y = random.uniform(50, 550)
        
        # Varying speeds
        speed = random.uniform(30, 70)
        
        # Create wandering entity
        entity = WanderingEntity(position=(x, y), speed=speed)
        
        # Add to world
        world.add_entity(entity)
    
    # Set environment properties for natural movement
    world.set_environment_property("friction", 0.02)
    
    # Run the visual simulation
    print("Starting wandering entities simulation...")
    print("Watch the entities wander and avoid each other.")
    print("Close the window to exit.")
    world.run_visual(dt=0.016)  # ~60 FPS


if __name__ == "__main__":
    main()