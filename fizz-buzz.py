class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string>ans;
        for(int i=1; i<=n; i++)
        { 
            string name;
            if(i%3==0 && i%5==0)
                 name+="FizzBuzz";
            else if(i%3==0)
                 name+="Fizz";
            else if(i%5==0)
                 name+="Buzz";
            else 
                 name=to_string(i);
            ans.push_back(name);
                 
        }
    
       return ans;
    }

};
