#!/bin/bash
#
# Alfresco Test Suite Installation Script
# Updated for Python 3.10+ and modern dependencies
#

set -e  # Exit on error

cd "`dirname $0`"
ROOT=`pwd`

echo "============================"
echo "Alfresco Test Suite Installer"
echo "============================"
echo ""

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "Detected Python version: $PYTHON_VERSION"

if ! python3 -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)"; then
    echo "ERROR: Python 3.8 or higher is required"
    echo "Current version: $PYTHON_VERSION"
    exit 1
fi

# Check for config
if [ -e config.yml ] ; then
	echo "✓ Found local config.yml"
else
	echo "WARNING: config.yml not found. Copy config.yml.example to config.yml and configure it."
fi

# Clean old virtual environment
if [ -e testing_virt ] ; then
	echo "Cleaning old virtual environment..."
	rm -rf testing_virt
fi

# Install system dependencies
if [ -f /etc/debian_version ] ; then
	echo "Detected Ubuntu/Debian system"
	sudo apt-get update
	sudo apt-get install -y gcc python3 python3-dev python3-pip python3-venv \
		libyaml-dev git xvfb firefox
elif [ -f /etc/redhat-release ] ; then
	echo "Detected CentOS/RHEL system"
	sudo yum install -y gcc python3-devel libyaml-devel git xorg-x11-server-Xvfb firefox
fi

echo ""
echo "Building Python virtual environment..."
mkdir -p testing_virt
cd testing_virt

# Create virtual environment using Python 3's built-in venv
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies from requirements.txt
echo "Installing Python dependencies..."
cd "$ROOT"
pip install -r requirements.txt

echo ""
echo "============================"
echo "✓ Installation Complete!"
echo "============================"
echo ""
echo "Next steps:"
echo "1. Configure environment variables:"
echo "   export ALFRESCO_USER=admin"
echo "   export ALFRESCO_PASSWORD=your_password"
echo ""
echo "2. Or copy config.yml.example to config.yml and edit it"
echo ""
echo "3. Run tests:"
echo "   ./runtests.sh ./testing_virt/venv/bin"
echo ""

