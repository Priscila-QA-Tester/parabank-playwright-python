# Git Push Guide: From Local to GitHub

This guide explains the step-by-step process of taking a local project on your computer and pushing it to a new repository on GitHub.

## Step-by-Step Instructions

Execute these commands one by one in your VS Code terminal (`Terminal > New Terminal`). Make sure you are inside your project folder (e.g., `C:\Users\prisc\projects\parabank-playwright-python`).

### 1. Initialize Git in your local folder
```powershell
git init
```
* **What it does:** This tells Git to start tracking changes in the current folder. It creates a hidden `.git` folder. You only need to run this once per project.

### 2. Add all files to the staging area
```powershell
git add .
```
* **What it does:** The `.` means "everything". This tells Git to prepare all the files and folders in your project to be saved in the next commit.

### 3. Save the changes locally (Commit)
```powershell
git commit -m "first commit"
```
* **What it does:** This takes a "snapshot" of all the files you added in the previous step and saves them in your local Git history. The `-m` stands for message, and "first commit" is the description of what you are saving.

### 4. Connect your local folder to GitHub
```powershell
git remote add origin https://github.com/Priscila-QA-Tester/parabank-playwright-python.git
```
* **What it does:** This tells your local Git that there is a remote server (GitHub) called "origin" at that specific URL where you want to send your code.

### 5. Rename the default branch to 'main'
```powershell
git branch -M main
```
* **What it does:** Historically, Git used 'master' as the default branch name. GitHub now uses 'main'. This command renames your local default branch to 'main' to match GitHub.

### 6. Push the code to GitHub
```powershell
git push -u origin main
```
* **What it does:** This sends (pushes) all your committed code to the "main" branch on the "origin" server (GitHub). The `-u` links your local 'main' branch to the remote 'main' branch, so in the future, you can just type `git push`.

---

## What to do next time you make changes?

After you've done the setup above, the next time you change a file or add a new test, you only need to run three commands:

1. `git add .` (Add the changes)
2. `git commit -m "Describe what you changed here"` (Save the changes)
3. `git push` (Send to GitHub)
