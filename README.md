# HunterXKOM

## Overview

This project will compare a given athlete to a Strava Segment, with the goal of seeing whether the athlete could achieve the best known time on the segment. We use three different methods to assess if an athlete could achieve a segment. The main aglorithm for doing so is a Dynamic Time Warping algorithm. The other two alorithms are less sophisticated and provide a baseline to compare our DTW algorith against.

### Repository structure

**data_gathering** - jupyter notebooks containing scripts for gathering segment and run data  
**experiment_notebooks** - notebooks where experiments pertaining to implementation 1 & 2 are stored.  
**data** - holds different types of relevent data used by our algorithms    
**jays_notebook** - contains notebooks broadly pertaining to implementation 3   

### Implementation 1 (Athlete vs Standardized segment)

Stored in **experiment_notebooks/athlete_v_segmet.ipynb**   

Take in an athlete's 5k PR as a percentage of the world record. Use this percentage to estimate other times that athlete could run at differing distances. Use these distances and times to plot a "perfomance curve" for the athlete. Then calculate the Grade Adjusted Pace (GAP) for the segment's current best known time. Plot this GAP against the perfomance curve to determine if the athlete would get the segment.

### Implementation 2 (Athlete run data vs Segment run data)

Stored in **experiment_notebooks/segment_v_segment.ipynb**  

Get a sample of GPX run data from a user and compare that data to the run data of the segment. By using a pattern matching algorithm to match a run with the segment, we can then measure how the athletes past performance compares to the segment. Pattern matching algorithms, such as dynamic time warping (DTW), an algorithm commonly used in market analysis and waveform analysis, will be able to compare past runs elevation/distance profile to the segment. Once a segment has been matched to a run, we can see if an athlete would run a faster time than the current segment record.

#### DTW Algorithm: (copied from Wikipedia)
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

Get some data about the athlete attempting the segment vs the athlete with the current best time. This could be PR's, estimated PR's, or previous run data. Use this data to compare the two athletes.


## Results
We tested our results by looking at a small sample of runs that James Settles has the KOM on. We then tested our implementations on these segments, using James Settles' running data to compare. The results we found were that on average our implementations successfully predicted that James would get the segments he already has. Our main algorithm, DTW, correctly predicted all of the runs that it was able to create an accurate match for. However, runs like the Blue Ridge Segment that didn't find any good runs for comparison, were predicted incorrectly. These results are still promising as they show that the more data we have, the more accurate the DTW algorithm will become.