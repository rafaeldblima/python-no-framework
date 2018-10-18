from settings.settings import ALLOWED_HOSTS


def split_domain(allowed_hosts):
    for host in allowed_hosts:
        if host == "*":
            return "0.0.0.0"
        return host


def get_host():
    allowed_hosts = ALLOWED_HOSTS
    if not allowed_hosts:
        allowed_hosts = ['localhost', '127.0.0.1', '[::1]']

    domain = split_domain(allowed_hosts)

    return domain

