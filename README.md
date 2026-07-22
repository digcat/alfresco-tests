# Alfresco Test Suite

**Python 3.10+ Selenium Test Automation for Alfresco**

Modern, secure test automation framework for Alfresco Content Services using Selenium WebDriver and the Page Object Model pattern.

## Version 2.0.0 - Major Refactoring

This version includes **critical security fixes**, Python 3.10+ migration, Selenium 4 compatibility, and comprehensive code quality improvements. See [CHANGELOG.md](CHANGELOG.md) for complete details.

---

## Requirements

- **Python**: 3.8+ (3.10+ recommended)
- **Alfresco**: Compatible with Alfresco Community/Enterprise 5.x-23.x
- **Browser**: Firefox or Chrome with WebDriver
- **OS**: Linux (Ubuntu/Debian or CentOS/RHEL)

---

## Quick Start

### 1. Installation

```bash
# Clone repository
git clone <repository-url>
cd alfresco-tests

# Run installation script
./install.sh
```

The `install.sh` script will:
- Verify Python 3.8+ is installed
- Install system dependencies (Firefox, Xvfb)
- Create Python virtual environment
- Install all required packages from `requirements.txt`

### 2. Configuration

**Option A: Environment Variables (Recommended for Production)**

```bash
export ALFRESCO_USER=admin
export ALFRESCO_PASSWORD=your_password
```

**Option B: Configuration File (Development Only)**

```bash
# Copy example config
cp config.yml.example config.yml

# Edit config.yml with your settings
nano config.yml
```

**Option C: .env File**

```bash
# Copy example file
cp .env.example .env

# Edit .env with your credentials
nano .env
```

**Important**: Never commit `config.yml` or `.env` files to version control!

### 3. Run Tests

```bash
# Activate virtual environment
source testing_virt/venv/bin/activate

# Set credentials
export ALFRESCO_USER=admin
export ALFRESCO_PASSWORD=your_password

# Run all tests using runtests.sh
./runtests.sh ./testing_virt/venv/bin

# Or run specific test suites
python test_share.py
python test_rm.py
python test_cmis.py
```

---

## Configuration Options

Edit `config.yml` to customize test behavior:

```yaml
# Alfresco Connection
sharehost: dev.daren.net
shareport: 443
https: true  # Use HTTPS (recommended)

# Browser Settings
browser: firefox  # Options: firefox, chrome

# Authentication (use environment variables instead!)
# user: admin
# passwd: admin

# Screenshot Settings
photopath: images  # Set to '' to disable screenshots

# Test URLs
loginurl: /share/page
```

**Security Note**: Do NOT store credentials in `config.yml` for production environments. Use environment variables instead.

---

## Test Suites

### Share UI Tests (`test_share.py`)
11 tests covering core Alfresco Share functionality:
- Login authentication
- People finder
- My tasks
- Repository browser
- My files / Shared files
- Site dashboard and document library
- Site member lists
- Search functionality
- Site creation

### Records Management Tests (`test_rm.py`)
14 tests for Alfresco Records Management:
- RM site navigation
- File plan access
- Records creation and management
- RM-specific workflows

### CMIS Tests (`test_cmis.py`)
Content Management Interoperability Services (CMIS) API tests:
- Repository connection
- Document queries
- CMIS property validation

### JavaScript Console Tests (`test_jsconsole.py`)
Tests for JavaScript Console addon:
- Admin console access
- Script execution

### Service Tests (`test_services.py`)
FTP and CMIS service connectivity tests

### Preview Tests (`test_preview.py`, `test_uploadandpreview.py`)
Document preview and upload functionality tests

---

## Architecture

### Page Object Model

The test suite follows the **Page Object Model** (POM) pattern for maintainability:

```
test_*.py          → Test cases (what to test)
    ↓
page*.py           → Page Objects (how to interact with pages)
    ↓
element.py         → Base elements (reusable components)
    ↓
locators.py        → Element locators (XPath, CSS, IDs)
```

**Key Files**:
- `page.py` - Main Alfresco Share page objects
- `page_rm.py` - Records Management page objects
- `page_jsconsole.py` - JavaScript Console page objects
- `element.py` - Base page element class
- `locators.py` - Centralized locator definitions
- `testconfig.py` - Configuration management (TestConfig singleton)

### Screenshot Capture

Tests automatically capture screenshots for visual verification:
- Stored in `photopath` directory (default: `./images/`)
- Named after calling test function
- Automatic unique filename generation (appends numbers if file exists)
- Disable by setting `photopath: ''` in config.yml

Example: Test `test_alfresco_login` generates `test_alfresco_login.png`

---

## Advanced Usage

### Running Specific Tests

```bash
# Single test file
python test_share.py

# Specific test method
python test_share.py TestMyAlfresco.test_alfresco_login

# With unittest verbose mode
python test_share.py -v
```

### Headless Execution

Tests run headless by default via `runtests.sh` using Xvfb:

```bash
./runtests.sh ./testing_virt/venv/bin
```

### Visible Browser Mode

For debugging, run tests directly without runtests.sh:

```bash
source testing_virt/venv/bin/activate
export ALFRESCO_USER=admin ALFRESCO_PASSWORD=pass
python test_share.py
```

### Content Generation

Create bulk test content using `makecontent.py`:

```bash
python makecontent.py <sitename> <filename> <count>
```

Example:
```bash
# Create 100 test documents in 'testsite'
python makecontent.py testsite testdoc 100
```

### Load Testing

Run parallel content creation for load testing:

```bash
python runload.py <sitename> <basename> <count>
```

This spawns multiple `makecontent.py` processes in parallel.

---

## Security Features (v2.0.0)

### Critical Fixes Implemented

