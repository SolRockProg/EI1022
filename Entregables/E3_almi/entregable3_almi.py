import string
import sys
from copy import deepcopy

from Utils.bt_scheme import PartialSolution, BacktrackingSolver, Solution, Iterable, Tuple


def load_riddle(filename: str) -> ([], string):
    def string_to_tuple(lin: str) -> Tuple:
        lin = lin.split()
        return lin

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            yield string_to_tuple(line)


def n_letters(words) -> int:

    letters = set()
    how_many = 0
    for word in words:
        for letter in word:
            if letter not in letters:
                letters.add(letter)
                how_many += 1
    return how_many


def nice_print(numbers, translator) -> string:
    coded = ""
    answer = ""
    for number in numbers[:-2]:
        coded += number + "+"
        for char in number:
            answer += str(translator[char])
        answer += "+"
    coded += numbers[-2] + " = " + numbers[-1] + " => "
    for char in numbers[-2]:
        answer += str(translator[char])
    answer += " = "
    for char in numbers[-1]:
        answer += str(translator[char])
    coded += answer
    print(coded)

def crypto_solver(words):
    #print(words)
    class CryptoAPS(PartialSolution):

        def __init__(
                self, dict, char_index, word_index, digits_left, sum, current_letter
        ):
            self.dict = dict
            self.n = len(dict)
            self.char_index = char_index
            self.word_index = word_index
            self.digits_left = digits_left
            self.n_words = len(words)
            self.n_chars = len(words[-1])
            self.sum = sum
            self.current_letter = current_letter

        def is_solution(self) -> bool:
            if self.n != n_letters(words):
                return False
            if self.dict[words[-1][0]] == 0:
                return False
            hidden = []
            for word in words:
                number = 0
                for i in range(1, len(word)+1):
                    number += self.dict[word[-i]] * 10 ** (i - 1)
                #print(number)
                hidden.append(number)

            return sum(hidden[:-1]) == hidden[-1]


        def get_solution(self) -> Solution:
            return self.dict

        def feasible(self, digit: int) -> bool:
            #print("sum, digit, index, word index", self.sum, digit, self.char_index, self.word_index)
            known_col = self.word_index < self.n_words - 1
            extra_value = 0


            for i in range(self.word_index + 1, self.n_words):
                word = words[i]
                is_there = self.char_index <= len(word)
                known = not is_there or word[-self.char_index] in self.dict.keys()
                #print(known)
                if not known:
                    known_col = False
                    break
                if is_there and i < self.n_words - 1:
                    extra_value += self.dict[word[-self.char_index]]

            if known_col:
                #print("Esta ", words[-1][-self.char_index], "en dict:",
                #      words[-1][-self.char_index] in self.dict.keys())
                part = (self.sum + (digit + extra_value) * 10 ** (self.char_index - 1))
                left = (part // (10 ** (self.char_index - 1))) % 10
                letter_o = words[-1][-self.char_index]
                right = self.dict[letter_o]
                coherent = left == right
                #print(
                #   "Am ", self.current_letter, ", in (", self.word_index, self.char_index, "letters below value",
                #    extra_value, "total sum is ", self.sum, "plus mine ,",digit,"."
                #    ". Part is ", part, ". That makes ",right, ", which is value of ", letter_o,
                #    "but actually ", left, coherent)



            return  not (digit == 0 and self.char_index == len(words[self.word_index])) and (
                    self.word_index < self.n_words - 1 and (
                    not known_col or
                    known_col and coherent) or
                    not self.word_index < self.n_words - 1 and digit == (self.sum // (10 ** (self.char_index - 1))) % 10
            )

        def next_letter(self) -> string:
            if self.word_index == self.n_words - 1:
                self.word_index = 0
                self.char_index += 1
            else:
                self.word_index += 1

            if self.char_index <= len(words[self.word_index]):
                return words[self.word_index][-self.char_index]
            else:
                return None

        def successors(self) -> Iterable["CryptoAPS"]:
            last = self.word_index == self.n_words and self.char_index == len(words[-1])
            #print("Lo pillo en", self.word_index, self.char_index, self.current_letter)
            right_path = True
            default = True
            while self.current_letter is None or self.current_letter in self.dict.keys():
                right_path = default or self.current_letter is None or self.feasible(self.dict[self.current_letter])
                if not right_path:
                    break
                self.current_letter = self.next_letter()
                #print("E none?", self.current_letter is None)
                default = False
                if self.word_index != self.n_words - 1 and self.current_letter in self.dict.keys():
                    #print("Esto sucede en letra", self.current_letter)
                    self.sum += self.dict[self.current_letter] * 10 ** (self.char_index - 1)
            #print(self.current_letter)
            #print(self.word_index, self.char_index)

            #print(self.current_letter)
            if right_path:
                for digit in self.digits_left:
                    #print("try " + self.current_letter + " = " + str(digit))
                    if self.feasible(digit):
                        sum = self.sum
                        #print("feasible")
                        copy_dict = deepcopy(self.dict)
                        copy_dict[self.current_letter] = digit
                        if self.word_index != self.n_words - 1:
                            sum += digit * 10 ** (self.char_index - 1)
                        digits_left = set(number for number in self.digits_left if number != digit)
                        #print(copy_dict)
                        #print(self.n, n_letters(words))
                        if self.n != n_letters(words) or last:
                            yield CryptoAPS(
                                copy_dict, self.char_index, self.word_index, digits_left, sum, self.current_letter
                            )
            #print("Lo dejo en", self.word_index, self.char_index, self.current_letter)


    initial_pc = CryptoAPS(
        {}, 1, 0, set(n for n in range(10)), 0, words[0][-1]
    )
    # dict, char_index, word_index, digits_left, sum, current_letter
    return BacktrackingSolver.solve(initial_pc)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Faltan argumentos")
    else:
        if len(sys.argv) > 2:
            words = sys.argv[1:]
            sol = crypto_solver(words)
            for solution in sol:
                nice_print(words, solution)

        else:
            for riddle in load_riddle(sys.argv[1]):
                sol = crypto_solver(riddle)
                for solution in sol:
                    nice_print(riddle, solution)
