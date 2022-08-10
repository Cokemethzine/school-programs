#include <iostream>
#include <cmath>
using namespace std;

struct Point {
    public:
        double x,y;
};

double distance(Point a, Point b) {
    return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}