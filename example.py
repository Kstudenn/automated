def factorial(n):
    """
    Computes the factorial of n.
    """
    if n < 0:
        raise ValueError('received negative input')
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

factorial(5)

def test_factorial_numbers():
    assert factorial(5)==120
    assert factorial(3)==6
    assert factorial(11)==39916800

def count_word_occurrence_in_string(text, word):
    """
    Counts how often word appears in text.
    Example: if text is "one two one two three four"
             and word is "one", then this function returns 2
    """
    words = text.split()
    return words.count(word)

def test_count_word_occurrence_in_string():
    assert count_word_occurrence_in_string('AAA BBB', 'AAA') == 1
    assert count_word_occurrence_in_string('AAA AAA', 'AAA') == 2
    # What does this last test tell us?
    assert count_word_occurrence_in_string('AAAAA', 'AAA') == 1
    
    
def count_word_occurrence_in_file(file_name, word):
    """
    Counts how often word appears in file file_name.
    Example: if file contains "one two one two three four"
             and word is "one", then this function returns 2
    """
    count = 0
    with open(file_name, 'r') as f:
        for line in f:
            words = line.split()
            count += words.count(word)
    return count

    
import tempfile
import os

def test_count_word_occurrence_in_file():
    _, temporary_file_name = tempfile.mkstemp()
    with open(temporary_file_name, 'w') as f:
        f.write("1 2 2 3 1 4 5 6 1 6 1 2")
    count = count_word_occurrence_in_file(temporary_file_name, "1")
    assert count == 4
    os.remove(temporary_file_name)
    
    
    

def check_reactor_temperature(temperature_celsius):       
    """
    Checks whether temperature is above max_temperature
    and returns a status.
    """
    #from reactor import max_temperature
    if temperature_celsius > max_temperature:
        status = 1
    else:
        status = 0
    return status

def test_set_temp(monkeypatch):
    monkeypatch.setattr(reactor, "max_temperature", 100)
    assert check_reactor_temperature(99)  == 0
    assert check_reactor_temperature(100) == 0   # boundary cases easily go wrong
    assert check_reactor_temperature(101) == 1


class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
    def go_for_a_walk(self):  # <-- how would you test this function?
        self.hunger += 1
        
def test_pet():
    p = Pet('asdf')
    assert p.hunger == 0
    p.go_for_a_walk()
    assert p.hunger == 1

    p.hunger = -1
    p.go_for_a_walk()
    assert p.hunger == 0



