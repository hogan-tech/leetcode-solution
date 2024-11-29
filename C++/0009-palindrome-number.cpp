class Solution
{
public:
    bool isPalindrome(int x)
    {
        int revert = 0;
        if (x < 0 || (!(x % 10) && x != 0))
        {
            return false;
        }
        while (x > revert)
        {
            revert = revert * 10 + x % 10;
            x /= 10;
        }
        return x == revert || (revert / 10) == x;
    }
};