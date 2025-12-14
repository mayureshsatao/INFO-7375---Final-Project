"""
Diagram Generator Module
Creates educational diagrams and visualizations for different topics
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from io import BytesIO
import base64


class DiagramGenerator:
    """Generate educational diagrams based on topics"""

    def __init__(self):
        self.diagram_types = {
            'pythagorean theorem': self._pythagorean_diagram,
            'quadratic equations': self._quadratic_diagram,
            'photosynthesis': self._photosynthesis_diagram,
            'cell structure': self._cell_diagram,
            'newton\'s laws': self._newton_laws_diagram,
            'data structures': self._data_structures_diagram,
            'world war ii': self._wwii_timeline,
        }

    def generate_diagram(self, topic: str, style: str = 'educational'):
        """Generate a diagram for the given topic"""
        topic_lower = topic.lower()

        # Find matching diagram generator
        for key, generator in self.diagram_types.items():
            if key in topic_lower or topic_lower in key:
                return generator()

        # Default: concept map
        return self._generic_concept_map(topic)

    def _pythagorean_diagram(self):
        """Generate Pythagorean theorem diagram"""
        fig, ax = plt.subplots(figsize=(10, 8))

        # Draw right triangle
        triangle = plt.Polygon([(1, 1), (1, 5), (5, 1)],
                               fill=False, edgecolor='blue', linewidth=2)
        ax.add_patch(triangle)

        # Draw squares on each side
        # Square on side a (height)
        square_a = patches.Rectangle((0.2, 1), 0.8, 4,
                                     fill=True, facecolor='lightblue',
                                     edgecolor='blue', linewidth=1.5, alpha=0.5)
        ax.add_patch(square_a)

        # Square on side b (base)
        square_b = patches.Rectangle((1, 0.2), 4, 0.8,
                                     fill=True, facecolor='lightgreen',
                                     edgecolor='green', linewidth=1.5, alpha=0.5)
        ax.add_patch(square_b)

        # Square on hypotenuse
        angle = np.arctan(4 / 4)
        # Simplified square on hypotenuse
        hyp_length = np.sqrt(16 + 16)

        # Labels
        ax.text(0.6, 3, 'a = 4', fontsize=14, fontweight='bold')
        ax.text(3, 0.5, 'b = 4', fontsize=14, fontweight='bold')
        ax.text(3.5, 3.5, 'c = √32 ≈ 5.66', fontsize=14, fontweight='bold', rotation=45)

        # Formula
        ax.text(3, 7, r'$a^2 + b^2 = c^2$', fontsize=20,
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        ax.text(3, 6.3, r'$4^2 + 4^2 = 32$', fontsize=16)

        # Right angle indicator
        right_angle = patches.Rectangle((1, 1), 0.3, 0.3,
                                        fill=False, edgecolor='red', linewidth=2)
        ax.add_patch(right_angle)

        ax.set_xlim(-0.5, 8)
        ax.set_ylim(-0.5, 8)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title('Pythagorean Theorem Visualization', fontsize=18, fontweight='bold')

        return self._fig_to_base64(fig)

    def _quadratic_diagram(self):
        """Generate quadratic equation parabola"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        # Left: Parabola with labeled parts
        x = np.linspace(-5, 5, 100)
        y = x ** 2 - 2 * x - 3  # (x-3)(x+1)

        ax1.plot(x, y, 'b-', linewidth=2, label='y = x² - 2x - 3')
        ax1.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        ax1.axvline(x=0, color='k', linestyle='-', alpha=0.3)
        ax1.grid(True, alpha=0.3)

        # Mark vertex
        vertex_x = 1
        vertex_y = -4
        ax1.plot(vertex_x, vertex_y, 'ro', markersize=10, label=f'Vertex ({vertex_x}, {vertex_y})')

        # Mark roots
        ax1.plot(3, 0, 'go', markersize=10, label='Root: x = 3')
        ax1.plot(-1, 0, 'go', markersize=10, label='Root: x = -1')

        # Axis of symmetry
        ax1.axvline(x=vertex_x, color='r', linestyle='--', alpha=0.5, label='Axis of symmetry')

        ax1.set_xlabel('x', fontsize=12)
        ax1.set_ylabel('y', fontsize=12)
        ax1.set_title('Parabola: y = x² - 2x - 3', fontsize=14, fontweight='bold')
        ax1.legend(loc='upper right')
        ax1.set_ylim(-6, 10)

        # Right: Quadratic formula breakdown
        ax2.axis('off')

        formula_text = [
            'Quadratic Formula',
            '',
            'For equation: ax² + bx + c = 0',
            '',
            'Solution:',
            r'$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$',
            '',
            'Example: x² - 2x - 3 = 0',
            'a = 1, b = -2, c = -3',
            '',
            'Discriminant: b² - 4ac',
            '(-2)² - 4(1)(-3) = 4 + 12 = 16',
            '',
            r'$x = \frac{2 \pm \sqrt{16}}{2} = \frac{2 \pm 4}{2}$',
            '',
            'x = 3  or  x = -1',
        ]

        y_pos = 0.95
        for line in formula_text:
            if line.startswith('$'):
                ax2.text(0.1, y_pos, line, fontsize=14, family='monospace')
            elif line in ['Quadratic Formula', 'Example: x² - 2x - 3 = 0']:
                ax2.text(0.1, y_pos, line, fontsize=16, fontweight='bold')
            else:
                ax2.text(0.1, y_pos, line, fontsize=12)
            y_pos -= 0.06

        plt.tight_layout()
        return self._fig_to_base64(fig)

    def _photosynthesis_diagram(self):
        """Generate photosynthesis process diagram"""
        fig, ax = plt.subplots(figsize=(12, 8))

        # Draw leaf shape
        leaf = patches.Ellipse((5, 5), 4, 6, fill=True,
                               facecolor='lightgreen', edgecolor='darkgreen', linewidth=2)
        ax.add_patch(leaf)

        # Inputs (left side)
        ax.annotate('', xy=(3, 6), xytext=(1, 7),
                    arrowprops=dict(arrowstyle='->', lw=2, color='orange'))
        ax.text(0.5, 7.3, '☀️ Sunlight', fontsize=14, fontweight='bold')

        ax.annotate('', xy=(3, 5), xytext=(1, 5),
                    arrowprops=dict(arrowstyle='->', lw=2, color='blue'))
        ax.text(0.3, 5.3, '💧 H₂O (Water)', fontsize=12, fontweight='bold')

        ax.annotate('', xy=(3, 4), xytext=(1, 3),
                    arrowprops=dict(arrowstyle='->', lw=2, color='gray'))
        ax.text(0.3, 2.7, '🌫️ CO₂', fontsize=12, fontweight='bold')

        # Chloroplast
        chloroplast = patches.Rectangle((4, 4.5), 2, 1,
                                        fill=True, facecolor='darkgreen',
                                        edgecolor='black', linewidth=1.5)
        ax.add_patch(chloroplast)
        ax.text(5, 5, 'Chloroplast', fontsize=11, ha='center',
                color='white', fontweight='bold')

        # Outputs (right side)
        ax.annotate('', xy=(9, 6), xytext=(7, 6),
                    arrowprops=dict(arrowstyle='->', lw=2, color='red'))
        ax.text(9.2, 6.2, '🍬 C₆H₁₂O₆\n(Glucose)', fontsize=12, fontweight='bold')

        ax.annotate('', xy=(9, 4), xytext=(7, 4),
                    arrowprops=dict(arrowstyle='->', lw=2, color='lightblue'))
        ax.text(9.2, 3.8, '💨 O₂\n(Oxygen)', fontsize=12, fontweight='bold')

        # Equation at bottom
        equation = '6CO₂ + 6H₂O + Light Energy → C₆H₁₂O₆ + 6O₂'
        ax.text(5, 1.5, equation, fontsize=14, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

        ax.set_xlim(0, 11)
        ax.set_ylim(0, 10)
        ax.axis('off')
        ax.set_title('Photosynthesis Process', fontsize=18, fontweight='bold')

        return self._fig_to_base64(fig)

    def _cell_diagram(self):
        """Generate cell structure diagram"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

        # Animal Cell
        cell = patches.Circle((5, 5), 3, fill=True, facecolor='lightyellow',
                              edgecolor='black', linewidth=2)
        ax1.add_patch(cell)
        ax1.text(5, 8.5, 'Animal Cell', fontsize=16, fontweight='bold', ha='center')

        # Nucleus
        nucleus = patches.Circle((5, 5), 1, fill=True, facecolor='lightblue',
                                 edgecolor='blue', linewidth=2)
        ax1.add_patch(nucleus)
        ax1.text(5, 5, 'Nucleus', fontsize=10, ha='center', fontweight='bold')

        # Mitochondria
        for pos in [(3.5, 6.5), (6.5, 6.5)]:
            mito = patches.Ellipse(pos, 0.8, 0.4, fill=True,
                                   facecolor='red', alpha=0.6)
            ax1.add_patch(mito)
        ax1.text(3.5, 7, 'Mitochondria', fontsize=8)

        # Ribosomes (small dots)
        for _ in range(8):
            x, y = np.random.uniform(2.5, 7.5), np.random.uniform(2.5, 7.5)
            if np.sqrt((x - 5) ** 2 + (y - 5) ** 2) > 1.2:  # Outside nucleus
                ax1.plot(x, y, 'ko', markersize=3)
        ax1.text(7, 4, 'Ribosomes', fontsize=8)

        # Cell membrane
        ax1.text(5, 1.8, 'Cell Membrane', fontsize=10, ha='center',
                 bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        ax1.set_xlim(0, 10)
        ax1.set_ylim(0, 10)
        ax1.axis('off')

        # Plant Cell
        cell_wall = patches.Rectangle((1.5, 1.5), 7, 7, fill=False,
                                      edgecolor='darkgreen', linewidth=3)
        ax2.add_patch(cell_wall)

        cell_membrane = patches.Rectangle((2, 2), 6, 6, fill=True,
                                          facecolor='lightgreen', alpha=0.3,
                                          edgecolor='green', linewidth=2)
        ax2.add_patch(cell_membrane)
        ax2.text(5, 9, 'Plant Cell', fontsize=16, fontweight='bold', ha='center')

        # Nucleus
        nucleus = patches.Circle((5, 5), 1, fill=True, facecolor='lightblue',
                                 edgecolor='blue', linewidth=2)
        ax2.add_patch(nucleus)
        ax2.text(5, 5, 'Nucleus', fontsize=10, ha='center', fontweight='bold')

        # Chloroplasts
        for pos in [(3, 6.5), (7, 6.5), (3, 3.5), (7, 3.5)]:
            chloro = patches.Ellipse(pos, 0.6, 0.4, fill=True,
                                     facecolor='green', alpha=0.7)
            ax2.add_patch(chloro)
        ax2.text(3, 7, 'Chloroplasts', fontsize=8)

        # Vacuole
        vacuole = patches.Circle((6.5, 4), 1.2, fill=True,
                                 facecolor='lightcyan', alpha=0.5,
                                 edgecolor='cyan', linewidth=1.5)
        ax2.add_patch(vacuole)
        ax2.text(6.5, 4, 'Vacuole', fontsize=9, ha='center')

        # Cell wall label
        ax2.text(5, 1, 'Cell Wall', fontsize=10, ha='center',
                 bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))

        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 10)
        ax2.axis('off')

        plt.tight_layout()
        return self._fig_to_base64(fig)

    def _newton_laws_diagram(self):
        """Generate Newton's Laws diagram"""
        fig, axes = plt.subplots(3, 1, figsize=(12, 10))

        # First Law - Inertia
        ax = axes[0]
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 3)
        ax.axis('off')

        # Moving object
        box1 = patches.Rectangle((2, 1), 1, 1, fill=True, facecolor='blue')
        ax.add_patch(box1)
        ax.arrow(3.2, 1.5, 2, 0, head_width=0.2, head_length=0.3, fc='blue', ec='blue')
        ax.text(5, 1.5, 'Constant Velocity', fontsize=10)

        ax.text(5, 2.5, "First Law: Objects in motion stay in motion\n(unless acted upon by external force)",
                fontsize=12, ha='center', fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

        # Second Law - F=ma
        ax = axes[1]
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 3)
        ax.axis('off')

        # Two scenarios
        # Light object
        box2 = patches.Rectangle((1, 1.5), 0.5, 0.5, fill=True, facecolor='orange')
        ax.add_patch(box2)
        ax.arrow(1.7, 1.75, 1, 0, head_width=0.15, head_length=0.2, fc='red', ec='red', linewidth=2)
        ax.text(1.25, 1, 'm = 1 kg', fontsize=9, ha='center')
        ax.arrow(2.9, 1.75, 1.5, 0, head_width=0.15, head_length=0.2, fc='green', ec='green', linewidth=2)
        ax.text(3.6, 1.4, 'a = 2 m/s²', fontsize=9)

        # Heavy object
        box3 = patches.Rectangle((5.5, 1.5), 1, 0.5, fill=True, facecolor='gray')
        ax.add_patch(box3)
        ax.arrow(6.7, 1.75, 1, 0, head_width=0.15, head_length=0.2, fc='red', ec='red', linewidth=2)
        ax.text(6, 1, 'm = 2 kg', fontsize=9, ha='center')
        ax.arrow(7.9, 1.75, 0.75, 0, head_width=0.15, head_length=0.2, fc='green', ec='green', linewidth=2)
        ax.text(8.3, 1.4, 'a = 1 m/s²', fontsize=9)

        ax.text(5, 2.7, "Second Law: F = ma\n(Same force, different masses = different accelerations)",
                fontsize=12, ha='center', fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

        # Third Law - Action-Reaction
        ax = axes[2]
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 3)
        ax.axis('off')

        # Two objects pushing each other
        box4 = patches.Rectangle((3, 1), 1, 1, fill=True, facecolor='red')
        ax.add_patch(box4)
        box5 = patches.Rectangle((6, 1), 1, 1, fill=True, facecolor='blue')
        ax.add_patch(box5)

        # Action arrow
        ax.arrow(4.1, 1.5, 1.7, 0, head_width=0.2, head_length=0.3,
                 fc='red', ec='red', linewidth=3)
        ax.text(5, 1.1, 'Action', fontsize=10, ha='center')

        # Reaction arrow
        ax.arrow(5.9, 1.5, -1.7, 0, head_width=0.2, head_length=0.3,
                 fc='blue', ec='blue', linewidth=3)
        ax.text(5, 1.9, 'Reaction', fontsize=10, ha='center')

        ax.text(5, 2.7, "Third Law: For every action, there is an equal\nand opposite reaction",
                fontsize=12, ha='center', fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))

        plt.tight_layout()
        return self._fig_to_base64(fig)

    def _data_structures_diagram(self):
        """Generate data structures comparison"""
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))

        # Array
        ax = axes[0, 0]
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 5)
        ax.axis('off')
        ax.text(5, 4.5, 'Array', fontsize=16, fontweight='bold', ha='center')

        for i in range(5):
            rect = patches.Rectangle((i * 1.5 + 2, 2), 1, 1,
                                     fill=True, facecolor='lightblue',
                                     edgecolor='black', linewidth=2)
            ax.add_patch(rect)
            ax.text(i * 1.5 + 2.5, 2.5, str(i * 10), fontsize=12, ha='center')
            ax.text(i * 1.5 + 2.5, 1.5, f'[{i}]', fontsize=10, ha='center')

        ax.text(5, 0.5, 'O(1) access • O(n) insert/delete', fontsize=10, ha='center')

        # Linked List
        ax = axes[0, 1]
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 5)
        ax.axis('off')
        ax.text(5, 4.5, 'Linked List', fontsize=16, fontweight='bold', ha='center')

        for i in range(4):
            circle = patches.Circle((i * 2 + 2, 2.5), 0.4,
                                    fill=True, facecolor='lightgreen',
                                    edgecolor='black', linewidth=2)
            ax.add_patch(circle)
            ax.text(i * 2 + 2, 2.5, str(i * 10), fontsize=10, ha='center')

            if i < 3:
                ax.arrow(i * 2 + 2.5, 2.5, 1.3, 0,
                         head_width=0.2, head_length=0.2, fc='black', ec='black')

        ax.text(5, 0.5, 'O(n) access • O(1) insert/delete', fontsize=10, ha='center')

        # Stack
        ax = axes[1, 0]
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 5)
        ax.axis('off')
        ax.text(5, 4.5, 'Stack (LIFO)', fontsize=16, fontweight='bold', ha='center')

        for i in range(4):
            rect = patches.Rectangle((4, i * 0.7 + 0.5), 2, 0.6,
                                     fill=True, facecolor='lightyellow',
                                     edgecolor='black', linewidth=2)
            ax.add_patch(rect)
            ax.text(5, i * 0.7 + 0.8, f'Item {i + 1}', fontsize=10, ha='center')

        ax.arrow(5, 3.5, 0, 0.7, head_width=0.3, head_length=0.2,
                 fc='red', ec='red', linewidth=2)
        ax.text(6, 4, 'Push/Pop', fontsize=10)

        # Queue
        ax = axes[1, 1]
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 5)
        ax.axis('off')
        ax.text(5, 4.5, 'Queue (FIFO)', fontsize=16, fontweight='bold', ha='center')

        for i in range(4):
            rect = patches.Rectangle((i * 1.5 + 2, 2), 1, 1,
                                     fill=True, facecolor='lightcoral',
                                     edgecolor='black', linewidth=2)
            ax.add_patch(rect)
            ax.text(i * 1.5 + 2.5, 2.5, f'{i + 1}', fontsize=12, ha='center')

        ax.arrow(1.5, 2.5, -0.7, 0, head_width=0.2, head_length=0.2,
                 fc='green', ec='green', linewidth=2)
        ax.text(0.5, 2.2, 'Dequeue', fontsize=9)

        ax.arrow(8.5, 2.5, 0.7, 0, head_width=0.2, head_length=0.2,
                 fc='blue', ec='blue', linewidth=2)
        ax.text(9.3, 2.2, 'Enqueue', fontsize=9)

        plt.tight_layout()
        return self._fig_to_base64(fig)

    def _wwii_timeline(self):
        """Generate WWII timeline"""
        fig, ax = plt.subplots(figsize=(14, 8))

        events = [
            (1939, 'WWII Begins\nGermany invades Poland', 'red'),
            (1940, 'Battle of Britain\nFall of France', 'orange'),
            (1941, 'Pearl Harbor\nUSA enters war', 'blue'),
            (1942, 'Battle of Stalingrad', 'purple'),
            (1943, 'Italy surrenders', 'green'),
            (1944, 'D-Day Invasion\nNormandy', 'cyan'),
            (1945, 'Germany surrenders\nAtomic bombs\nJapan surrenders', 'red'),
        ]

        # Timeline line
        ax.plot([1939, 1945], [5, 5], 'k-', linewidth=3)

        for year, event, color in events:
            # Marker on timeline
            ax.plot(year, 5, 'o', markersize=15, color=color)

            # Event text (alternate above and below)
            y_pos = 6.5 if year % 2 == 1 else 3.5
            ax.text(year, y_pos, f'{year}\n{event}',
                    fontsize=10, ha='center',
                    bbox=dict(boxstyle='round', facecolor=color, alpha=0.3))

            # Connecting line
            ax.plot([year, year], [5, y_pos - 0.3 if y_pos > 5 else y_pos + 0.3],
                    'k--', alpha=0.3)

        ax.set_xlim(1938, 1946)
        ax.set_ylim(2, 8)
        ax.axis('off')
        ax.set_title('World War II Timeline (1939-1945)',
                     fontsize=18, fontweight='bold')

        # Legend
        ax.text(1938.5, 1.5, 'Key Events of WWII', fontsize=12, fontweight='bold')

        return self._fig_to_base64(fig)

    def _generic_concept_map(self, topic: str):
        """Generate a generic concept map"""
        fig, ax = plt.subplots(figsize=(12, 8))

        # Center concept
        center = patches.Circle((6, 5), 1, fill=True,
                                facecolor='lightblue', edgecolor='blue', linewidth=2)
        ax.add_patch(center)
        ax.text(6, 5, topic, fontsize=12, ha='center', fontweight='bold', wrap=True)

        # Connected concepts
        positions = [
            (3, 7, 'Concepts'),
            (9, 7, 'Applications'),
            (3, 3, 'Examples'),
            (9, 3, 'Key Points'),
        ]

        for x, y, label in positions:
            circle = patches.Circle((x, y), 0.7, fill=True,
                                    facecolor='lightyellow', edgecolor='orange', linewidth=2)
            ax.add_patch(circle)
            ax.text(x, y, label, fontsize=10, ha='center', fontweight='bold')

            # Connection to center
            ax.plot([x, 6], [y, 5], 'k--', alpha=0.5)

        ax.set_xlim(0, 12)
        ax.set_ylim(0, 10)
        ax.axis('off')
        ax.set_title(f'Concept Map: {topic}', fontsize=16, fontweight='bold')

        return self._fig_to_base64(fig)

    def _fig_to_base64(self, fig):
        """Convert matplotlib figure to base64 string"""
        buf = BytesIO()
        fig.savefig(buf, format='png', bbox_inches='tight', dpi=100)
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close(fig)
        return img_base64

    def get_diagram_html(self, topic: str):
        """Get HTML img tag for the diagram"""
        img_base64 = self.generate_diagram(topic)
        return f'<img src="data:image/png;base64,{img_base64}" style="max-width:100%; height:auto;"/>'