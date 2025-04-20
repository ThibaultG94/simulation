"""Environment module for the simulation."""

from typing import Tuple, Dict, Any

class Environment:
    """Base environment that defines physical rules and constraints."""

    def __init__(self, width: float = 800, height: float = 600) -> None:
        """Initialize the environment with dimensions and properties."""
        self.width = width
        self.height = height
        
        # Physical properties
        self.friction: float = 0.1 # Friction coefficient
        self.gravity: Tuple[float, float] = (0.0, 0.0) # Gravity vector

        # Environment properties
        self.properties: Dict[str, Any] = {}

    def apply_constraints(self, position: Tuple[float, float]) -> Tuple[float, float]:
        """Apply environmental constraints to a position."""
        x, y = position

        # Boundary constraints (wrapping)
        x = x % self.width
        y = y % self.height

        return (x, y)
    
    def apply_forces(self, velocity: Tuple[float, float]) -> Tuple[float, float]:
        """Apply environmental forces like friction."""
        vx, vy = velocity

        # Apply friction (simple linar model)
        vx -= self.friction * vx
        vy -= self.friction * vy

        return (vx, vy)
    
    def set_property(self, key: str, value: Any) -> None:
        """Set an environment property."""
        self.properties[key] = value

    def get_property(self, key: str, default: Any = None) -> Any:
        """Get an environment property."""
        return self.properties.get(key, default)