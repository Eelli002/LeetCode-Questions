class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {
        int sum = 0;
        for (int i = 0; i < sentences.size(); ++i) {
            int wordCount = 0;
            for (int j = 0; j < sentences.at(i).size(); ++j) {
                if (sentences.at(i).at(j) == ' ') wordCount++;
            }
            wordCount++;
            if (wordCount > sum) sum = wordCount;
        }
        return sum;
    }
};