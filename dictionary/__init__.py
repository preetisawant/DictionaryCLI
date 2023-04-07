__app_name__ = "dictionary"
__version__ = "0.1.0"
__api_key__ = "" #Please enter your Merriam Webster API key here.
(
    API_UNREACHABLE,
    SUCCESS

) = range(2)

ERRORS = {
    API_UNREACHABLE: "API is not reachable",
}