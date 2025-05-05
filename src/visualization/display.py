"""Visual display module for the simulation using Pygame."""

import pygame
import sys
from typing import List, Tuple, Optional

class Display:
    """Visual display for the simulation."""

    def __init__(self, width: int = 800, height: int = 600):
        """Initialize the display."""
        # Initialize Pygame
        pygame.init()

        # Screen dimensions
        self.width = width
        self.height = height

        # Create the screen
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Individualistic Society Simulation")

        # Clock for FPS control
        self.clock = pygame.time.Clock()

        # Colors
        self.BACKGROUND = (245, 245, 245) # Light gray background
        self.ENTITY_COLORS = [
            (255, 64, 64),    # Red
            (64, 64, 255),    # Blue
            (64, 255, 64),    # Green
            (255, 255, 64),   # Yellow
            (255, 64, 255),   # Magenta
            (64, 255, 255),   # Cyan
            (255, 128, 64),   # Orange
            (128, 64, 255),   # Purple
            (64, 128, 64),    # Dark green
            (255, 160, 160),  # Pink
        ]
        self.TEXT_COLOR = (50, 50, 50)  # Dark gray

        # Font for HUD
        self.font = pygame.font.SysFont('arial', 24)
        self.small_font = pygame.font.SysFont('arial', 16)

        # Performance tracking
        self.fps_history = []

        # Running state
        self.is_running = True

    def draw(self, positions: List[Tuple[float, float]], frame_count: int) -> bool:
        """Draw the current frame."""
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
                return False
            
        # Clear screen
        self.screen.fill(self.BACKGROUND)

        # Draw entities
        for i, (x, y) in enumerate(positions):
            color = self.ENTITY_COLORS[i % len(self.ENTITY_COLORS)]
            pygame.draw.circle(self.screen, color, (int(x), int(y)), 5)

        # Draw HUD
        self._draw_hud(len(positions), frame_count)

        # Update display
        pygame.display.flip()
        
        # Control FPS
        self.clock.tick(60)
        
        return True
    
    def _draw_hud(self, entity_count: int, frame_count: int) -> None:
        """Draw the heads-up display."""
        # Get current FPS
        current_fps = self.clock.get_fps()
        self.fps_history.append(current_fps)
        if len(self.fps_history) > 60:  # Keep last 60 FPS values
            self.fps_history.pop(0)
        
        # Calculate average FPS
        avg_fps = sum(self.fps_history) / len(self.fps_history) if self.fps_history else 0
        
        # Draw HUD background
        hud_rect = pygame.Rect(10, 10, 250, 100)
        hud_surface = pygame.Surface((hud_rect.width, hud_rect.height), pygame.SRCALPHA)
        hud_surface.fill((255, 255, 255, 128))  # Semi-transparent white
        self.screen.blit(hud_surface, hud_rect)
        
        # Draw text information
        texts = [
            (f"Entities: {entity_count}", 15, 15),
            (f"Frame: {frame_count}", 15, 40),
            (f"FPS: {avg_fps:.1f}", 15, 65),
            (f"Time: {frame_count/60:.1f}s", 15, 90)
        ]
        
        for text, x, y in texts:
            surface = self.font.render(text, True, self.TEXT_COLOR)
            self.screen.blit(surface, (x, y))

    def quit(self) -> None:
        """Cleanup and quit pygame."""
        pygame.quit()
        sys.exit()