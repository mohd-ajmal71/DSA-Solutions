class Solution {
    public String processStr(String s)
    { 
        StringBuilder sb=new StringBuilder("");
        for(char ch:s.toCharArray())
        {
            if(Character.isLetter(ch))
            {
                sb.append(ch);
            }
            else if(ch=='*')
            {
                if(sb.length()==0)
                {
                    continue;

                }
                sb.deleteCharAt(sb.length()-1);
            }
            else if(ch=='#')
            {
                sb.append(sb);

            }
            else if(ch=='%')
            {
                sb.reverse();
            }
        }
        
        return sb.toString();
    }
}