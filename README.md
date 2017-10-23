# Project 4:  Brevet time calculator with Ajax
Author: Mikaela Schaefer

Contact: kaelas@uoregon.edu

## Description
This application includes a small Python/Flask server that calculates opening and closing times for brevets of distances
200km, 300km, 400km, 600km, and 1000km based on the RUSA rules for brevets. The client side of the application utilizes JavaScript
and JQuery to update opening and closing times whenever a change is detected in either of the control point's distance fields.

### ACP controle times Algorithm
The rules that the acp_times algorithms follow are those set forth by RUSA. A brief overview of those rules follows:
* Distance Rules
    * Brevets must have a total and final control distance of 200km, 300km, 400km, 600km, or 1000km
        * There is a "fudge factor" which allows for the final control to be between total distance and total distance + 10% to allow for
        control points to be placed in locations that make sense (e.g. in a town instead of on a highway).

        Thus, a 200km brevet may have its final control between 200km and 210km, a 300km between 300km and 330km, and so on.

    * The first control must be at the start (0 km)


* Time Rules
    * For Initial and Final Controls
        * Initial control must open at the beginning time of the entire brevet and close exactly 1HR after it opens

        * Final control close times are pre-determined by the rules. This includes final controls that fall under the final distance + 10% rule. 
        For example, if a final control distance is 1100KM and the brevet distance is 1000km, the closing times will be as if the final control distance was 1000KM. 
        
        The close times for final controls are as follows. Times given are relative to the start time of the brevet.

            * 200KM : 13H30 (meaning 13HR 30MIN)
            * 300KM : 20H00
            * 400KM : 27H00
            * 600KM : 40H00
            * 1000KM : 75H00

### Functionality to be Implemented

