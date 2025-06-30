#  _______________
#  Import LIBRARIES
import requests as rq
from requests import exceptions

#  Import FILES
#  _______________


"""Requests code."""


def make_get_request(url: str) -> rq.Response | dict[str, str]:
    try:
        response: rq.Response = rq.get(url=url)
    except exceptions.RequestException:
        return {"Error": "oh no!"}
    else:
        return response.json()["headers"]


works: rq.Response | dict[str, str] = make_get_request(url="https://httpbin.org/get")
print(works, "\n\n")
fails: rq.Response | dict[str, str] = make_get_request(url="https://notasite.abc")
print(fails)


# if __name__ == "__main__":
#     main()


#  _______________
#  Import LIBRARIES
#  Import FILES
#  _______________
