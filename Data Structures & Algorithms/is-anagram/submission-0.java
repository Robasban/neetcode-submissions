class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()) return false;
        HashMap<Character, Integer> bob = new HashMap<Character, Integer>();
        HashMap<Character, Integer> bob2 = new HashMap<Character, Integer>();
        for(int i=0; i<s.length(); i++){;
            if(!bob.containsKey(s.charAt(i))) bob.put(s.charAt(i), 1);
            else bob.put(s.charAt(i), bob.get(s.charAt(i))+1);
            if(!bob2.containsKey(t.charAt(i))) bob2.put(t.charAt(i), 1);
            else bob2.put(t.charAt(i), bob2.get(t.charAt(i))+1);
        }
        return bob.equals(bob2);

    }
}
