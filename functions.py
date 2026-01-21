# change the request string to dictionary
def req_to_dict(request_string):
    """
    Parses a raw HTTP request string into a dictionary.
    Cookies are parsed into individual key-value pairs within the dictionary.
    """
    headers_dict = {}
    
    # Split the string into lines and filter out empty ones
    lines = [line.strip() for line in request_string.strip().split('\n') if line.strip()]
    
    for line in lines:
        # Skip the Request Line (e.g., GET /path HTTP/1.1)
        if line.startswith(("GET ", "POST ", "PUT ", "DELETE ", "HEAD ", "OPTIONS ", "PATCH ")):
            continue
            
        # Ensure the line contains a header separator
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            
            # Special handling to explode 'Cookie' header into individual keys
            if key == "Cookie":
                cookies = value.split(";")
                for cookie in cookies:
                    if "=" in cookie:
                        cookie_name, cookie_val = cookie.split("=", 1)
                        headers_dict[cookie_name.strip()] = cookie_val.strip()
            else:
                # Add standard headers (e.g., User-Agent)
                headers_dict[key] = value
                
    return headers_dict


####################################


# Extract the path from the post's get request
def get_path_from_req(req_string):
    path = req_string.split(" ")[1].split(" ")[0]
    return path


####################################


# Extract the image name from the image's get request
def get_image_name(req_string):
    image_name = req_string.split("_")[1].split("_")[0]
    return image_name