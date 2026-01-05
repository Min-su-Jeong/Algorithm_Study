#include <string>
#include <vector>
#include <deque>

using namespace std;

int solution(int n, int m, vector<int> section) {
    int ret = 0;
    
    deque<int> q;
    for (int i: section) q.push_back(i);
    
    while (q.size()) {
        int start = q.front(); q.pop_front();
        while (q.size() && start + m > q.front()) q.pop_front();
        ret++;
    }
    return ret;
}