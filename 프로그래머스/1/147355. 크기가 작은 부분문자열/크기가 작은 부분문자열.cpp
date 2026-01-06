#include <string>
#include <vector>

using namespace std;

int solution(string t, string p) {
    int ret = 0;
    int tLen = t.size();
    int pLen = p.size();
    
    for (int i=0; i<=tLen-pLen; i++) {
        if (t.substr(i, pLen) <= p) ret++;
    }
    return ret;
}