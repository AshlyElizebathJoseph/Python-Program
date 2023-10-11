pi=3.14
def cylinder_surface_area(r, h):
    lateral_surface_area = 2 * pi * r * h
    circular_base_area = 2 * pi * r * r
    total_surface_area = lateral_surface_area + circular_base_area
    return total_surface_area

def cylinder_volume(radius, height):
    volume = pi * r *r * h
    return volume
  
r = float(input("Enter the radius of the cylinder: "))
h = float(input("Enter the height of the cylinder: "))
surface_area = cylinder_surface_area(r, h)
volume = cylinder_volume(r, h)
print("Surface Area:", surface_area)
print("Volume:", volume)
