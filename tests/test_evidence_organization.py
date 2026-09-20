from pathlib import Path
from  playwright.sync_api import sync_playwright
def test_evidence_organization():
    screenshot_dir = Path("artifactsscreenshots")
    screenshot_dir.mkdir(parents=True,exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/")
        assert "The Internet" in page.title()
        page.screenshot(path=str(screenshot_dir/"home+page.png"),full_page=True)
        browser.close()
