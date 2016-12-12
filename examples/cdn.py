# -*- encoding:utf-8 -*-

from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()

    client = s.create_client("cdn", use_ssl=False)

    domains = client.get_cdn_Domains()