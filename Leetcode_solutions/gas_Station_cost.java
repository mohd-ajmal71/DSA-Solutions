class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost)
    { 
        int curr_petrol=0;
        int idx=0;
        int total_gas=0;
        int total_cost=0;
        for(int i=0;i<gas.length;i++)
        {
            total_gas+=gas[i];
            total_cost+=cost[i];
            curr_petrol+=gas[i]-cost[i];
            if(curr_petrol<0)
            {
                curr_petrol=0;
                idx=i+1;

            }

        }
        if(total_gas<total_cost)
        {
            return -1;
        }
        return idx;
        
    }
}