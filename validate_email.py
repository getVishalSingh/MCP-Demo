import re


EMAIL_PATTERN = re.compile(
    r"^[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*@"
    r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?"
    r"(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)+$"
)


def is_valid_email(email: str) -> bool:
    """Return whether an email address has a conventional email format."""
    if len(email) > 254 or len(email) == 0:
        return False

    local_part, separator, domain = email.partition("@")
    if not separator or len(local_part) > 64:
        return False

    return EMAIL_PATTERN.fullmatch(email) is not None


if __name__ == "__main__":
    address = input("Email address: ").strip()
    if is_valid_email(address):
        print("Valid email address")
    else:
        print("Invalid email address")
