from rest_framework.decorators import api_view
from rest_framework.response import Response
import os

from .helper import Helper

ml_engine_path = os.environ['EVENT_RECOMMANDATION_PATH']

@api_view(['POST'])
def events_api_handler(request):
  Helper.load_storage()
  Helper.store_data('delegate', str(request.data['delegate']))
  Helper.store_data('supplier', str(request.data['supplier']))
  os.system(
    "python " + ml_engine_path + "/main.py"
  )
  response = Helper.get_match_file()
  return Response(response)