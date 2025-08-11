class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        
        freq_s1 = defaultdict(int)
        freq_window = defaultdict(int)
        
        # Build frequency map for s1
        for char in s1:
            freq_s1[char] = freq_s1[char] + 1
        
        # Initialize first window
        for i in range(len(s1)):
            char = s2[i]
            freq_window[char] = freq_window[char] + 1
        
        if freq_window == freq_s1:
            return True
        
        # Slide the window
        for i in range(len(s1), len(s2)):
            # Add new character
            char_add = s2[i]
            freq_window[char_add] = freq_window[char_add] + 1
            
            # Remove old character
            char_remove = s2[i - len(s1)]
            freq_window[char_remove] -= 1
            if freq_window[char_remove] == 0:
                del freq_window[char_remove]
            
            if freq_window == freq_s1:
                return True
        
        return False