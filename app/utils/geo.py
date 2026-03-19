import math

def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the great-circle distance between two points 
    on the Earth (specified in decimal degrees) using the Haversine formula.
    Returns distance in kilometers.
    """
    # Convert decimal degrees to radians 
    phi1, lambda1 = math.radians(lat1), math.radians(lon1)
    phi2, lambda2 = math.radians(lat2), math.radians(lon2)

    # Haversine formula
    dphi = phi2 - phi1
    dlambda = lambda2 - lambda1

    a = (math.sin(dphi / 2)**2 + 
         math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2)
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Radius of Earth in kilometers
    r = 6371.0
    return r * c