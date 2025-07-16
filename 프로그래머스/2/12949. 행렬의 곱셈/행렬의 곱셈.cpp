#include <vector>
using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
    int N = arr1.size();
    int M = arr2.size();
    int K = arr2[0].size();

    vector<vector<int>> ret(N, vector<int>(K, 0));

    for (int i = 0; i < N; ++i) {
        for (int k = 0; k < M; ++k) {
            for (int j = 0; j < K; ++j) {
                ret[i][j] += arr1[i][k] * arr2[k][j];
            }
        }
    }

    return ret;
}