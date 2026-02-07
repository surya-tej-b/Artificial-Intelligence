class ExtractGraph:

    #  ​‌​​‌​​‌​‌‌​​‌‌‌​‌‌​‌‌‌​​‌‌​‌‌‌‌​‌‌‌​​‌​​‌‌​​‌​‌​​‌​​​​​​‌‌​​​​‌​‌‌​‌‌​​​‌‌​‌‌​​​​‌​​​​​​‌‌‌​​​​​‌‌‌​​‌​​‌‌​​‌​‌​‌‌‌​‌‌​​‌‌​‌​​‌​‌‌​‌‌‌‌​‌‌‌​‌​‌​‌‌‌​​‌‌​​‌​​​​​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌‌​​‌‌​‌‌‌​‌​​​‌‌‌​​‌​​‌‌‌​‌​‌​‌‌​​​‌‌​‌‌‌​‌​​​‌‌​‌​​‌​‌‌​‌‌‌‌​‌‌​‌‌‌​​‌‌‌​​‌‌​​‌​‌‌‌​​​‌​​​​​​‌​​‌‌‌​​‌‌​‌‌‌‌​‌‌‌​‌‌‌​​‌​​​​​​‌‌​​​​‌​‌‌​‌‌‌​​‌‌‌​​‌‌​‌‌‌​‌‌‌​‌‌​​‌​‌​‌‌‌​​‌​​​‌​​​​​​‌‌‌​​​‌​‌‌‌​‌​‌​‌‌​​‌​‌​‌‌‌​​‌‌​‌‌‌​‌​​​‌‌​‌​​‌​‌‌​‌‌‌‌​‌‌​‌‌‌​​‌‌‌​​‌‌​​‌​​​​​​‌‌​​​​‌​‌‌​‌‌‌​​‌‌​​‌​​​​‌​​​​​​‌‌‌​​​​​‌‌‌​​‌​​‌‌​‌‌‌‌​‌‌‌​‌‌​​‌‌​‌​​‌​‌‌​​‌​​​‌‌​​‌​‌​​‌​​​​​​‌‌​​‌‌‌​‌‌‌​‌​‌​‌‌​‌​​‌​‌‌​​‌​​​‌‌​​​​‌​‌‌​‌‌‌​​‌‌​​​‌‌​‌‌​​‌​‌​​‌​​​​​​‌‌​‌​​‌​‌‌​‌‌‌​​​‌​​​​​​‌‌​​​​‌​​‌​​​​​​‌‌​​‌‌​​‌‌​​​​‌​‌‌​‌​​‌​‌‌‌​‌​​​‌‌​‌​​​​‌‌​​‌‌​​‌‌‌​‌​‌​‌‌​‌‌​​​​‌​​​​​​‌‌‌​‌‌‌​‌‌​​​​‌​‌‌‌‌​​‌​​‌​​​​​​‌‌​​​‌​​‌‌‌​‌​‌​‌‌‌​‌​​​​‌​​​​​​‌‌​​‌‌‌​‌‌​​‌​‌​‌‌​‌‌‌​​‌‌​​‌​‌​‌‌‌​​‌​​‌‌​​​​‌​‌‌‌​‌​​​‌‌​​‌​‌​​‌​​​​​​‌‌‌​‌‌‌​‌‌‌​​‌​​‌‌​‌‌‌‌​‌‌​‌‌‌​​‌‌​​‌‌‌​​‌​​​​​​‌‌​​​‌‌​‌‌​‌‌‌‌​‌‌​​‌​​​‌‌​​‌​‌​‌‌‌​​‌‌​​‌​‌‌‌​Please add comments along with your code.
    #  ​‌​​‌​​‌​‌‌​​‌‌‌​‌‌​‌‌‌​​‌‌​‌‌‌‌​‌‌‌​​‌​​‌‌​​‌​‌​​‌​​​​​​‌‌​​​​‌​‌‌​‌‌​​​‌‌​‌‌​​​​‌​​​​​​‌‌‌​​​​​‌‌‌​​‌​​‌‌​​‌​‌​‌‌‌​‌‌​​‌‌​‌​​‌​‌‌​‌‌‌‌​‌‌‌​‌​‌​‌‌‌​​‌‌​​‌​​​​​​‌‌​‌​​‌​‌‌​‌‌‌​​‌‌‌​​‌‌​‌‌‌​‌​​​‌‌‌​​‌​​‌‌‌​‌​‌​‌‌​​​‌‌​‌‌‌​‌​​​‌‌​‌​​‌​‌‌​‌‌‌‌​‌‌​‌‌‌​​‌‌‌​​‌‌​​‌​‌‌‌​​​‌​​​​​​‌​​‌‌‌​​‌‌​‌‌‌‌​‌‌‌​‌‌‌​​‌​​​​​​‌‌​​​​‌​‌‌​‌‌‌​​‌‌‌​​‌‌​‌‌‌​‌‌‌​‌‌​​‌​‌​‌‌‌​​‌​​​‌​​​​​​‌‌‌​​​‌​‌‌‌​‌​‌​‌‌​​‌​‌​‌‌‌​​‌‌​‌‌‌​‌​​​‌‌​‌​​‌​‌‌​‌‌‌‌​‌‌​‌‌‌​​‌‌‌​​‌‌​​‌​​​​​​‌‌​​​​‌​‌‌​‌‌‌​​‌‌​​‌​​​​‌​​​​​​‌‌‌​​​​​‌‌‌​​‌​​‌‌​‌‌‌‌​‌‌‌​‌‌​​‌‌​‌​​‌​‌‌​​‌​​​‌‌​​‌​‌​​‌​​​​​​‌‌​​‌‌‌​‌‌‌​‌​‌​‌‌​‌​​‌​‌‌​​‌​​​‌‌​​​​‌​‌‌​‌‌‌​​‌‌​​​‌‌​‌‌​​‌​‌​​‌​​​​​​‌‌​‌​​‌​‌‌​‌‌‌​​​‌​​​​​​‌‌​​​​‌​​‌​​​​​​‌‌​​‌‌​​‌‌​​​​‌​‌‌​‌​​‌​‌‌‌​‌​​​‌‌​‌​​​​‌‌​​‌‌​​‌‌‌​‌​‌​‌‌​‌‌​​​​‌​​​​​​‌‌‌​‌‌‌​‌‌​​​​‌​‌‌‌‌​​‌​​‌​​​​​​‌‌​​​‌​​‌‌‌​‌​‌​‌‌‌​‌​​​​‌​​​​​​‌‌​​‌‌‌​‌‌​​‌​‌​‌‌​‌‌‌​​‌‌​​‌​‌​‌‌‌​​‌​​‌‌​​​​‌​‌‌‌​‌​​​‌‌​​‌​‌​​‌​​​​​​‌‌‌​‌‌‌​‌‌‌​​‌​​‌‌​‌‌‌‌​‌‌​‌‌‌​​‌‌​​‌‌‌​​‌​​​​​​‌‌​​​‌‌​‌‌​‌‌‌‌​‌‌​​‌​​​‌‌​​‌​‌​‌‌‌​​‌‌​​‌​‌‌‌​key is head word; value stores next word and corresponding probability.
    graph = {}

    sentences_add = "assign1_sentences.txt"

    def __init__(self):
        # Extract the directed weighted graph, and save to {head_word, {tail_word, probability}}
        # Read sentences from the file
        with open(self.sentences_add, 'r', encoding='utf-8') as f:
            sentences = f.readlines()
        
        # Dictionary to store word transition counts: {head_word: {tail_word: count}}
        word_counts = {}
        
        # Process each sentence
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
            
            # Split by whitespace to get words
            words = sentence.split()
            
            # Count transitions between consecutive words
            for i in range(len(words) - 1):
                head_word = words[i]
                tail_word = words[i + 1]
                
                # Initialize nested dictionary if needed
                if head_word not in word_counts:
                    word_counts[head_word] = {}
                
                # Increment count for this transition
                if tail_word not in word_counts[head_word]:
                    word_counts[head_word][tail_word] = 0
                word_counts[head_word][tail_word] += 1
        
        # Convert counts to probabilities
        for head_word in word_counts:
            # Calculate total transitions from this head word
            total_count = sum(word_counts[head_word].values())
            
            # Convert each count to probability
            self.graph[head_word] = {}
            for tail_word in word_counts[head_word]:
                probability = word_counts[head_word][tail_word] / total_count
                self.graph[head_word][tail_word] = probability
        
        print("*"*100)
        print("Finished!")
        
        return

    def getProb(self, head_word, tail_word):
        """
        Get the probability of tail_word appearing after head_word.
        
        Args:
            head_word: The word before the transition
            tail_word: The word after the transition
            
        Returns:
            Probability of the transition (0.0 if not found)
        """
        # Check if head_word exists in graph
        if head_word not in self.graph:
            return 0.0
        
        # Check if tail_word exists after head_word
        if tail_word not in self.graph[head_word]:
            return 0.0
        
        # Return the probability
        return self.graph[head_word][tail_word]
