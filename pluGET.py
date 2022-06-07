"""
	Handles the main function and the argument passing for the whole pluGET program
"""

import sys
import argparse

# check if folder 'src' is accessible with all modules needed and if not exit
try:
	from src.handlers.handle_config import check_config, validate_config, config_value
	from src.utils.console_output import rename_console_title, clear_console, print_logo
	from src.utils.utilities import rich_print_error, api_test_spiget
	from src.handlers.handle_input import handle_input
except:
	print("Folder 'src' not found in the directory or missing files detected! Please redownload the files from here: https://www.github.com/Neocky/pluGET")
	sys.exit()


if __name__ == "__main__":
	check_config()
	rename_console_title()
	api_test_spiget()
    #check_requirements()
	validate_config()
	parser = argparse.ArgumentParser(description="Just an example",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	#parser.add_argument("-a", "--archive", action="store_true", help="archive mode")
	#parser.add_argument("--exclude", help="files to exclude")
	parser.add_argument("mode", help="Mode (install/update)", nargs='?', default=None)
	parser.add_argument("plugin", help="Plugin Name", nargs='?', default=None)
	args = vars(parser.parse_args())
	if args["mode"] is not None and args["plugin"] is not None:
		print("arguments")

	else:
		print("no arguments")
		clear_console()
		print_logo()
		rich_print_error("test")
		rich_print_error("test2")
		handle_input()
	config = config_value()
	print(config.connection)
	print(config.path_to_plugin_folder)
	print(config.sftp_port)
	print(config.local_seperate_download_path)

