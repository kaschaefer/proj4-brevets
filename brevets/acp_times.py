"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#


MIN_SPEEDS = [(600, 11.428), (0, 15)]
MAX_SPEEDS = [(600, 28), (400, 30), (200, 32), (0, 34)]
MAX_TIME_LIMIT = {200: [13, 30], 300: [20, 00], 400: [27, 00], 600: [40, 00], 1000: [75, 00]}

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    #Check for good data before continuing
    try: 
        arrow.get(brevet_start_time)
    except:
        print("Error occured.")
        return

    distance = control_dist_km
    time = arrow.get(brevet_start_time)
    total_time = 0.0
    for km, mxspeed in MAX_SPEEDS:
        if distance > km:
            total_time = total_time + float((distance-km)/mxspeed)
            distance = km
    hrs = int(total_time)
    mins = int((total_time - hrs)*60)
    time = time.shift(hours=+hrs, minutes=+mins)
    return time.isoformat()



def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
          brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    #Test for bad input before continuing
    try: 
        arrow.get(brevet_start_time)
    except:
        print("Error occured.")
        return

    time = arrow.get(brevet_start_time)
    distance = control_dist_km

    #Requested closing time is for entire brevet, give max finish time
    if control_dist_km >= brevet_dist_km:
        hrs = MAX_TIME_LIMIT[brevet_dist_km][0]
        mins = MAX_TIME_LIMIT[brevet_dist_km][1]
        time = time.shift(hours=+hrs, minutes=+mins)

    else:
        """
        for each denomination (dist, speed) in max speed where distance < dist
        get current distance and subtract the next lowest denomination
        """
        distance = control_dist_km
        time = arrow.get(brevet_start_time)
        total_time = 0.0
        for km, min_speed in MIN_SPEEDS:
            if distance > km:
                total_time = total_time + float(distance-km)/min_speed
                distance = km
        hrs = int(total_time)
        mins = int((total_time - hrs)*60)
        time = time.shift(hours=+hrs, minutes=+mins)

    return time.isoformat()
