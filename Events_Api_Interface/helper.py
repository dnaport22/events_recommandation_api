import os

class Helper():

  @staticmethod
  def load_storage():
    os.system("mkdir /tmp/events_ml_engine")

  @classmethod
  def store_data(cls, instance, data):
    fl = open("/tmp/events_ml_engine/"+instance+".json", 'w')
    fl.write(data)
    fl.close()

  @staticmethod
  def get_match_file():
    with open("/tmp/events_ml_engine/match.json", "r") as fl:
      return fl.read()