# HunterXKOM
## Overview 
This project will allow a given athlete to search a range of x miles around themselves and determine
which Strava segments they could likely get the # 1 ranked time on
### Potential implementations
Looking at three different possible implementations:
#### Implementation 1 (Athlete vs Standardized segment)
Take the athlete's PR or some data about their speed and compare it to the segment itself. In order to do this we need to find a way to standardize segments so that they may be reduced to a value easily comparable to the athlete's performance. Looking into Algorithms that create Grade Adjusted Pace (GAP) or similar standardizations may be useful
#### Implementation 2 (Athlete run data vs Segment run data)
Get a sample of GPX run data from a user (perhaps only workouts and races) and compare that data to the run data of the segment. By using a pattern matching algorithm to match a run with the segment, we can then measure how the athletes past performance compares to the segment.
### Implementations 3 (Athlete data vs Athlete data)
Get some data about the athlete attempting the segment vs the athlete with the current best time. This could be PR's, estimated PR's, or previous run data.