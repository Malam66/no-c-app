import zipfile
import os
import shutil

def create_download_package():
    """Create a ZIP file with all necessary application files"""
    
    # Files to include in the download package
    files_to_include = [
        'improved_no_recoil_app.py',
        'no_recoil_app.py',
        'advanced_no_recoil.py',
        'launcher.py',
        'setup.py',
        'requirements.txt',
        'run_improved_app.bat',
        'run_launcher.bat',
        'run_no_recoil.bat',
        'config_1.json',
        'README.md'
    ]
    
    # Create the ZIP file
    zip_filename = 'Strong_No_Recoil_App.zip'
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in files_to_include:
            if os.path.exists(file):
                zipf.write(file)
                print(f"Added {file} to package")
            else:
                print(f"Warning: {file} not found")
    
    print(f"\n✅ Download package created: {zip_filename}")
    print(f"📦 Package size: {os.path.getsize(zip_filename) / 1024:.1f} KB")
    
    return zip_filename

if __name__ == "__main__":
    create_download_package() 