from expects import equal, expect
from mamba import describe, it

from src.handlers.hello.app import say_hello

STATUS_OK = 200


with describe(say_hello):
    with it('is ok'):
        response = say_hello(event={})

        expect(response['statusCode']).to(equal(STATUS_OK))
