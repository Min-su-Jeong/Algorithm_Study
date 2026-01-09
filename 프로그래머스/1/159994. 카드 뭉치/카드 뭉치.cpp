#include <string>
#include <vector>
#include <queue>

using namespace std;

string solution(vector<string> cards1, vector<string> cards2, vector<string> goal) {
    queue<string> q1, q2;
    
    for (string s: cards1) q1.push(s);
    for (string s: cards2) q2.push(s);
    
    for (string s: goal) {
        if (q1.size() && q1.front() == s) q1.pop();
        else if (q2.size() && q2.front() == s) q2.pop();
        else return "No";
    }
    return "Yes";
}