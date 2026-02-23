#!/usr/bin/env python3
"""
Complete H1 Title Updater for Remaining 6 CBAM Blog Files
Run this script from the repository root directory
"""

import os
import sys

# Remaining files with their H1 replacements
FILES_TO_UPDATE = {
    "cbam-blog/navigating-cbam-changes.html": {
        "old": "<h1>Navigating CBAM Changes: What Importers and Manufacturers Must Prepare For</h1>",
        "new": "<h1>CBAM 2026: The Regulatory Shifts Every Importer Must Know</h1>"
    },
    "cbam-blog/cbam-six-pains-predictions.html": {
        "old": "<h1>EU CBAM Reality Check: Separating Myths from Facts</h1>",
        "new": "<h1>Six CBAM Myths Debunked: What's Real, What's Hype</h1>"
    },
    "cbam-blog/cbam-developing-countries-impact.html": {
        "old": "<h1>How CBAM Affects Developing Nations: Economic Impact Analysis</h1>",
        "new": "<h1>The Global South vs CBAM: Trade Barriers or Climate Justice?</h1>"
    },
    "cbam-blog/cbam-verification-requirements-2026.html": {
        "old": "<h1>CBAM Verification Requirements 2026: Your Complete Compliance Guide</h1>",
        "new": "<h1>2026 CBAM Verification: Everything You Need to Pass the Audit</h1>"
    },
    "cbam-blog/cbam-impact-steel-industry.html": {
        "old": "<h1>How CBAM is Reshaping the Global Steel Industry</h1>",
        "new": "<h1>Steel Under Pressure: CBAM's Impact on Global Metal Markets</h1>"
    },
    "cbam-blog/cbam-omnibus-new-rules.html": {
        "old": "<h1>CBAM Omnibus: What the New Rules Mean for Importers</h1>",
        "new": "<h1>CBAM Omnibus Explained: Simpler Rules, Same Climate Goals</h1>"
    }
}

def update_file(filepath, old_h1, new_h1):
    """Update H1 in a single file"""
    try:
        if not os.path.exists(filepath):
            print(f"❌ File not found: {filepath}")
            return False
        
        # Read file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if old H1 exists
        if old_h1 not in content:
            print(f"⚠️  Old H1 not found in: {filepath}")
            print(f"   Expected: {old_h1}")
            return False
        
        # Replace H1
        new_content = content.replace(old_h1, new_h1)
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Updated: {filepath}")
        print(f"   Old: {old_h1[:60]}...")
        print(f"   New: {new_h1[:60]}...")
        return True
        
    except Exception as e:
        print(f"❌ Error updating {filepath}: {e}")
        return False

def main():
    print("=" * 70)
    print("CBAM Blog H1 Title Updater - Remaining 6 Files")
    print("=" * 70)
    print()
    
    success_count = 0
    fail_count = 0
    
    for filepath, titles in FILES_TO_UPDATE.items():
        print(f"\nProcessing: {filepath}")
        print("-" * 70)
        if update_file(filepath, titles['old'], titles['new']):
            success_count += 1
        else:
            fail_count += 1
    
    # Summary
    print()
    print("=" * 70)
    print(f"✅ Successfully updated: {success_count}/{len(FILES_TO_UPDATE)} files")
    if fail_count > 0:
        print(f"❌ Failed: {fail_count}/{len(FILES_TO_UPDATE)} files")
    print("=" * 70)
    
    if success_count > 0:
        print("\n📝 Next steps:")
        print("   1. Review changes: git diff")
        print("   2. Commit: git add . && git commit -m 'Update H1 titles for remaining CBAM blog articles'")
        print("   3. Push: git push origin main")
        print()
        return 0
    else:
        print("\n⚠️  No files were updated. Please check the error messages above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
