#include <bits/stdc++.h>
using namespace std;


char a[51], c[3];
double b, ret, cnt, tmp;

int main() {
    for (int i=0; i<20; i++) {
        scanf("%s %lf %s", a, &b, c);
        if (c[0] == 'P') continue;

        cnt += b;
        if (c[0] == 'F') continue;

        if (c[0] == 'A') tmp = 4;
        else if (c[0] == 'B') tmp = 3;
        else if (c[0] == 'C') tmp = 2;
        else tmp = 1;

        if (c[1] == '+') tmp += 0.5;
        ret += b * tmp;
    }
    printf("%lf\n", ret/cnt);
    
    return 0;
}