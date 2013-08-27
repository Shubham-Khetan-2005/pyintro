#-*- coding: utf-8 -*-
import os
import random


class Hangman:
    database = 'dictionary.txt'

    def __init__(self):
        self.all_words = [word[:-1] for word in open(self.database)]

    def pick_word_length(self):
        self.word_length = int(raw_input('What is the word length? '))

    def pick_a_random_word(self):
        words_available = [
            word for word in self.all_words if len(word) == self.word_length
        ]
        self.word = list(random.choice(words_available).upper())

    def pick_max_tries(self):
        self.max_tries = int(raw_input('Max number of tries: '))

    def init_game(self):
        self.guess = list('-' * self.word_length)
        self.remaining_letters = [
            chr(letter) for letter in range(ord('A'), ord('Z') + 1)
        ]
        self.won = False

    def print_current_status(self):
        os.system('clear')
        # print self.word
        print
        print 'WORD TO GUESS: %s' % ' '.join(self.guess)
        print
        print 'Remaining letters: %s' % ' '.join(self.remaining_letters)
        print
        print 'You have %s guesses left.' % self.max_tries
        print

    def pick_a_letter(self):
        letter = str(raw_input('Enter a letter: ')).upper()
        while not letter in self.remaining_letters:
            print 'This letter is not available, try again!'
            letter = str(raw_input('Enter a letter: ')).upper()
        self.current_letter = letter

    def check_current_letter(self):
        position = 0
        found = False

        for letter in self.word:
            if letter == self.current_letter:
                self.guess[position] = letter
                found = True
            position += 1

        self.remaining_letters.remove(self.current_letter)

        if not found:
            self.max_tries -= 1
            print "The word has no %s!" % (self.current_letter, )

        elif '-' not in self.guess:
            self.won = True
            print "You won! The word is %s" % (''.join(self.word))
            raw_input()

    def start(self):
        self.pick_word_length()
        self.pick_a_random_word()
        self.pick_max_tries()
        self.init_game()

        while not self.won:
            self.print_current_status()
            self.pick_a_letter()
            self.check_current_letter()
            if self.max_tries == 0:
                print 'You lose! The word is %s' % ''.join(self.word)
                raw_input()
                break


if __name__ == '__main__':
    game = Hangman()
    game.start()
