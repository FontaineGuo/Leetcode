/*Given an array S of n integers, are there elements
 a, b, c in S such that a + b + c = 0? Find all unique
triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.
For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]*/

#include<iostream>
#include<vector>
#include <algorithm>

using namespace std;

static bool compare(const int &a, const int &b)
{
    return a < b;
}

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end(), compare);
        
        vector<vector<int>> rst;
        
        int len = nums.size();
        
        if(len < 3)
            return rst;
            
        for(int i = 0; i < len; i++)
        {
            if(i>0 && i<len && nums[i] == nums[i-1])//因为数列已经排序，故附近的必然相等
                continue;
                
            int pA = i+1;
            int pB = len-1;
            while(pA<pB)
            {
                int sum = nums[i]+nums[pA]+nums[pB];
                
                if(sum == 0)
                {

                    vector<int> temp;
                    temp.push_back(nums[i]);
                    temp.push_back(nums[pA]);
                    temp.push_back(nums[pB]);
                    rst.push_back(temp);
                   
                    while(++pA<pB && nums[pA]==nums[pA-1]){}
                    cout<< "i = " << i << " pA = " << pA << " pB = " << pB << endl;
                    while(--pB>pA && nums[pB]==nums[pB+1]){}
                    cout<< "i = " << i << " pA = " << pA << " pB = " << pB << endl;
                }
                
                else if(sum < 0)
                    pA++;
                else
                    pB--;
            }
        }
        return rst;
    }
};

int main()
{   
    int v[7] = {-1, 0, 2, 1, 0, 1,0};
    vector<int> samples(&v[0], &v[6]);
    vector<vector<int>> rst ; 
    Solution s;
    rst = s.threeSum(samples);


    for(int i = 0; i < rst.size(); i++)
    {
        for(int j = 0; j < 3; j++)
        {
            cout << rst[i][j] << ",";
        }
    }
}