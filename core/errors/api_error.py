class KakaoAPIError(Exception):
    """
    Base class for Errors occured while using Kakao APIs
    """
    def __init__(self, api_type: str, msg: str):
        self.api_type = api_type
        self.msg = msg


class KakaoSynthesizeError(KakaoAPIError):
    """
    Base class for Errors occured while using Kakao Synthesize APIs
    """
    def __init__(self, msg: str, target_xml):
        super(KakaoSynthesizeError, self).__init__(api_type="Synthesize", msg=msg)
        self.target_xml = target_xml


class KakaoRecognizationError(KakaoAPIError):
    """
    Base class for Errors occured while using Kakao Synthesize APIs
    """
    def __init__(self, msg: str, data):
        super(KakaoRecognizationError, self).__init__(api_type="Recognization", msg=msg)
        self.data = data