1. **Credentials Management**
   - Removed all hardcoded credentials
   - Environment variable support (`ALFRESCO_USER`, `ALFRESCO_PASSWORD`)
   - Secure credential loading with validation

2. **Command Injection Prevention**
   - Fixed `subprocess.call()` usage in `runload.py`
   - Changed from `shell=True` to secure list arguments

3. **SQL Injection Prevention**
   - Proper escaping for CMIS queries in `makecontent.py`
   - Prevents injection via filename manipulation

4. **Secure Protocols**
   - HTTPS support added to `fast_selenium.py`
   - Default to secure connections
   - Security warnings for plain FTP usage

5. **Dependency Security**
   - All packages updated to latest secure versions
   - Fixes for multiple CVEs in Selenium, PyYAML, Pillow, requests

See [CHANGELOG.md](CHANGELOG.md) for complete security fix details.

---

## Troubleshooting

### Python Version Issues

```bash
# Check Python version
python3 --version  # Must be 3.8+

# If python3 is not default
python3 -m venv testing_virt/venv
source testing_virt/venv/bin/activate
```

### Credential Errors

```
ValueError: Credentials must be set via ALFRESCO_USER and ALFRESCO_PASSWORD
```

**Solution**: Set environment variables before running tests:
```bash
export ALFRESCO_USER=admin
export ALFRESCO_PASSWORD=your_password
```

### Selenium WebDriver Issues

```
selenium.common.exceptions.WebDriverException: 'geckodriver' not found
```

**Solution**: Install WebDriver for your browser:
```bash
# Firefox
sudo apt-get install firefox-geckodriver

# Chrome
sudo apt-get install chromium-chromedriver
```

### Connection Refused Errors

```
ConnectionRefusedError: [Errno 111] Connection refused
```

**Solution**: Verify Alfresco is running and accessible:
```bash
curl https://dev.daren.net:443/share/page
```

Check `sharehost` and `shareport` in `config.yml`.

### Screenshots Not Generated

Verify `photopath` is set in config.yml:
```yaml
photopath: images  # Must not be empty string
```

Ensure directory is writable:
```bash
mkdir -p images
chmod 755 images
```

---

## Development

### Adding New Tests

1. **Create test file**: `test_myfeature.py`
2. **Import dependencies**:
```python
import unittest
from selenium import webdriver
import page
import testconfig
```

3. **Create test class**:
```python
class TestMyFeature(unittest.TestCase):
    def setUp(self):
        self.config = testconfig.TestConfig.get_instance()
        self.driver = testconfig.setBrowser(self.config)
        self.driver.get(self.config.loginurl)

    def test_my_feature(self):
        main_page = page.MainPage(self.driver)
        main_page.click_login_button()
        # Your test logic here
        assert main_page.is_title_matches("Expected Title"), "Test failed"

    def tearDown(self):
        self.driver.close()
```

4. **Add to runtests.sh**:
```bash
TESTS=${2:-"cmis share rm myfeature"}
```

### Adding New Page Objects

1. **Edit page.py or create new page_*.py file**
2. **Add method to page class**:
```python
def click_my_element(self):
    vars = testconfig.getVars(self)
    element = self.driver.find_element(By.ID, 'myElementId')
    element.click()
```

3. **Add locator to locators.py** (if using MainPageLocators):
```python
class MainPageLocators(object):
    MY_ELEMENT = (By.ID, 'myElementId')
```

### Code Quality

Run static analysis:
```bash
pip install black isort pylint flake8

# Format code
black .
isort .

# Lint
pylint testconfig.py page.py
flake8 . --exclude=venv
```

---

## Migration from v1.0.0

If upgrading from the legacy Python 2.7 version:

1. **Update Python**: Install Python 3.8+
2. **Set Environment Variables**:
   ```bash
   export ALFRESCO_USER=admin
   export ALFRESCO_PASSWORD=your_password
   ```
3. **Reinstall**:
   ```bash
   rm -rf testing_virt
   ./install.sh
   ```
4. **Update Test Execution**:
   ```bash
   # Old (Python 2.7):
   python test_share.py

   # New (Python 3):
   python3 test_share.py
   # or
   source testing_virt/venv/bin/activate
   python test_share.py
   ```

See [CHANGELOG.md](CHANGELOG.md) Section "Migration Guide" for complete details.

---

## Test Coverage Summary

| Test Suite | Tests | Coverage |
|------------|-------|----------|
| Share UI | 11 | Core Share functionality, navigation, search |
| Records Management | 14 | RM site, file plans, records lifecycle |
| CMIS | 2 | CMIS API, repository queries |
| JavaScript Console | 2 | Admin console, script execution |
| Services | 1 | FTP/CMIS connectivity |
| Previews | 3 | Document preview, upload, rendering |

**Total**: 33 tests covering major Alfresco functionality

---

## Contributing

When contributing:
1. **Never commit credentials** - Use environment variables
2. **Follow PEP 8** - Python style guide
3. **Add docstrings** - Document new methods
4. **Handle exceptions** - Use specific exception types
5. **Test thoroughly** - Verify changes don't break existing tests
6. **Update docs** - Keep README.md and CHANGELOG.md current

---

## License

See LICENSE file for details.

---

## Support

- **Issues**: Report bugs via GitHub Issues
- **Documentation**: See [CHANGELOG.md](CHANGELOG.md) for version history
- **Alfresco Docs**: https://docs.alfresco.com

---

## Acknowledgments

- **Original Author**: DigCat.com
- **v2.0.0 Refactoring**: Comprehensive security and modernization update (2026-07-22)

This test suite addresses years of technical debt and brings Alfresco testing up to modern standards for security, reliability, and maintainability.
