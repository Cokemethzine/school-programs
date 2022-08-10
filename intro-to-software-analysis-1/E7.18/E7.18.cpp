#include <iostream>
#include <cmath>
using namespace std;

struct Point {
    public:
        double x,y;
};

struct Triangle {
    public:
        Point A,B,C;
};

double distance(Point a, Point b) {
    return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}

double perimeter(Triangle x) {
    double s1 = distance(x.A, x.B);
    double s2 = distance(x.A, x.C);
    double s3 = distance(x.B, x.C);
    return s1 + s2 + s3;
}