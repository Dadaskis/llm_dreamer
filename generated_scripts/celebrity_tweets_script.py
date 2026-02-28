#!/usr/bin/env python3
import sys
import random
import re
from collections import Counter

class CelebrityTweeter:
    def __init__(self, celebrity_style):
        self.celebrity = celebrity_style.lower()
        self.setup_style_patterns()
        
    def setup_style_patterns(self):
        """Define style patterns for different celebrities"""
        self.styles = {
            'kanyewest': {
                'caps_chance': 0.3,
                'typo_methods': ['double_consonant', 'drop_vowel', 'phonetic'],
                'hashtag_source': ['thoughts', 'feelings', 'random_absurd'],
                'sentence_enders': ['', '!!!', '??', '...'],
                'common_misspellings': {
                    'the': 'teh', 'and': 'adn', 'you': 'u', 'are': 'r',
                    'love': 'lvoe', 'believe': 'beleive', 'people': 'ppl'
                },
                'phrase_replacements': [
                    ('i am', 'im'),
                    ('i think', 'i thinkk'),
                    ('you are', 'ur'),
                    ('going to', 'gonna'),
                    ('got to', 'gotta')
                ]
            },
            'trump': {
                'caps_chance': 0.6,
                'typo_methods': ['cap_random', 'simple_misspelling'],
                'hashtag_source': ['political', 'simple_words'],
                'sentence_enders': ['', '!', 'VERY!'],
                'common_misspellings': {
                    'america': 'amerika', 'winning': 'wining', 
                    'disaster': 'disater', 'tremendous': 'tremendus'
                },
                'phrase_replacements': [
                    ('make america great again', 'MAGA'),
                    ('fake news', 'FAKE NEWS'),
                    ('the best', 'the BEST'),
                    ('so sad', 'SAD!')
                ]
            },
            'beyonce': {
                'caps_chance': 0.2,
                'typo_methods': ['aesthetic', 'drop_letter'],
                'hashtag_source': ['empowerment', 'royal'],
                'sentence_enders': ['', '💕', '✨', '🔥'],
                'common_misspellings': {
                    'love': 'luv', 'queen': 'qween', 'run': 'runn',
                    'flawless': 'flawlesss'
                },
                'phrase_replacements': [
                    ('i am', 'im'),
                    ('formation', 'formation'),
                    ('sasha fierce', 'sasha fierce')
                ]
            },
            'elonmusk': {
                'caps_chance': 0.4,
                'typo_methods': ['tech_abbr', 'missing_space'],
                'hashtag_source': ['tech', 'math', 'space'],
                'sentence_enders': ['', '🚀', '⚡', '🔥'],
                'common_misspellings': {
                    'mars': 'Mars', 'tesla': 'TESLA', 'rocket': 'rockett',
                    'the': 'teh', 'and': '&'
                },
                'phrase_replacements': [
                    ('going to', 'gonna'),
                    ('rocket', 'rocket'),
                    ('mars', 'Mars'),
                    ('electric', ' ELECTRIC')
                ]
            }
        }
        
        if self.celebrity not in self.styles:
            # Default style if celebrity not found
            self.celebrity = 'kanyewest'
            
        self.style = self.styles[self.celebrity]
        
        # Nonsense hashtag generators
        self.hashtag_banks = {
            'thoughts': ['deepthoughts', 'randomness', 'philosophy', 'mindblown', 'thinking'],
            'feelings': ['feelinggood', 'emotions', 'vibes', 'energy', 'soul'],
            'random_absurd': ['banana', 'spoon', 'quantum', 'toaster', 'pineapple',
                            'cheese', 'waffle', 'ninja', 'penguin', 'dinosaur'],
            'political': ['maga', 'usa', 'freedom', 'patriot', 'america',
                         'winning', 'greatness', 'truth', 'news'],
            'simple_words': ['yes', 'no', 'maybe', 'ok', 'hi', 'bye', 'wow'],
            'empowerment': ['queen', 'slay', 'flawless', 'runworld', 'girlpower',
                           'royalty', 'crown', 'throneroom'],
            'royal': ['queen', 'king', 'royal', 'crown', 'throne', 'royalty'],
            'tech': ['code', 'hack', 'ai', 'future', 'tech', 'innovation',
                    'algorithm', 'quantum'],
            'math': ['π', '∑', '∞', 'math', 'calculate', 'equation', 'logic'],
            'space': ['mars', 'spacex', 'rocket', 'stars', 'orbit', 'galaxy',
                     'universe', 'moon']
        }
    
    def process_text(self, text):
        """Main processing function"""
        # Split into sentences
        sentences = self.split_into_sentences(text)
        
        output_tweets = []
        for sentence in sentences:
            if not sentence.strip():
                continue
                
            # Process sentence
            processed = self.apply_style(sentence)
            
            # Break into tweet-length chunks
            chunks = self.chunk_for_twitter(processed)
            output_tweets.extend(chunks)
            
        return output_tweets
    
    def split_into_sentences(self, text):
        """Split text into sentences (simple version)"""
        # Replace multiple spaces with single space
        text = re.sub(r'\s+', ' ', text.strip())
        
        # Split on sentence endings
        sentences = re.split(r'(?<=[.!?])\s+', text)
        
        # Clean up
        return [s.strip() for s in sentences if s.strip()]
    
    def apply_style(self, text):
        """Apply celebrity style transformations"""
        words = text.split()
        transformed_words = []
        
        for i, word in enumerate(words):
            # Lowercase for processing
            original_word = word
            word_lower = word.lower().strip('.,!?;:"\'')
            
            # 1. Apply phrase replacements (whole phrases)
            if i > 0:
                prev_word = words[i-1].lower().strip('.,!?;:"\'')
                for old, new in self.style['phrase_replacements']:
                    if f"{prev_word} {word_lower}" == old:
                        transformed_words[-1] = new.split()[0] if ' ' in new else new
                        word = new.split()[1] if ' ' in new else ''
                        break
            
            # 2. Apply common misspellings
            if word_lower in self.style['common_misspellings']:
                word = self.style['common_misspellings'][word_lower]
            else:
                # 3. Random typos based on style
                if random.random() < 0.15:  # 15% chance for typo
                    word = self.apply_random_typo(word)
            
            # 4. Random capitalization
            if random.random() < self.style['caps_chance']:
                word = word.upper()
            elif random.random() < 0.1:  # 10% chance for random caps
                word = ''.join([c.upper() if random.random() < 0.5 else c.lower() 
                              for c in word])
            
            # 5. Add emoji/text emoji based on style
            if random.random() < 0.2:
                emoji = random.choice(['💕', '✨', '🔥', '🚀', '⚡', '😂', '👏'])
                word = word + emoji
            
            if word:  # Only add non-empty words
                transformed_words.append(word)
        
        result = ' '.join(transformed_words)
        
        # 6. Add random sentence ender
        if random.random() < 0.3:
            result += random.choice(self.style['sentence_enders'])
        
        return result
    
    def apply_random_typo(self, word):
        """Apply random typo based on celebrity style"""
        method = random.choice(self.style['typo_methods'])
        
        if len(word) < 3:
            return word
            
        if method == 'double_consonant':
            # Double a consonant (except at end)
            consonants = 'bcdfghjklmnpqrstvwxyz'
            for i in range(len(word)-1):
                if word[i].lower() in consonants and word[i+1].lower() != word[i].lower():
                    return word[:i+1] + word[i] + word[i+1:]
                    
        elif method == 'drop_vowel':
            # Drop a vowel (except first letter)
            vowels = 'aeiou'
            for i in range(1, len(word)):
                if word[i].lower() in vowels and random.random() < 0.5:
                    return word[:i] + word[i+1:]
                    
        elif method == 'phonetic':
            # Common phonetic misspellings
            phonetic_map = {
                'ph': 'f', 'gh': 'f', 'ck': 'k', 'qu': 'kw',
                's': 'z', 'c': 'k', 'the': 'teh'
            }
            for old, new in phonetic_map.items():
                if old in word.lower():
                    return word.replace(old, new)
                    
        elif method == 'cap_random':
            # Already handled in main loop
            return word
            
        elif method == 'simple_misspelling':
            # Swap adjacent letters
            i = random.randint(0, len(word)-2)
            return word[:i] + word[i+1] + word[i] + word[i+2:]
            
        elif method == 'aesthetic':
            # Remove vowels aesthetically
            if len(word) > 4 and random.random() < 0.5:
                return ''.join([c for i, c in enumerate(word) 
                              if i % 2 == 0 or c.lower() not in 'aeiou'])
                
        elif method == 'missing_space':
            # This would run between words, handled separately
            return word
            
        elif method == 'tech_abbr':
            # Abbreviate common tech words
            tech_abbrs = {
                'you': 'u', 'are': 'r', 'the': 'teh', 'and': '&',
                'for': '4', 'to': '2', 'too': '2', 'be': 'b',
                'see': 'c', 'why': 'y', 'excellent': 'excelnt'
            }
            word_lower = word.lower()
            for full, abbr in tech_abbrs.items():
                if word_lower == full:
                    return abbr
        
        return word
    
    def chunk_for_twitter(self, text):
        """Break text into tweet-sized chunks (280 chars)"""
        words = text.split()
        chunks = []
        current_chunk = []
        current_length = 0
        
        for word in words:
            word_len = len(word)
            # Account for space if not first word
            space_len = 1 if current_chunk else 0
            
            if current_length + space_len + word_len > 280:
                if current_chunk:
                    chunks.append(' '.join(current_chunk))
                current_chunk = [word]
                current_length = word_len
            else:
                current_chunk.append(word)
                current_length += space_len + word_len
        
        if current_chunk:
            chunks.append(' '.join(current_chunk))
            
        # Add hashtags to each chunk
        result_chunks = []
        for chunk in chunks:
            # 1-3 random hashtags
            num_hashtags = random.randint(1, 3)
            
            # Select hashtag source based on celebrity
            source = random.choice(self.style['hashtag_source'])
            bank = self.hashtag_banks[source]
            
            hashtags = []
            for _ in range(num_hashtags):
                if random.random() < 0.7:  # 70% from bank
                    hashtag = random.choice(bank)
                else:  # 30% nonsense generated
                    hashtag = self.generate_nonsense_hashtag()
                hashtags.append(f"#{hashtag}")
            
            # Mix in some words from the text as hashtags too
            if random.random() < 0.4 and len(chunk.split()) > 3:
                chunk_words = [w.lower().strip('.,!?;:"\'') 
                             for w in chunk.split() 
                             if len(w) > 3 and w.isalpha()]
                if chunk_words:
                    word_hashtag = random.choice(chunk_words)
                    hashtags.append(f"#{word_hashtag}")
            
            # Combine
            final_chunk = chunk
            if hashtags:
                final_chunk += ' ' + ' '.join(hashtags)
                
            result_chunks.append(final_chunk)
            
        return result_chunks
    
    def generate_nonsense_hashtag(self):
        """Generate a nonsense hashtag"""
        patterns = [
            lambda: ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(5, 8))),
            lambda: f"{random.choice(['get', 'love', 'hate', 'need', 'want'])}"
                   f"{random.choice(['this', 'that', 'them', 'us'])}",
            lambda: f"{random.choice(['real', 'true', 'fake', 'new'])}"
                   f"{random.choice(['talk', 'news', 'facts', 'story'])}"
        ]
        return random.choice(patterns)()

def main():
    if len(sys.argv) < 2:
        print("Usage: python celebrity_tweets.py <input_file> [celebrity]")
        print("Available celebrities: kanyewest, trump, beyonce, elonmusk")
        sys.exit(1)
    
    input_file = sys.argv[1]
    celebrity = sys.argv[2] if len(sys.argv) > 2 else 'kanyewest'
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    tweeter = CelebrityTweeter(celebrity)
    tweets = tweeter.process_text(text)
    
    print(f"Generated {len(tweets)} tweet(s) in the style of {celebrity}:")
    print("-" * 50)
    for i, tweet in enumerate(tweets, 1):
        print(f"Tweet {i} ({len(tweet)} chars):")
        print(tweet)
        print()

if __name__ == "__main__":
    main()