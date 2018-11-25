#include <iostream>
#include <vector>

using namespace std;

vector<int> solution(vector<int> &A, int K);

int main()
{
    vector<int> arr = {};
    int K = -1;
    vector<int> result = solution(arr, K);

    for(unsigned int i = 0; i < arr.size() ; i++){
        cout <<  result[i] << ' ';
    }
    cout << endl;
}

vector<int> solution(vector<int> &A, int K) {
    // write your code in C++14 (g++ 6.2.0)
    if( A.empty() == true ){
        return A;
    }

    if(K < 0){
        K = A.size() + K ;
    }

    vector<int> shiftedA;

    for(unsigned int i = A.size() - (K % A.size()); i < A.size(); i++){
        shiftedA.push_back( A[i] );
    }

    for(unsigned int j = 0; j < A.size() - (K % A.size()); j++){
        shiftedA.push_back( A[j] );
    }

    return shiftedA;
}
