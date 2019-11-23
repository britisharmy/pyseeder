R = ... Radius of earth ...
def great_circle_destination(lon1, lat1, bearing, dist):
    lat2 = math.asin( math.sin(lat1)*math.cos(dist/R) + 
          math.cos(lat1)*math.sin(dist/R)*math.cos(bearing) )
    lon2 = lon1 + math.atan2(math.sin(bearing)*math.sin(dist/R)*math.cos(lat1), 
                 math.cos(dist/R)-math.sin(lat1)*math.sin(lat2)
    return lon2, lat2
