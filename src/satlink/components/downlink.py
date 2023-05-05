import json
from typing import Dict, List, Tuple
from wsgiref.types import StartResponse


class Downlink:
  def __init__(self, start_response: StartResponse):
    self.__start_response = start_response
    self.__body = ''
    self.__status = '200 OK'
    self.__headers: List[Tuple[str, str]] = []
    self.__encoding = 'utf-8'

  def __iter__(self):
    for b in self.__body:
      yield b.encode()

  def header(self, name: str, value: str):
    self.__headers = [h for h in self.__headers if name != h[0]]
    self.__headers.append((name, value))

    return self

  def status(self, code: int):
    self.__status = f'{code} '
    return self

  def text(self, message: str):
    self.header('Content-Type', 'text/plain')
    self.__start_response(self.__status, self.__headers)
    self.__body = message

    return self

  def json(self, data: Dict):
    self.header('Content-Type', 'application/json')
    self.__start_response(self.__status, self.__headers)
    self.__body = json.dumps(data)

    return self
  
  def html(self, data: Dict):
    self.header('Content-Type', 'text/html')
    self.__start_response(self.__status, self.__headers)
    self.__body = json.dumps(data)

    return self
