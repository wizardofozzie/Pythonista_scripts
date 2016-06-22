##Fetch password from keychain with touchid authentication

import keychain, sys
try:
    from touchid import authenticate
except ImportError:
    Exception("Couldn't load touchid module")


def get_apikey(service="", account=""):
    assert service is not None and account is not None
    d = {}
    d.update(keychain.get_services())
    if service in d:
        assert d.get(service, "") == account
        PWD = keychain.get_password(service, account)
        touchid_status = 0
        touchid_status = authenticate("Authenticate API lookup", allow_passcode=True, timeout=10)
        if touchid_status:
            return PWD
        else:
            sys.stderr.write("Bad fingerprint!")
    else:
        raise Exception("API key not found")
