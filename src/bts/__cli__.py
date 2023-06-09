"""Command line interface for bts"""

# Importing the libraries

from . import __version__


def main() -> None:
    """This is the cli function of the package"""
    print("This is the cli function of the package")
    print(f"The version of the package is: {__version__}")


if __name__ == "__main__":
    main()
