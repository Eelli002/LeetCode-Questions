class Solution {
public:
    int minPartitions(string n) 
    {
        int max = n[0] - '0';
        int currChar;
        cout << "Max: " << max << endl;
        for (int i = 0; i < n.size(); i++) 
        {
            currChar = n[i] - '0';
            if (currChar > max) 
            {
                max = currChar;
                cout << "New Max: " << max << endl;
            }
        }
        return max;
    }
};