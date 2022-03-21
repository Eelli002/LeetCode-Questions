class Solution {
public:
    int minimumSum(int num) {
        string numString = to_string(num);
        int charToInt;
        
        char minString1 = numString[0];
        int minInt1 = minString1 - '0';
        int minIndex1 = 0;     
        for (int i = 0; i < numString.size(); ++i) {
            charToInt = numString[i] - '0';
            // cout << "charToInt Loop1 : " << charToInt << endl;
            if (charToInt < minInt1) {
                cout << "NEW MIN FOUND!!" << endl;
                minString1 = numString[i];
                minInt1 = minString1 - '0';
                cout << "The new min is: " << minInt1 << endl;
                minIndex1 = i;
            }
            // cout << minInt1 << endl;
        }
        cout << "Final minInt1: " << minInt1 << endl;
        cout << "minIndex1: " << minIndex1 << endl;
        numString.erase(minIndex1, 1);
        
        
        char minString2 = numString[0];
        int minInt2 = minString2 - '0';
        int minIndex2 = 0;
        for (int i = 0; i < numString.size(); ++i) {
            charToInt = numString[i] - '0';
            if (charToInt < minInt2) {
                minString2 = numString[i];
                minInt2 = minString2 - '0';
                minIndex2 = i;
                // cout << minIndex1 << endl;
            }
        }
        cout << "minInt2: " << minInt2 << endl;
        cout << "minIndex2: " << minIndex2 << endl;
        numString.erase(minIndex2, 1);
        
        int minTotal = (minInt1 + minInt2) * 10;
        int max1 = numString[0] - '0';
        int max2 = numString[1] - '0';
        cout << "minTotal: " << minTotal << endl;
        cout <<  "Max1: " << max1 << endl << "Max2 " << max2 << endl;
        
        minTotal += (max1 + max2);
        
        // take biggest two
        // add two max together, mulitply by 10
        // add final two numbers
        return minTotal;
        
    }
};