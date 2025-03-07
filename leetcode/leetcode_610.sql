-- Report for every three line segments whether they can form a triangle.

select x, y, z,
if(((x + y) > z and (y + z) > x and (z + x) > y), 'Yes', 'No') triangle
from Triangle
