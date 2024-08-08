import pathlib
import zipfile


"""First you must create the directory folder in your chosen location before running the function. Whatever name you give this folder, will be fed into
the function and contain the compressed zip containing the files."""


def create_zip(files, dest_direc_folder):  # You must create the directory folder in your chosen location before running the function.
	dest_path = pathlib.Path(dest_direc_folder, "compressed4.zip")  # dest_direc_folder + 'compressed2.zip' name all together into one path name.
	with zipfile.ZipFile(dest_path, 'w') as zf:
		for file in files:
			file = pathlib.Path(file)  # This along with 'arcname' below makes it so only the file name is in the zip and not sub-folders.
			zf.write(file, arcname=file.name)


if __name__ == '__main__':  # To test the function first within the project's directory.
	create_zip(files=["goodie.txt", "blackholes.txt", "members.txt", "redhot.txt"], dest_direc_folder="sam")
# Files to be zipped, destination directory folder name you have chosen.
# If using an absolute path reference, remember to change all "\" to "/".
