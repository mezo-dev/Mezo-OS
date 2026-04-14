


class ProcessValidator:
    def validate_process_name(name: str): # split these methods into small ones
        if not isinstance(name, str):
            raise ValueError("Process name must be string!")
        
        if len(name) >= 100:
            raise ValueError(
                "Process name must be less then 100 character"
            )
        
        invalid_names = ["", " ",  "@", "$", "!", "%", "^", "&", "*"]
        if name in invalid_names:
            raise NameError(
                f"these characters are not allowed, {invalid_names}"
            )