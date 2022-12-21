# HunterXKOM

## Overview

This project will allow a given athlete to search a range of x miles around themselves and determine
which Strava segments they could likely get the # 1 ranked time on

### Potential implementations

Looking at three different possible implementations:

#### Implementation 1 (Athlete vs Standardized segment)

Take the athlete's PR or some data about their speed and compare it to the segment itself. In order to do this we need to find a way to standardize segments so that they may be reduced to a value easily comparable to the athlete's performance. Looking into Algorithms that create Grade Adjusted Pace (GAP) or similar standardizations may be useful

#### Implementation 2 (Athlete run data vs Segment run data)

Get a sample of GPX run data from a user (perhaps only workouts and races) and compare that data to the run data of the segment. By using a pattern matching algorithm to match a run with the segment, we can then measure how the athletes past performance compares to the segment. Pattern matching algorithms, such as dynamic time warping (DTW), an algorithm commonly used in market analysis and waveform analysis, will be able to compare past runs elevation/distance profile to the segment, and then we will compare times to see how far off atheletes are. 

##### DTW Algorithm: (copied from Wikipedia)
* Every index from the first set of GPS data must be matched with one or more indices from the other set
* The first index from the first set must be matched with the first index from the other sequence (but doesn't have to be its only match)
* The last indexes must also be matched
* The mapping of the indices from the first sequence to indices from the
  other sequence must be monotonically increasing, and vice versa, i.e. if
  `j > i` are indices from the first sequence, then there must not be two indices `l > k` in the other sequence, such that index `i` is matched with index `l` and index `j` is matched with index `k` , and vice versa
* The optimal match is denoted by the match that satisfies all the restrictions and the rules and that has the minimal cost, where the cost is computed as the sum of absolute differences, for each matched pair of indices, between their values.
##### How to use:
1. Use the data_gathering/strava_api_scraping.ipynb to get the detailed segment data for desired segments and save as a JSON file. 
2. Use experiment_notebooks/detailed_segment_data_maps.ipynb to generate JSON files of lists of coorindates
3. Use experiment_notebooks/coordinates_to_elevation.ipynb to convert those to have elevation data using the USGS API
4. Add a representative amount of .GPX files from desired users to a folder, I used data/Mix_data
5. In experiment_notebooks/segment_v_segment.ipynb run the method compare_user_activities_to_segment(segmentPath, segmentID) with the path of the segment and the segment ID as strings. This will tell you wheter you could or couldn't get the segment.
### Implementations 3 (Athlete data vs Athlete data)

Get some data about the athlete attempting the segment vs the athlete with the current best time. This could be PR's, estimated PR's, or previous run data.
