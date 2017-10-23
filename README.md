# Project 4:  Brevet time calculator with Ajax
Author: Mikaela Schaefer

Contact: kaelas@uoregon.edu

## Description
This application includes a small Python/Flask server that calculates opening and closing times for brevets of distances
200km, 300km, 400km, 600km, and 1000km based on the RUSA rules for brevets. The client side of the application utilizes JavaScript
and JQuery to update opening and closing times whenever a change is detected in one of a control point's distance fields.

### ACP controle times Algorithm
The rules that the acp_times algorithms follow are those set forth by RUSA. A brief overview of those rules follows:
* Distance Rules
    * Brevets must have a total and final control distance of 200km, 300km, 400km, 600km, or 1000km
        * There is a "fudge factor" which allows for the final control to be between total distance and total distance + 10% to allow for
        control points to be placed in locations that make sense (e.g. in a town instead of on a highway).

        Thus, a 200km brevet may have its final control between 200km and 210km, a 300km between 300km and 330km, and so on.

    * The initial control must be at the start (0 km)


* Time Rules
    * General Rules
        * Minimum and maximum speeds for each distance interval can be found at: https://rusa.org/octime_alg.html
        * The given max and min speeds refer to how fast and slow a rider can reasonably be expected to bike the corresponding distance. **However, the control distance does not determine the max and min speeds for the entire distance, but only for the portion that falls within that interval.**  For example, if a control is placed at 650KM, the maximum speed is *not* 28 km/hr for the *entire* 650km, but rather for any amount of kilometers over 600km. Continuing with this example, the maximum speeds to be used to calculate the open time of the control would be 28 km/hr for the last 50km, 30 km/hr for 600km - 400km, 32 km/hr for 400km - 200km, and 34 for the first 200km.
        Intuitively, this makes sense because a person will bike the first 200km of any brevet at more or less the same pace, regardless of how much further they have to go. Similarly, that person will bike the second 200km of any brevet at more or less the same pace, since they have already biked the first 200km at their first pace and are now a little tired, and so on. 


    * For Initial and Final Controls
        * Initial control must open at the beginning time of the entire brevet and close exactly 1HR after it opens

        * Final control open times should be calculated as if the final control distance = total brevet distance. For example, if the final control is located at 1100km and the total brevet distance is 1000km, the opening time of the final control will be calculated using 1000km as the distance instead of 1100km. This applies to brevets of any distance.

        * Final control close times are pre-determined by the rules. This includes final controls that fall under the final distance + 10% rule. For example, if a final control distance is 1100KM and the brevet distance is 1000km, the closing times will be as if the final control distance was 1000KM. This applies to brevets of any distance.
        
        The close times for final controls are as follows. Times given are relative to the start time of the brevet.
            ```
            200KM : 13H30 (meaning 13HR 30MIN)
            300KM : 20H00
            400KM : 27H00
            600KM : 40H00
            1000KM : 75H00
            ```


### Functionality to be Implemented
At the moment, the application does not update already calculated control open and close times if the user changes the start date, start time, or total brevet distance. Furthermore, the application does not update the initial control open and close times if the user changes the start date or start time, but this does not affect the correctness of the other control open and close times. These aspects of functionality should be implemented for a more robust application.

