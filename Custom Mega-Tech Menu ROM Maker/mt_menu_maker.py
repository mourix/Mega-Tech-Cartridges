"""Mega-Tech Menu ROM Generator

Generates a custom Sega Mega-Tech menu ROM based on config.ini.
It uses epr-12368-22.ic3 from your legally dumped mt_tetri.zip.

Jos van Mourik, 2024
"""


import configparser


def read_ini_file(file_path):
    config = configparser.ConfigParser()
    config.read(file_path) 
    print(file_path)
    return config


def copy_file(source_file, output_file):
    # Open the source file in binary read mode
    with open(source_file, 'rb') as src:
        # Read the content of the source file
        content = src.read()
    
    # Write the modified content to the output file
    with open(output_file, 'wb') as out:
        out.write(content)
    print(source_file)


def edit_file(file, data, address):
    # Open the source file in binary read mode
    with open(file, 'rb') as src:
        # Read the content of the source file
        content = src.read()
    
    # Hex editing: insert the data
    content = content[:address] + data + content[address + len(data):]
    
    # Write the modified content to the output file
    with open(file, 'wb') as out:
        out.write(content)


def create_game_name(file, name):
    # Verify input
    if len(name) < 1 or len(name) > 24:
        print("Error: Game name must be 1-24 characters.")
        return
    
    name = name.upper().ljust(24)
    edit_file(file, name.encode('utf-8'), 0x10)
    print(name)


def create_page_1_header(file, header):
    # Verify input
    if len(header) < 1 or len(header) > 14:
        print("Error: Header 1 must be 1-14 characters.")
        return
    
    header = header.upper().ljust(14)
    
    # Transform header to hex code
    header_hex = bytearray()
    for char in header:
        if char == ' ':
            char_hex = 0x20
        else:
            char_hex = ord('A') + 15 + (4 * (ord(char) - ord('A')) )
        header_hex.append(char_hex)
    
    # Create the header hex pattern
    header_pattern = bytearray()
    for char in header_hex:
        if char == 0x20:
            header_pattern.append(0x20)
        else:
            header_pattern.append(0xf6)
        header_pattern.append(char)
    edit_file(file, header_pattern, 0xDB)
    
    # Create the header visibility hex pattern
    header_v_pattern = bytearray()
    for char in header_pattern:
        if char == 0x20:
            header_v_pattern.append(0x20)
        else:
            header_v_pattern.append(0x00)
            
    edit_file(file, header_v_pattern, 0xF7)
    print(header)


def create_page_1_text(file, lines):
    # Filter lines to include only those that start with '|'
    lines = [line for line in lines if line.startswith('|')]
    
    # Ensure there are 7 lines
    while len(lines) < 7:
        lines.append("|" + " " * 28)  # Add a line of 28 spaces
    
    for i, line in enumerate(lines[:7]): # Process only the first 7 lines
        line = line[1:29] # Remove the start character (always '|')
        line = line.upper().ljust(28) # Pad and uppercase
        edit_file(file, line.encode('utf-8'), 0x19F + (i * 28 * 2))
        print(line)


def create_page_2_header(file, header):
    # Verify input
    if len(header) < 1 or len(header) > 18:
        print("Error: Header 2 must be 1-18 characters.")
        return
    
    header = header.upper().ljust(18)
    edit_file(file, header.encode('utf-8') , 0x584)
    edit_file(file, "                ".encode('utf-8') , 0x5a2)
    print(header)


def create_page_2_text(file, lines):
    # Filter lines to include only those that start with '|'
    lines = [line for line in lines if line.startswith('|')]
    
    # Ensure there are 16 lines
    while len(lines) < 16:
        lines.append("|" + " " * 28)  # Add a line of 28 spaces
    
    for i, line in enumerate(lines[:16]): # Process only the first 16 lines
        line = line[1:29] # Remove the start character (always '|')
        line = line.upper().ljust(28) # Pad and uppercase
        edit_file(file, line.encode('utf-8'), 0x5CF + (i * 28))
        print(line)


def main():
    print("MEGA-TECH MENU ROM MAKER")
    
    source_file = "epr-12368-22.ic3" # Original mt_tetri epr-12368-22.ic3
    output_file = "menu.bin" # Output menu ROM
    
    print("\nREADING CONFIG:")
    config = read_ini_file("config.ini") # Config file with text data
    game_name = config.get("Menu", "game_name", fallback="")
    page_1_header = config.get("page_1", "page_1_header", fallback="")
    page_1_text = config.get("page_1", "Page_1_text", fallback="").splitlines()
    page_2_header = config.get("page_2", "page_2_header", fallback="")
    page_2_text = config.get("page_2", "Page_2_text", fallback="").splitlines()
    
    print("\nCOPYING FILE FOR EDIT:")
    copy_file(source_file, output_file)
    
    print("\nGAME NAME:")
    create_game_name(output_file, game_name)
    
    print("\nPAGE 1 HEADER:")
    create_page_1_header(output_file, page_1_header)
    
    print("\nPAGE 1 TEXT:")
    create_page_1_text(output_file, page_1_text)
    
    print("\nPAGE 2 HEADER:")
    create_page_2_header(output_file, page_2_header)
    
    print("\nPAGE 2 TEXT:")
    create_page_2_text(output_file, page_2_text)
    
    print("\nSCRIPT DONE. OUTPUT: " + output_file)
    
    
if __name__ == "__main__":
    main()
