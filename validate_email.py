import re

MAX_EMAIL_LENGTH = 254
MAX_LOCAL_PART_LENGTH = 64

EMAIL_PATTERN = re.compile(
    r"^(?=.{1,254}$)"
    r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*@"
    r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?"
    r"(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)+$",
    re.ASCII,
)


def is_valid_email(email: str) -> bool:
    """Return whether an email address is in a conventional format."""
    if not isinstance(email, str):
        return False

    email = email.strip()
    if not email or len(email) > MAX_EMAIL_LENGTH:
        return False

    if email.count("@") != 1:
        return False

    local_part, domain = email.split("@")
    if len(local_part) > MAX_LOCAL_PART_LENGTH or not domain:
        return False

    return EMAIL_PATTERN.fullmatch(email) is not None


if __name__ == "__main__":
    address = input("Email address: ").strip()
    if is_valid_email(address):
        print("Valid email address")
    else:
        print("Invalid email address")
