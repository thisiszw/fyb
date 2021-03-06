class Predictor:
  def __init__(self):
    """
    - `self.batch_size`: to tell the caller the batch_size 
    """
    self.batch_size = 128

  def predict(self, content):
    """
    Args:
    - contents: list of facts (as in string)
    Returns:
    - list of dict, with each dict to be a sentence result:
        {
            'accusation': list of integers (accusation index as in accu.txt)
            'imprisonment': float
            'articles': list fo integers (article index as in article.txt)
        }
    """
    return [
    {
        "accusation": [1],
        "imprisonment": 5,
        "articles": [5]
    } for desc in content]