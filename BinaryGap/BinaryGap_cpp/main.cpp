#include <iostream>
#include <vector>

using namespace std;

int solution(int N);
vector<int> toBinary(int N);

int main()
{

}

int solution(int N) {
    vector<int> arr = toBinary(N);
    int theBestGap = 0;
    for(unsigned int i = 0; i < arr.size(); i++ ){
        int countGaps = 0;
        if(arr[i] == 1){
            for(unsigned int k = i+1; (arr[k] == 0) && (k < arr.size()); k++){
                countGaps += 1;
            }

            if(theBestGap <= countGaps ){
                theBestGap = countGaps;
            }
        }
    }
    return theBestGap;
}

vector<int> toBinary(int N){
    vector<int> arr;
    for(int i=0; N>0; i++){
        arr.push_back(N % 2);
        N = N/2;
    }
    return arr;
}
