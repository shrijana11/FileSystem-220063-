import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

class FileSystemExplorer:
    def __init__(self, root):
        self.root = root
        self.root.title("File System Explorer")

        self.root.geometry("300x190")

        self.browse_button = tk.Button(self.root, text="Browse Directory", command=self.browse_directory)
        self.browse_button.pack()

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.files_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Contents", menu=self.files_menu)
        self.files_menu.add_command(label="New File", command=self.file_creation)
        self.files_menu.add_command(label="New Folder", command=self.directory_creation)
        self.files_menu.add_command(label="Erase File", command=self.delete_file)
        self.files_menu.add_command(label="Erase Folder", command=self.delete_directory)

        self.edit_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Edits", menu=self.edit_menu)
        self.edit_menu.add_command(label="Log File", command=self.write_file)
        self.edit_menu.add_command(label="View File", command=self.read_file)
        self.edit_menu.add_command(label="Addmore Data", command=self.append_to_file)
        self.edit_menu.add_command(label="File Rewrite", command=self.rewrite_file)

        self.lists_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Database", menu=self.lists_menu)
        self.lists_menu.add_command(label="Record of Files", command=self.list_files)
        self.lists_menu.add_command(label="Record of Folders", command=self.list_directories)

        self.menu.add_command(label="Exit", command=self.root.quit)

    def message(self, action):
        messagebox.showinfo("Success", f"Successfully {action}.Hoorrayyyy!!!!!")

    def browse_directory(self):
        chosen_path = filedialog.askdirectory(title="Select Directory")
        if chosen_path:
            self.current_path = chosen_path

    def file_creation(self):
        if hasattr(self, 'current_path'):
            file_name = filedialog.asksaveasfilename(title="Create File", initialdir=self.current_path)
            if file_name:
                try:
                    with open(file_name, "w") as file:
                        file.write("")
                    self.message("created a file")
                except Exception as e:
                    messagebox.showerror("Error", f"Error creating file: {str(e)}")

    def directory_creation(self):
        if hasattr(self, 'current_path'):
            dir_name = simpledialog.askstring("Create Directory", "Enter directory name:")
            if dir_name:
                new_dir_path = os.path.join(self.current_path, dir_name)
                try:
                    os.makedirs(new_dir_path)
                    self.message("created a folder")
                except Exception as e:
                    messagebox.showerror("Error", f"Error creating directory: {str(e)}")

    def delete_file(self):
        if hasattr(self, 'current_path'):
            file_name = filedialog.askopenfilename(title="Delete File", initialdir=self.current_path)
            if file_name:
                try:
                    os.remove(file_name)
                    self.message("deleted a file")
                except Exception as e:
                    messagebox.showerror("Error", f"Error deleting file: {str(e)}")

    def delete_directory(self):
        if hasattr(self, 'current_path'):
            dir_name = filedialog.askdirectory(title="Delete Directory", initialdir=self.current_path)
            if dir_name:
                try:
                    os.rmdir(dir_name)
                    self.message("deleted a folder")
                except Exception as e:
                    messagebox.showerror("Error", f"Error deleting directory: {str(e)}")

    def write_file(self):
        if hasattr(self, 'current_path'):
            file_name = filedialog.askopenfilename(title="Write File", initialdir=self.current_path)
            if file_name:
                new_content = simpledialog.askstring("Write File", f"Enter content for '{file_name}':")
                if new_content is not None:
                    try:
                        with open(file_name, "w") as file:
                            file.write(new_content)
                        self.message("written to a file")
                    except Exception as e:
                        messagebox.showerror("Error", f"Error writing to file: {str(e)}")

    def read_file(self):
        if hasattr(self, 'current_path'):
            file_name = filedialog.askopenfilename(title="Read File", initialdir=self.current_path)
            if file_name:
                try:
                    with open(file_name, "r") as file:
                        content = file.read()
                        messagebox.showinfo("File Content", f"Content of '{file_name}':\n{content}")
                    self.message("read a file")
                except Exception as e:
                    messagebox.showerror("Error", f"Error reading file: {str(e)}")

    def append_to_file(self):
        if hasattr(self, 'current_path'):
            file_name = filedialog.askopenfilename(title="Append to File", initialdir=self.current_path)
            if file_name:
                append_content = simpledialog.askstring("Append to File", f"Enter content to append to '{file_name}':")
                if append_content is not None:
                    try:
                        with open(file_name, "a") as file:
                            file.write("\n" + append_content)
                        self.message("appended to a file")
                    except Exception as e:
                        messagebox.showerror("Error", f"Error appending to file: {str(e)}")

    def rewrite_file(self):
        if hasattr(self, 'current_path'):
            file_name = filedialog.askopenfilename(title="Rewrite File", initialdir=self.current_path)
            if file_name:
                new_content = simpledialog.askstring("Rewrite File", f"Enter new content for '{file_name}':")
                if new_content is not None:
                    try:
                        with open(file_name, "w") as file:
                            file.write(new_content)
                        self.message("rewritten a file")
                    except Exception as e:
                        messagebox.showerror("Error", f"Error rewriting file: {str(e)}")
    def list_files(self):
        if hasattr(self, 'current_path'):
            try:
                file_list = [file for file in os.listdir(self.current_path) if os.path.isfile(os.path.join(self.current_path, file))]
                file_list_str = "\n".join(file_list)
                if file_list_str:
                    messagebox.showinfo("File List", f"List of Files in '{self.current_path}':\n{file_list_str}")
                    self.message("listed files")
                else:
                    messagebox.showinfo("File List", f"No files found in '{self.current_path}'.")
            except Exception as e:
                messagebox.showerror("Error", f"Error listing files: {str(e)}")

    def list_directories(self):
        if hasattr(self, 'current_path'):
            try:
                dir_list = [dir for dir in os.listdir(self.current_path) if os.path.isdir(os.path.join(self.current_path, dir))]
                dir_list_str = "\n".join(dir_list)
                if dir_list_str:
                    messagebox.showinfo("Directory List", f"List of Directories in '{self.current_path}':\n{dir_list_str}")
                    self.message("listed directories")
                else:
                    messagebox.showinfo("Directory List", f"No directories found in '{self.current_path}'.")
            except Exception as e:
                messagebox.showerror("Error", f"Error listing directories: {str(e)}")
    def set_file_permissions(self, path):
        if hasattr(self, 'current_path'):
            try:
                permission_input = simpledialog.askstring("Set File Permissions", "Enter file permissions (e.g., 'rw-r--r--'):")
                if permission_input:
                    os.chmod(path, int(permission_input, 8))
                    self.message("set file permissions")
            except Exception as e:
                messagebox.showerror("Error", f"Error setting file permissions: {str(e)}")

    def manage_directory(self):
        if hasattr(self, 'current_path'):
            try:
                dir_name = filedialog.askdirectory(title="Manage Directory", initialdir=self.current_path)
                if dir_name:
                    new_name = simpledialog.askstring("Manage Directory", f"Enter new name for '{dir_name}':")
                    if new_name:
                        new_path = os.path.join(self.current_path, new_name)
                        os.rename(dir_name, new_path)
                        self.message("renamed directory")
            except Exception as e:
                messagebox.showerror("Error", f"Error managing directory: {str(e)}")

    def handle_errors(self, action, e):
        messagebox.showerror("Error", f"Error {action}: {str(e)}")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = FileSystemExplorer(root)
    root.mainloop()
