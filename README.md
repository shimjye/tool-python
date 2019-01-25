# tool-python

## install pyenv
  - https://gist.github.com/perhapsspy/b1d5c175e2c40a1ad21e8e7ec29e8b88
  - http://guswnsxodlf.github.io/pyenv-virtualenv-autoenv

### Pyenv 설치 (https://github.com/yyuu/pyenv-virtualenv)
```
brew install pyenv-virtualenv
```

### ~/.bash_profile 파일에 아래 내용 추가
```
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

### 사용할 Python 버전을 미리 깔고
```
pyenv install 3.7.2
```

### 가상환경을 만듬
```
pyenv virtualenv 3.7.2 project_venv_name
```

### 프로젝트를 하나 만들고 
```
mkdir project_name
cd project_name
```

### 이 프로젝트 디렉토리에 접근할때 알아서 가상환경 활성화/비활성화 시키기 (.python-version 파일이 생성됨 적절히 .gitignore 등에 넣어줍시다.)
```
pyenv local project_venv_name 
```

### +@ 자주 쓰는 다른 명령
```
pyenv versions  # 설치된 버전 + 가상환경 목록
pyenv install --list  # 설치 가능한 Python 버전 
pyenv uninstall project_venv_name  # 가상환경 삭제
pyenv global version_or_venv_name  # 전역 설정 
pyenv activate pytest (가상환경명)
pyenv deactivate
```


## setting module
- install requests
  - sudo pip install requests
