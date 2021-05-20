# Rolling Dice with Plotly
""" We’ll use the Python package Plotly to produce interactive visualizations. Plotly is particularly useful when you’re creating visualizations that will be displayed in a browser, because the visualizations will scale automatically to fit the viewer’s screen. Visualizations that Plotly generates are also interactive; when the user hovers over certain elements on the screen, information about that element is highlighted """

""" Install plotly using the command: python -m pip install --user plotly """

from random import randint

class Die:
    """A class representing a single die."""
    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides
 
    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)