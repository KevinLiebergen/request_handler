from request_handler import RequestHandler

if __name__ == '__main__':
    handler = RequestHandler('https://catfact.ninja/fact')
    handler_jsoned = handler.check_json_response()
    if handler_jsoned:
        print(handler_jsoned)
    else:
        print("[-] Exiting...")
        exit(1)
