import unittest

def chance(lst):
    return sum(lst)

def yatzy(lst):
    return 50 if len(set(lst)) == 1 else 0

def ones_twos_threes_fours_fives_sixes(lst, num):
  if num not in lst:
    return 0

  if num in lst:
    return lst.count(num) * num

class TestChance(unittest.TestCase):
    def test_chance(self):
      # Arrange
      dice = [1,1,3,3,6]

      # Act
      result = chance(dice)

      # Assert
      self.assertEqual(result, (1+1+3+3+6))

class TestChance2(unittest.TestCase):
    def test_chance(self):
      # Arrange
      dice = [4,5,5,6,1]

      # Act
      result = chance(dice)

      # Assert
      self.assertEqual(result, (4+5+5+6+1))

class TestYatzy(unittest.TestCase):
    def test_yatzy(self):
      # Arrange
      dice = [1,1,1,1,1]

      # Act
      result = yatzy(dice)

      # Assert
      self.assertEqual(result, 50)

class TestYatzy2(unittest.TestCase):
    def test_yatzy(self):
      # Arrange
      dice = [1,1,1,2,1]

      # Act
      result = yatzy(dice)

      # Assert
      self.assertEqual(result, 0)

class TestOnesTwosThreesFoursFivesSixes(unittest.TestCase):
    def test_ones_twos_threes_fours_fives_sixes(self):
      # Arrange
      dice = [1,1,2,4,4]

      # Act
      result = ones_twos_threes_fours_fives_sixes(dice, 4)

      # Assert
      self.assertEqual(result, (4+4))

class TestOnesTwosThreesFoursFivesSixes(unittest.TestCase):
  def test_ones_twos_threes_fours_fives_sixes(self):
    # Arrange
    dice = [2,3,2,5,1]

    # Act
    result = ones_twos_threes_fours_fives_sixes(dice, 2)

    # Assert
    self.assertEqual(result, (2+2))

class TestOnesTwosThreesFoursFivesSixes(unittest.TestCase):
  def test_ones_twos_threes_fours_fives_sixes(self):
    # Arrange
    dice = [3,3,3,4,5]

    # Act
    result = ones_twos_threes_fours_fives_sixes(dice, 2)

    # Assert
    self.assertEqual(result, 0)
