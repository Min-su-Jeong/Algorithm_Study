#include <bits/stdc++.h>
using namespace std;

const int MAX = 14;
const int dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
const int dy[8] = {-1, 0, 1, -1, 1, -1, 0, 1};
int N, M, K, ret, A[MAX][MAX], feed[MAX][MAX];
vector<int> a[MAX][MAX];

void springSummer() {
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            if (a[i][j].size() == 0) continue;
            int die_tree = 0;
            sort(a[i][j].begin(), a[i][j].end());

            vector<int> tmp;
            for (int tree: a[i][j]) {
                if (feed[i][j] >= tree) {
                    feed[i][j] -= tree;
                    tmp.push_back(tree+1);
                } else {
                    die_tree += tree / 2;
                }
            }
            a[i][j] = tmp;
            feed[i][j] += die_tree;
        }
    }
}

void fall() {
    for (int y=0; y<N; y++) {
        for (int x=0; x<N; x++) {
            if (a[y][x].size() == 0) continue;
            for (int tree: a[y][x]) {
                if (tree % 5 == 0) {
                    for (int i=0; i<8; i++) {
                        int ny = y + dy[i];
                        int nx = x + dx[i];
                        if (ny < 0 || ny >= N || nx < 0 || ny >= N) continue;
                        a[ny][nx].push_back(1);
                    }
                }
            }
        }
    }
}

void winter() {
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            feed[i][j] += A[i][j];
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N >> M >> K;
    fill(&feed[0][0], &feed[0][0]+MAX*MAX, 5);
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> A[i][j];
        }
    }
    for (int i=0; i<M; i++) {
        int x, y, z;
        cin >> x >> y >> z; x--; y--;
        a[x][y].push_back(z);
    }
    for (int i=0; i<K; i++) {
        springSummer(); fall(); winter();
    }
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            ret += a[i][j].size();
        }
    }
    cout << ret << '\n';
    return 0;
}