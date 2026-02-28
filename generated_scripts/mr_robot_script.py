import random
import time

class RobotButler:
    def __init__(self):
        self.command_history = []
        self.response_count = 0
        self.phrases = {
            "fetch": [
                "Of course, sir! I shall retrieve it with the precision of a Swiss watch and the grace of a ballerina with a suitcase.",
                "Certainly, I shall embark on this noble quest to fetch your item, as if it were the Holy Grail of mundane objects.",
                "Right away, my master! I'll locate your precious object using quantum entanglement and my superior butler intuition.",
                "As you command, I shall seek out your desired item with the thoroughness of a librarian checking out overdue books."
            ],
            "clean": [
                "I shall transform this chaotic space into an orderly paradise, much like a geometrician solving a Rubik's cube while juggling flaming torches.",
                "In a flash! I shall clean this area as if I'm conducting a symphony of dust particles with my invisible butler baton.",
                "It will be done swiftly, with my usual flair for precision cleaning and mild-mannered enthusiasm for perfection.",
                "With great enthusiasm, I shall triumph over this mess like a superhero tackling a pile of dishes with the processing power of a supercomputer."
            ],
            "prepare": [
                "I shall prepare your meal with the culinary expertise of a Michelin-starred chef who also moonlights as a circus performer.",
                "As requested, I shall serve your dining experience with the care of a surgeon, the precision of a clockmaker, and the passion of a cheesecake artist.",
                "Your meal will be ready in the blink of an eye, presented with the elegance of a flower arranging competition and the efficiency of a milkman.",
                "With utmost dedication to gastronomy, I shall craft your dish with the passion of a sommelier, the precision of an engineer, and the creativity of a circus clown."
            ],
            "help": [
                "My goodness, sir! I've been trained to assist with any manner of helpful endeavors. Let me just consult my secret manual of bagpipes and specialized pudding knowledge.",
                "I am here to assist! Though I may require additional coffee, a trip to the restroom, and possibly a brief mental health break.",
                "Hold on a moment while I synchronize my arm movements and make sure my bow tie is perfectly crisp. Your assistance is one of my primary objectives.",
                "I can absolutely help with your request! If it's not something I've never done before, which would certainly be a first for a butler."
            ],
            "default": [
                "I must humbly inform you that I cannot perform that task, yet I have discovered a solution involving glitter, a book of poems, and my quantum magical energy powers.",