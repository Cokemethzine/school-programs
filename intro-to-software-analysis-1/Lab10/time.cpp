//
//
//
//
//
//
//
#include <iostream>
using namespace std;

class Time {
public:
    int h;
    int m;
};

// Part A: return the number of minutes from 00:00 (12:00) until current time
int minutesSinceMidnight(Time time){
    int num_of_mins = time.h*60 + time.m;
    return num_of_mins;
}
int minutesUntil(Time earlier, Time later){
    int num_of_mins = (later.h-earlier.h)*60 + (later.m-earlier.m);
    return num_of_mins;
}

/*int main(){
    Time time1, time2;
    cout << "Enter"<< endl;
    cin >> time1.h >> time1.m;
    cout << "Enter" << endl;
    cin >> time2.h >> time2.m;
}*/

// Part B: return a new moment of time that is 'min' minutes after 'time0'
Time addMinutes(Time time0, int min){
    Time new_time;
    new_time.h = time0.h + (time0.m + min)/60;
    new_time.m = (time0.m+min)%60;
    return new_time;
}

/*int main(){
    Time time1, time2;
    cout << "Enter"<< endl;
    cin >> time1.h >> time1.m;

    time2= addMinutes(time1, 150);
    cout << "Enter" << time2.h << ":" << time2.m << endl;
}
*/

enum Genre {ACTION, COMEDY, DRAMA, ROMANCE, THRILLER};

class Movie { 
public: 
    string title;
    Genre genre;     // only one genre per movie
    int duration;    // in minutes
};

class TimeSlot { 
public: 
    Movie movie;     // what movie
    Time startTime;  // when it starts
};

//Part C: Copied fromt he instructions.
void printMovie(Movie mv){
    string g;
    switch (mv.genre) {
        case ACTION   : g = "ACTION"; break;
        case COMEDY   : g = "COMEDY"; break;
        case DRAMA    : g = "DRAMA";  break;
        case ROMANCE  : g = "ROMANCE"; break;
        case THRILLER : g = "THRILLER"; break;
    }
    cout << mv.title << " " << g << " (" << mv.duration << " min)";
}

//Part C:
void printTimeSlot(TimeSlot ts){
    //Calculate the ending time
    Time endingTime = addMinutes(ts.startTime, ts.movie.duration);
    printMovie(ts.movie);
    cout << " [starts at " << ts.startTime.h << ":" << ts.startTime.m << ", ends by " << endingTime.h << ":" << endingTime.m << "]" << endl;

}


//Part D:
TimeSlot scheduleAfter(TimeSlot ts, Movie nextMovie){
    TimeSlot nextTimeSlot;
    // Since nextTimeSlot is TimeSlot type, we have to determine its 2 members.
    // What movie?
    nextTimeSlot.movie = nextMovie;
    // Starting time  of nextTimeSlot.
    nextTimeSlot.startTime = addMinutes(ts.startTime, ts.movie.duration);
    return nextTimeSlot;
}

//Part E:
bool timeOverlap(TimeSlot ts1, TimeSlot ts2){
    // We need to make sure which one is earlier (ts1 or ts2).
    if (minutesSinceMidnight(ts1.startTime) < minutesSinceMidnight(ts2.startTime) ){
        return ts1.movie.duration > (minutesSinceMidnight(ts2.startTime)- minutesSinceMidnight(ts1.startTime));
    }
    else{
        return ts2.movie.duration > (minutesSinceMidnight(ts1.startTime)- minutesSinceMidnight(ts2.startTime));

    }
}