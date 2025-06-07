python -m pip install --upgrade pip
pip install -r requirements.txt
cp pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
brew update
brew install postgresql@16
export PATH="/opt/homebrew/opt/postgresql@16/bin:$PATH"
