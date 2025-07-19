#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> ret;
    
    arr.erase(unique(arr.begin(), arr.end()), arr.end());
    ret = arr;
    
    return ret;
}