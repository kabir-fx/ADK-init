from google.genai import types

"""
When working with LLMs, you may encounter transient errors like rate limits or temporary service unavailability. Retry options automatically handle these failures by retrying the request with exponential backoff.
"""
retry_config = types.HttpRetryOptions(
    # Maximum number of attempts, including the original request.
    attempts=5,

    # Multiplier by which the delay increases after each attempt
    exp_base=7,

    # Initial delay before the first retry (in seconds)
    initial_delay=1,

    # List of HTTP status codes that should trigger a retry 
    http_status_codes=[429, 500, 503, 504]
)