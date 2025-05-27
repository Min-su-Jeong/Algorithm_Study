#include <bits/stdc++.h>
using namespace std;

const int MAX = 104;
int H, W, graph[MAX][MAX];
string s;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> H >> W;
    for (int i=0; i<H; i++) {
        cin >> s;
        for (int j=0; j<W; j++) {
            if (s[j] == 'c') graph[i][j] = 0;
            else graph[i][j] = -1;
        }
    }
    
    for (int i=0; i<H; i++) {
        for (int j=0; j<W; j++) {
            if (graph[i][j] == 0) {
                int cnt = 1;
                while (graph[i][j+1] == -1) {
                    graph[i][j+1] = cnt++;
                    j++;
                }
            }
        }
    }

    for (int i=0; i<H; i++) {
        for (int j=0; j<W; j++) cout << graph[i][j] << " ";
        cout << "\n";
    }
    return 0;
}