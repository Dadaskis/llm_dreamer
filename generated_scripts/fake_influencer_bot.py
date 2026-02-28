import cv2
import random
import time
import threading
from datetime import datetime
import os

class FakeInfluencer:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.posts = []
        self.running = True
        
        # Predefined ridiculous content templates
        self.templates = [
            "OMG! Just witnessed the most AMAZING {action} in my {location}! #LifeIsGood #InfluencerLife",
            "Did you know that {animal} can {action} better than humans? My {location} is {adjective}! {hashtag}",
            "Why I {action} at {time} in {location}: #InfluencerTruth #RealTalk",
            "My {location} {action} is so {adjective} that my {body_part} is {emotion}! {hashtag}",
            "I {action} {amount} times daily and everyone should too! #LifeHacks {hashtag}",
            "This {object} in my {location} just {action} and I {emotion}! #InfluencerMoments",
            "My {body_part} {action} when {animal} {action} in my {location}! #Viral #Funny",
            "The secret to my {adjective} {location} is: {action} and {action}! {hashtag}"
        ]
        
        # Content categories
        self.categories = {
            'action': ['sway', 'dance', 'jump', 'wave', 'spin', 'bounce', 'sneeze', 'yawn', 'giggle', 'scream'],
            'location': ['bedroom', 'kitchen', 'living room', 'bathroom', 'backyard', 'office', 'bed', 'car'],
            'animal': ['cat', 'dog', 'bird', 'fish', 'hamster', 'rabbit', 'squirrel', 'panda'],
            'adjective': ['amazing', 'crazy', 'wild', 'insane', 'incredible', 'spectacular', 'epic', 'wonderful'],
            'hashtag': ['#InfluencerLife', '#FakeNews', '#Blessed', '#Inspirational', '#Viral', '#Trending'],
            'time': ['morning', 'afternoon', 'evening', 'night', 'early dawn', 'midnight'],
            'body_part': ['nose', 'eyes', 'mouth', 'hands', 'feet', 'ears', 'toes', 'eyebrows'],
            'emotion': ['thrilled', 'excited', 'overwhelmed', 'amazed', 'shocked', 'happy', 'delighted'],
            'object': ['mirror', 'window', 'pillow', 'television', 'lamp', 'book', 'coffee mug', 'plant'],
            'amount': ['once', 'twice', 'three times', 'five times', 'ten times', 'hundreds of times']
        }

    def generate_post(self):
        # Randomly select template and fill with random content
        template = random.choice(self.templates)
        
        post = template
        for category, words in self.categories.items():
            if '{' + category + '}' in post:
                replacement = random.choice(words)
                post = post.replace('{' + category + '}', replacement, 1)
        
        # Add timestamp and fake engagement
        timestamp = datetime.now().strftime("%H:%M")
        likes = random.randint(100, 10000)
        comments = random.randint(10, 500)
        
        return f"[{timestamp}] {post}\n📊 {likes} likes • 💬 {comments} comments"
    
    def capture_frame(self):
        # Capture frame from webcam
        ret, frame = self.cap.read()
        if ret:
            # Add some visual effects to make it more "influencer" style
            frame = cv2.flip(frame, 1)  # Mirror effect
            cv2.putText(frame, "FAKE INFLUENCER", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            cv2.putText(frame, "LIVE NOW", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            return frame
        return None

    def run(self):
        print("Starting Fake Influencer...")
        print("Press Ctrl+C to stop")
        print("\n" + "="*50)
        
        try:
            while self.running:
                # Generate and display influencer post
                post = self.generate_post()
                print(post)
                print("="*50)
                
                # Show webcam feed with "influencer" overlay
                frame = self.capture_frame()
                if frame is not None:
                    cv2.imshow('Fake Influencer', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                
                # Random delay but keep it short for fast posting
                time.sleep(random.uniform(10, 20))
                
        except KeyboardInterrupt:
            print("\nStopping Fake Influencer...")
        finally:
            self.cleanup()

    def cleanup(self):
        self.running = False
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    influencer = FakeInfluencer()
    influencer.run()