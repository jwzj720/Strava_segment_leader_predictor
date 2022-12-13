import gpxpy
import gpxpy.gpx

class gpx_to_arr1():
    def __init__(self) -> None:
        pass
    def file_to_elevation_arr(self, fileName):
        gpx_file = open(fileName, 'r')
        gpx = gpxpy.parse(gpx_file)
        elevationOne = []
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    #print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))
                    elevationOne.append(point.elevation)
        return elevationOne