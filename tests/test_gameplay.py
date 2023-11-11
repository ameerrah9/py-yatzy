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

def pair(lst):
  # the range is 6, 0, -1 because we want to start at 6 and go down to 1
  # we start at 6 because we want to find the highest pair
  # ex: start at 6, then 5, then 4, etc. until we reach 1
  # 0 is excluded, so we stop at 1
  for i in range(6, 0, -1):
    # if the count of the number is greater than or equal to 2, then we have a pair
    # once we find a pair, we return the pair * 2
    # we start at 6 so we find the highest pair first
    if lst.count(i) >= 2:
      return i * 2
  # if we don't find a pair, we return 0
  return 0

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

class TestPair(unittest.TestCase):
  def test_pair(self):
    # Arrange
    dice = [3,3,3,4,4]

    # Act
    result = pair(dice)

    # Assert
    self.assertEqual(result, (4+4))

class TestPair2(unittest.TestCase):
  def test_pair(self):
    # Arrange
    dice = [1,1,6,2,6]

    # Act
    result = pair(dice)

    # Assert
    self.assertEqual(result, (6+6))

class TestPair3(unittest.TestCase):
  def test_pair(self):
    # Arrange
    dice = [1,2,3,4,5]

    # Act
    result = pair(dice)

    # Assert
    self.assertEqual(result, 0)