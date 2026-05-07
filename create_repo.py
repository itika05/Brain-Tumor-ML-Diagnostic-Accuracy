#!/usr/bin/env python3
"""
Script to create a GitHub repository and push the analysis folder to it.
"""

import subprocess
import sys
import os

def run_command(cmd, description):
    """Run a shell command and handle errors."""
    print(f"\n📝 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        print(f"✅ {description} - Done!")
        if result.stdout:
            print(result.stdout)
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during: {description}")
        print(f"Error: {e.stderr}")
        sys.exit(1)

def main():
    repo_name = "Brain-Tumor-ML-Diagnostic-Accuracy"
    repo_description = "Meta-analysis of diagnostic accuracy of machine learning models for brain tumor classification"

    current_dir = os.getcwd()
    print(f"📂 Working directory: {current_dir}")
    print(f"📦 Repository name: {repo_name}")
    print(f"📝 Description: {repo_description}")

    # Step 1: Initialize git repository (if not already initialized)
    print("\n" + "="*60)
    print("STEP 1: Initializing Local Git Repository")
    print("="*60)

    if not os.path.exists(".git"):
        run_command("git init", "Initializing git repository")
        run_command("git config user.email 'user@example.com'", "Setting git email")
        run_command("git config user.name 'GitHub User'", "Setting git name")
    else:
        print("✅ Git repository already initialized")

    # Step 2: Add all files
    print("\n" + "="*60)
    print("STEP 2: Staging Files")
    print("="*60)

    run_command("git add .", "Adding all files to staging")

    # Step 3: Create initial commit
    print("\n" + "="*60)
    print("STEP 3: Creating Initial Commit")
    print("="*60)

    run_command('git commit -m "Initial commit: Brain Tumor ML Diagnostic Accuracy Analysis"', "Creating initial commit")

    # Step 4: Create GitHub repository
    print("\n" + "="*60)
    print("STEP 4: Creating GitHub Repository")
    print("="*60)

    create_repo_cmd = f'gh repo create {repo_name} --public --description "{repo_description}" --source=. --remote origin --push'
    run_command(create_repo_cmd, "Creating GitHub repository")

    # Step 5: Get username for final message
    print("\n" + "="*60)
    print("STEP 5: Retrieving repository information")
    print("="*60)

    username_result = subprocess.run("gh api user -q .login", shell=True, capture_output=True, text=True)
    username = username_result.stdout.strip()

    # Step 6: Display success message
    print("\n" + "="*60)
    print("✨ SUCCESS! Repository created and pushed!")
    print("="*60)
    print(f"\n🎉 Your repository is ready at:")
    print(f"   https://github.com/{username}/{repo_name}")
    print(f"\n💻 To clone locally:")
    print(f"   git clone https://github.com/{username}/{repo_name}.git")

if __name__ == "__main__":
    main()
