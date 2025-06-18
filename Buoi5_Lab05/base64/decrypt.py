import base64

def main():
    try:
        with open("data.txt","r") as file:
            encoded_string = file.read().strip()
            
        dencoded_bytes = base64.b64decode(encoded_string)
        dencoded_string = dencoded_bytes.decode("utf-8")
    
        print("Chuỗi sau khi giải mã:",dencoded_string)
    except Exception as e:
        print("Lỗi:",e)
        
if __name__=="__main__":
    main()
            